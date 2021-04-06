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

cleanup ()
{
	trun "multipathd disablequeueing maps"
	trun "service multipathd stop"
	sleep 5
	trun "udevadm settle"
	trun "multipath -F"
	sleep 5
	trun "modprobe -r scsi_debug"
}

tlog "running $0"

# which not set find_multipaths yes, so multipath always create a multipath device for single device
# so stop service and reconfig with  --find_multipaths y, and reload/start the service again. 
rpm -q device-mapper-multipath || yum install -y device-mapper-multipath

# test with find_multipath=y, will not multipath for the single device; reload/start the service to enable the config
cleanup
trun "rm -f /etc/multipath.conf"
trun "mpathconf --enable --user_friendly_names y --find_multipaths y --with_multipathd n"
sed -i '/^blacklist[[:space:]]*{/ a\
	device {\n              vendor ".*"\n           product ".*"\n  }
' /etc/multipath.conf
if grep -qw blacklist_exceptions /etc/multipath.conf ; then
	sed -i '/^blacklist_exceptions[[:space:]]*{/ a\
	device {\n              vendor Linux\n          product scsi_debug\n    }
' /etc/multipath.conf
else
	cat << _EOF_ >> /etc/multipath.conf
blacklist_exceptions {
	device {
		vendor Linux
		product scsi_debug
	}
}
_EOF_
fi
trun "service multipathd start"
trun "modprobe scsi_debug"
sleep 5
trun "multipath -W"
cat /etc/multipath/wwids
trun "multipath"
disk_path=$(get_scsi_debug_devices)
disk_node=$(basename $disk_path)
mpath_name=$(get_mpath_disk_by_scsi_device $disk_node)
tok '[[ $mpath_name = "[orphan]" ]]'

# test with find_multipath=n, will multipath for the single device
trun "mpathconf --user_friendly_names y --find_multipaths n --with_multipathd y"
sleep 5
mpath_name=$(get_mpath_disk_by_scsi_device $disk_node)
tok "is_mpath $mpath_name"

# flush new created path
trun "multipath -F"
sleep 1

# test with find_multipath=y, A path has the same WWID as a multipath device that was previously created
trun "mpathconf --user_friendly_names y --find_multipaths y --with_multipathd y"
sleep 5
mpath_name=$(get_mpath_disk_by_scsi_device $disk_node)
tok "is_mpath $mpath_name"
trun "multipath -F"
sleep 1

# Clear wwid, test with find_multipath=y, will not multipath for the single device
trun "multipath -W"
trun "service multipathd reload"
sleep 5
mpath_name=$(get_mpath_disk_by_scsi_device $disk_node)
tok '[[ $mpath_name = "[orphan]" ]]'

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

cleanup
trun "multipath -W"
cat /etc/multipath/wwids
tend
