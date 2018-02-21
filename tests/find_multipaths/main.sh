#!/bin/bash

# Copyright (c) 2016 Red Hat, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Author: Lin Li   <lilin@redhat.com>

#set -x
source ../include/ec.sh || exit 200

tlog "running $0"

# which not set find_multipaths yes, so multipath always create a multipath device for single device
# so stop service and reconfig with  --find_multipaths y, and reload/start the service again. 
trun "service multipathd stop"
rpm -q device-mapper-multipath || yum install -y device-mapper-multipath

# test with find_multipath=y, will not multipath for the single device; reload/start the service to enable the config
trun "mpathconf --enable --user_friendly_names y --find_multipaths y --with_multipathd y"
trun "service multipathd status"
# use scsi_debug to simulate a drive
trun "multipath -F"
terr "modprobe -r scsi_debug"
trun "modprobe scsi_debug"
sleep 3
trun "multipath -W"
cat /etc/multipath/wwids
trun "multipath"
disk_path=$(get_scsi_debug_devices)
disk_node=$(basename $disk_path)
mpath_name=$(get_mpath_disk_by_scsi_device $disk_node)
tok '[[ -z $mpath_name ]]'

# test with find_multipath=n, will multipath for the single device
trun "mpathconf --enable --user_friendly_names y --find_multipaths n --with_multipathd y"
sleep 5
trun "multipath"
mpath_name=$(get_mpath_disk_by_scsi_device $disk_node)
tok "is_mpath $mpath_name"

# flush new created path
sleep 3
trun "multipath -F"
sleep 3

# test with find_multipath=y, A path has the same WWID as a multipath device that was previously created
trun "mpathconf --enable --user_friendly_names y --find_multipaths y --with_multipathd y"
sleep 5
trun "multipath"
mpath_name=$(get_mpath_disk_by_scsi_device $disk_node)
tok "is_mpath $mpath_name"

# Clear wwid, test with find_multipath=y, will not multipath for the single device
trun "multipath -W"
trun "mpathconf --disable --with_multipathd y"
sleep 5
mpath_name=$(get_mpath_disk_by_scsi_device $disk_node)
tok '[[ -z $mpath_name ]]'

trun "multipath -F"
sleep 5
trun "modprobe -r scsi_debug"

# test find_multipaths=y create device for paths have same wwid
tok "modprobe scsi_debug num_tgts=1 vpd_use_hostno=0 add_host=2 delay=20 max_luns=2 no_lun_0=1"
sleep 10
disk_paths=$(get_scsi_debug_devices)
disk_node=$(basename $disk_paths)
mpath_name=$(get_mpath_disk_by_scsi_device $disk_node)
tok "is_mpath $mpath_name"

sleep 10

trun "multipath -F"
sleep 5
trun "modprobe -r scsi_debug"
# remove the scsi_debug wwid
trun "service multipathd stop"
sleep 3
trun "multipath -W"
cat /etc/multipath/wwids
tend
