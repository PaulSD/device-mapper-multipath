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

source ../include/ec.sh || exit 200

tlog "start running"
Result=FAILED
MulDevice=`rpm -qa|grep device-mapper-multipath | wc -l`
if [ $MulDevice != 2 ]; then
	tlog "multi-device is not install"
	exit 1
fi
tlog "multi-device is installed"
trun "mpathconf --enable --find_multipaths n --with_module y --with_multipathd y"
trun "echo '' > /var/log/messages"
trun "multipath -F"
trun "modprobe -r scsi_debug"
trun "dmsetup remove_all"
OriginalDev=`multipathd show paths | grep "running" | awk '{print $2}'`
OLD_IFS="$IFS"
IFS=" "
OriginalDevList=($OriginalDev)
IFS="$OLD_IFS"


#trun "service multipathd restart" 
OriPathCount=`multipathd show paths | grep -i "running" |grep -v grep|wc -l`
tlog "Original MultPathDevice = ${OriPathCount}"
trun "modprobe scsi_debug vpd_use_hostno=0 add_host=2 dev_size_mb=1024"
trun "multipath -ll"
sleep 1s
OriPathCount=`multipathd show paths | grep -i "running" |grep -v grep|wc -l`
tlog "After add tow virturl device, MultPathDevice = ${OriPathCount}"

if [ $OriPathCount -eq  0 ];then
	tlog "Virtual MultiPath is Fail"
	exit 1
fi

tlog "offline one MultiPathDevice"
DeviceName=`multipath -ll | grep -i "sd[a|b|c|d|e|f|g|h]" | awk -F" " '{print $3}' | tail -1`
trun "echo 'offline' > /sys/block/${DeviceName}/device/state"
sleep 1s
trun "multipath -ll"
sleep 1s
trun "multipath -r"
sleep 1s
trun "multipathd show paths"
sleep 5s
MulPathCount=`multipathd show paths | grep -i "running" |grep -v grep|wc -l`
let "RightPathCout=$OriPathCount-1"
if [ $MulPathCount != $RightPathCout ]; then
	Result=FAIL
	tlog "second check fail MulPathCount=$MulPathCount  RightPathCout=$RightPathCout"
	tlog "running result $Result"
	exit 1
fi
tlog "second check is OK MulPathCount=$MulPathCount"

tlog "running one Multipath"
trun "echo 'running' > /sys/block/${DeviceName}/device/state"
sleep 1s
trun "multipath -ll"
sleep 4s
#verified
Condition1=`grep "reinstate failed" /var/log/messages | wc -l`
Condition2=`grep "segfault" /var/log/messages | wc -l`
trun "service multipathd status > tmp_file"
Condition3=`grep " DM message failed" tmp_file | wc -l`

trun "multipath -F"
trun "modprobe -r scsi_debug"
trun "dmsetup remove_all"

trun "rm -f tmp_file"
tlog "Condition1=${Condition1}  Condition2=${Condition2} Condition3=${Condition3}"
RESULT=PASS
[[ $Condition1 -eq 1 ]]&&[[ $Condition2 -eq 1 ]]&&[[ $Condition3 -eq 1 ]]&&RESULT=FAIL
echo "Test Result =  $RESULT"
[[ $RESULT = "FAIL" ]]&&exit 1
exit 0

