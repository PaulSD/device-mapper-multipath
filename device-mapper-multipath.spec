Summary: Tools to manage multipath devices using device-mapper.
Name: device-mapper-multipath
Version: 0.4.4
Release: 0.pre8.0
License: GPL
Group: System Environment/Base
URL: http://christophe.varoqui.free.fr/
Source0: multipath-tools-0.4.4-pre8.tar.bz2
Patch0: old_dev_t_long.patch
Patch1: old_dev_t_int.patch
Patch2: old_dev_t_short.patch
Patch3: makefile.patch
Patch4: kpartx_endian.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: sysfsutils-devel,device-mapper

%description
%{name} provides tools to manage multipath devices by instructing the 
device-mapper multipath kernel module what to do. 
The tools are :
* multipath :   Scan the system for multipath devices and assemble them.
* multipathd :  Detects when paths fail and execs multipath to update things.
* kpartx :      Makes multipath devices partitionable.

%prep
%setup -q -n multipath-tools-0.4.4-pre8

%ifarch ppc64 x86_64
%patch0 -p1
%endif

%ifarch ppc ia64
%patch1 -p1
%endif

%ifarch i386 s390 s390x
%patch2 -p1
%endif

%patch3 -p1
%patch4 -p1

%build
make DESTDIR=$RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT bindir=/sbin rcdir=/etc/rc.d/init.d

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add multipathd

%preun
if [ "$1" = 0 ]; then
        /sbin/chkconfig --del multipathd
fi

%files
%defattr(-,root,root,-)
/sbin/multipath
/sbin/kpartx
/sbin/multipathd
/sbin/pp_balance_units
%{_mandir}/man8/kpartx.8.gz
%{_mandir}/man8/multipath.8.gz
%{_mandir}/man8/multipathd.8.gz
%config /etc/rc.d/init.d/multipathd
%doc AUTHOR COPYING README* FAQ multipath.conf.* multipath/01_udev multipath/02_multipath multipath/multipath.dev

%changelog
* Mon Apr 04 2005 Alasdair Kergon <agk@redhat.com> - 0.4.4-0.pre8.0
- Incorporate numerous upstream fixes.
- Update init script to distribution standards.

* Tue Mar 01 2005 Alasdair Kergon <agk@redhat.com> - 0.4.2-1.0
- Initial import based on Christophe Varoqui's spec file.
