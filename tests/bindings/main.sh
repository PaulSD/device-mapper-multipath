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

trun "service multipathd stop"
rpm -q device-mapper-multipath || yum install -y device-mapper-multipath
trun "mpathconf --enable --with_multipathd y --user_friendly_names y"
trun "service multipathd status"

trun "multipath -F"
sleep 5
terr "modprobe -r scsi_debug"
terr "modprobe scsi_debug dev_size_mb=1024 num_tgts=1 vpd_use_hostno=0 \
add_host=2 delay=20 max_luns=2 no_lun_0=1"
sleep 60 

disk_path=$(get_scsi_debug_devices)
disk=$(basename $disk_path)
mpath_name=$(get_mpath_disk_by_scsi_device $disk)
new_alias="mpath_test_$$"

trun "sed -i 's/$mpath_name/$new_alias/' /etc/multipath/bindings"
trun "multipath -r"
sleep 5
tok "[[ -b /dev/mapper/$new_alias ]]"
tok is_mpath $new_alias

trun "multipath -F"
sleep 5
trun "modprobe -r scsi_debug"
trun "service multipathd stop"
sleep 3
trun "multipath -W"
tend
