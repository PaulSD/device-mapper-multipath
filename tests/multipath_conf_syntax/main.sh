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


# Include Beaker environment
. /usr/bin/rhts-environment.sh || exit 1
. /usr/share/beakerlib/beakerlib.sh || exit 1

PACKAGE="device-mapper-multipath"

rlJournalStart
    rlPhaseStartSetup
        rlAssertRpm $PACKAGE
	rlRun "multipath -F; sleep 5"
        rlRun "modprobe -r scsi_debug" 0 "Remove if scsi_debug load before"
	rlRun "rm -f /etc/multipath.conf"
        rlRun "mpathconf --enable --with_module y --with_multipathd y --find_multipaths n" 0 "Set up multipath"
        rlServiceStart multipathd
	rlRun "cp /etc/multipath.conf /etc/multipath.conf.bak" 0 "Backup /etc/multipath.conf first"
    rlPhaseEnd

    rlPhaseStartTest
        rlRun "modprobe scsi_debug"
        sleep 5
        rlLogInfo "`multipath -ll`"
	wwid=`multipathd show maps format %w | grep -v uuid`
	# test missing closing quote on alias
	cat << _EOF_ >> /etc/multipath.conf 
multipaths {
  multipath {
	wwid "$wwid" 
	alias "mypath
  }
}
_EOF_
	rlRun "multipath 2>&1 | grep 'missing closing quotes on line'" 0 "test missing closing quote on alias"
	rlRun "multipath -r |grep mypath" 0 "mpath rename to mypath"

	# test no value for alias
	rlRun "sed -i 's/alias.*$/alias/g' /etc/multipath.conf"
	rlRun "multipath 2>&1 | grep \"missing value for option 'alias' on line\"" 0 "test no value for alias"
	rlRun "multipath -r |grep mpath*" 0 "mpath rename to mpath* from mypath"

	# test missing starting quote on alias
	rlRun "sed -i 's/alias.*$/alias mypath\"/g' /etc/multipath.conf"
	rlRun "multipath 2>&1 |grep 'ignoring extra data starting with'" 0 "test missing starting quote on alias"
	rlRun "multipath -r |grep mypath" 0 "mpath rename to mypath"

	# test wrong quote on alias
	rlRun "sed -i 's/alias.*$/alias <mypath>/g' /etc/multipath.conf"
	rlRun "multipath 2>&1 | grep config" 1 "no warning"	
	rlRun "multipath -r |grep '<mypath>'" 0 "mpath rename to <mypath>"

	# test value has a space
	rlRun "sed -i 's/alias.*$/alias mypath test/g' /etc/multipath.conf"
	rlRun "multipath 2>&1 |grep 'ignoring extra data starting with'" 0 "test value has a space"
	rlRun "multipath -r |grep mypath" 0 "mpath rename to mypath"

	# test wrong alias keyword
	rlRun "sed -i 's/alias.*$/alia mypath/g' /etc/multipath.conf"
	rlRun "multipath 2>&1 |grep 'invalid keyword: alia'" 0 "invalid keyword: alia"
	rlRun "multipath -r |grep mpath*" 0 "mpath rename to mpath* from mypath"
	rlRun "sed -i 's/alia.*$/alias mypath/g' /etc/multipath.conf"

	# test no space between the section name and the open bracket that followed it	
	# fix issue about if a section doesn't have a space between the section name and the open bracket, that section isn't read in.
	rlRun "sed -i 's/multipaths.*/multipaths{/g' /etc/multipath.conf"
	rlRun "multipath 2>&1 | grep config" 1 "no warning"
	rlRun "multipath -r |grep mypath" 0 "mpath rename to mypath"

	# test wrong section keywords
	rlRun "sed -i 's/multipaths.*/ultipaths {/g' /etc/multipath.conf"
	rlRun "multipath 2>&1 | grep 'invalid keyword: ultipaths'" 0 "test wrong multipaths section keyword"
	rlRun "sed -i 's/defaults.*/efaults {/g' /etc/multipath.conf"
	rlRun "multipath 2>&1 | grep 'invalid keyword: efaults'" 0 "test wrong defaults section keyword"
	rlRun "sed -i 's/blacklist {/lacklist {/g' /etc/multipath.conf"
	rlRun "multipath 2>&1 | grep 'invalid keyword: lacklist'" 0 "test wrong blacklist section keyword"

    rlPhaseEnd

    rlPhaseStartCleanup
        rlRun "multipath -F" 0 "Flush all unused multipath device maps"
        rlServiceStop multipathd
        rlRun "modprobe -r scsi_debug" 0 "Remove scsi_debug"
	rlRun "cp -f /etc/multipath.conf.bak /etc/multipath.conf" 0 "Recovery /etc/multipath.conf"
    rlPhaseEnd
rlJournalPrintText
rlJournalEnd
