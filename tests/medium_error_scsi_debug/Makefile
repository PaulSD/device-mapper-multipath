# Copyright (c) 2006 Red Hat, Inc. This copyrighted
# material is made available to anyone wishing to use, modify, copy, or
# redistribute it subject to the terms and conditions of the GNU General
# Public License v.2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# Author: LiLin <lilin@redhat.com>


.PHONY: all install download clean

BUILT_FILES=

FILES=$(METADATA)  Makefile PURPOSE main.sh

run: $(FILES) build
	./main.sh

build: $(BUILT_FILES)
	chmod a+x ./main.sh

clean:
	rm -f *~ *.rpm $(BUILT_FILES)

include /usr/share/rhts/lib/rhts-make.include

$(METADATA): Makefile
	@touch $(METADATA)
	@echo "Owner:        LiLin <lilin@redhat.com>" > $(METADATA)
	@echo "Name:         $(TEST)" >> $(METADATA)
	@echo "Path:         $(TEST_DIR)"	>> $(METADATA)
	@echo "License:      GPLv3" >> $(METADATA)
	@echo "TestVersion:  $(TESTVERSION)"	>> $(METADATA)
	@echo "Description:  CEE feedback" >> $(METADATA)
	@echo "TestTime:     15m" >> $(METADATA)
	@echo "RunFor:       device-mapper-multipath" >> $(METADATA)
	@echo "Requires:     device-mapper-multipath" >> $(METADATA)

	rhts-lint $(METADATA)
