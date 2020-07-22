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
# along with this program.  If not, see <http://www.gnu.cp /etc/multipath.conf /etc/multipath.conf.$$org/licenses/>.

# Author: Lin Li   <lilin@redhat.com>

source ../include/ec.sh || exit 200

tlog "running $0"

trun "rpm -q device-mapper-multipath || yum install -y device-mapper-multipath"
trun "mpathconf --enable --with_multipathd y --user_friendly_names y"

# backup the /etc/multipath.conf
trun "cp /etc/multipath.conf /etc/multipath.conf.$$"
trun "multipath -F"

trun "modprobe scsi_debug num_tgts=1 vpd_use_hostno=0 add_host=2 delay=20 \
max_luns=2 no_lun_0=1"
trun "multipath"
# wwid shown slowly on s390x by the script framework, but normally when run by multipath command directly
# so extend sleep time 
sleep 20

disk=$(get_scsi_debug_devices)
disk=$(basename $disk)
wwid=$(get_wwid_of_disk $disk)
mpath=$(get_mpath_disk_by_scsi_device $disk)

# user_friendly_names = yes and mpath=test
#cur_dir=/mnt/tests/kernel/storage/multipath/user_friendly_names/
#cur_dir=/home/test/scratch/device-mapper-multipath/user_friendly_names
trun "cat multipath.conf.yes | sed "s/your_wwid/$wwid/g" > /etc/multipath.conf"
trun "cat -n /etc/multipath.conf"
trun "multipath -r"
echo ">>> Verify 'test ($wwid)' is present ..."
trun "multipath -ll"
tok "multipath -ll | egrep \"^test\""

# user_friendly_names = no
trun "cat multipath.conf.no > /etc/multipath.conf"
trun "multipath -r"
echo ">>> Verify 'test' is gone but '$wwid' present ..."
trun "multipath -ll"
tok "multipath -ll | egrep \"^$wwid\""
sleep 10
tok "multipath -F $wwid"
sleep 10
trun "modprobe -r scsi_debug"

trun "cp /etc/multipath.conf.$$ /etc/multipath.conf"
trun "multipath -F; multipath"
tend
