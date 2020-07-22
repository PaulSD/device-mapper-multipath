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
    sleep 5
    udevadm settle
    multipath -F
    sleep 5
    modprobe -r scsi_debug    

    return 0
}

yum -y install device-mapper device-mapper-multipath
mpathconf --enable
service multipathd stop
modprobe scsi_debug num_tgts=1 vpd_use_hostno=0 add_host=2 delay=20  max_luns=2 no_lun_0=1 opts=2
sleep 5
multipath > /dev/null
sleep 5
mpathdev=`multipath -l | grep scsi_debug | awk '{print $1}' | head -1`
if [ -z "$mpathdev" ]; then
	echo "------- FAIL, no multipath device created -----"
	cleanup
	exit 1
fi
before_active=`multipath -l $mpathdev | grep "active undef" | wc -l`

IO_error=`dd if=/dev/zero of=/dev/mapper/$mpathdev bs=1024 seek=2330 count=10 2>&1 | grep -o "Input/output error" `
if [ -n "$IO_error" ];then
	after_active=`multipath -l $mpathdev | grep "active undef" | wc -l`
	if [ "$before_active" -eq "$after_active" ]; then
		echo "------- PASS,  a medium error, correctly generated an I/O error and did not fail paths -----"
		cleanup
		exit 0
	else
		echo "------- FAIL, paths failed -----"
		cleanup
		exit 1
	fi
else
	echo "------- FAIL, did not generate an I/O error -----"
	cleanup
	exit 1
fi
