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

# Author: LiLin <lilin@redhat.com>

function cleanup()
{
    multipath -F
    service multipathd stop 
    sleep 15
    modprobe -r scsi_debug    
    rt=$?
    while [ $rt -ne 0 ]
    do
	sleep 15
	modprobe -r scsi_debug
        rt=$?
    done
}

yum -y install device-mapper device-mapper-multipath
mpathconf --enable
modprobe scsi_debug  dev_size_mb=1024 num_tgts=1 vpd_use_hostno=0 add_host=2 delay=20  max_luns=2 no_lun_0=1 opts=2 every_nth=1
sleep 5
service multipathd restart
sleep 10
disk1=`multipath -ll | grep -A 5 scsi_debug | grep -oE "sd." | head -1`
if [ -z "$disk1" ]; then
	cleanup
	exit 1
fi

IO_error=`dd if=/dev/zero of=/dev/$disk1 bs=1024 count=262144 2>&1 | grep -o "Input/output error" `
if [ -n "$IO_error" ];then
	echo "------- PASS,  a medium error, correctly generate an I/O error and do not get infinitely retried -----"
	cleanup
else
	echo "------- FAIL, not generate an I/O error -----"
	cleanup
	exit -1
fi
