Summary: Tools to manage multipath devices using device-mapper.
Name: device-mapper-multipath
Version: 0.4.5
Release: 9.1.1
License: GPL
Group: System Environment/Base
URL: http://christophe.varoqui.free.fr/
Source0: multipath-tools-0.4.5.52.tgz
Patch0: fedora.patch
Obsoletes: kpartx = 0.4.4-2.4
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: sysfsutils-devel, device-mapper >= 1.02.02-2

%description
%{name} provides tools to manage multipath devices by instructing the 
device-mapper multipath kernel module what to do. 
The tools are :
* multipath :   Scan the system for multipath devices and assemble them.
* multipathd :  Detects when paths fail and execs multipath to update things.

%prep
%setup -q -n multipath-tools-0.4.5.52

%patch0 -p1

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
/sbin/kpartx
/sbin/kpartx.static
/sbin/multipath
/sbin/multipath.static
/sbin/multipathd
/sbin/mpath_prio_alua
/sbin/mpath_prio_emc
/sbin/mpath_prio_netapp
/etc/udev/rules.d/40-multipath.rules
%{_mandir}/man8/mpath_prio_alua.8.gz
%{_mandir}/man8/kpartx.8.gz
%{_mandir}/man8/multipath.8.gz
%{_mandir}/man8/multipathd.8.gz
%config /etc/rc.d/init.d/multipathd
%config(noreplace) /etc/multipath.conf
%doc AUTHOR COPYING README* FAQ Multipath-usage.txt multipath.conf.annotated multipath.conf.defaults multipath.conf.synthetic
/var/cache/multipath

%changelog
* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.4.5-9.1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Dec 19 2005 Benjamin Marzinski <bmarzins@redhat.com> - 0.4.5-9.1
- added patch for fedora changes

* Fri Dec 16 2005 Benjamin Marzinski <bmarzins@redhat.com> - 0.4.5-9.0
- Updated to latest upstream source (t)_4_5_post52)

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sun Dec  4 2005 Peter Jones <pjones@redhat.com> - 0.4.4-2.6
- rebuild for newer libs

* Tue Nov 15 2005 Peter Jones <pjones@redhat.com> - 0.4.4-2.5
- unsplit kpartx.  parted knows how to do this now, so we don't
  need this in a separate package.

* Tue Nov 15 2005 Peter Jones <pjones@redhat.com> - 0.4.4-2.4
- split kpartx out into its own package

* Fri May 06 2005 Bill Nottingham <notting@redhat.com> - 0.4.4-2.3
- Fix last fix.

* Thu May 05 2005 Alasdair Kergon <agk@redhat.com> - 0.4.4-2.2
- Fix last fix.

* Wed May 04 2005 Alasdair Kergon <agk@redhat.com> - 0.4.4-2.1
- By default, disable the multipathd service.

* Tue Apr 19 2005 Alasdair Kergon <agk@redhat.com> - 0.4.4-2.0
- Fix core dump from last build.

* Tue Apr 19 2005 Alasdair Kergon <agk@redhat.com> - 0.4.4-1.0
- Move cache file into /var/cache/multipath.

* Fri Apr 08 2005 Alasdair Kergon <agk@redhat.com> - 0.4.4-0.pre8.1
- Remove pp_balance_units.

* Mon Apr 04 2005 Alasdair Kergon <agk@redhat.com> - 0.4.4-0.pre8.0
- Incorporate numerous upstream fixes.
- Update init script to distribution standards.

* Tue Mar 01 2005 Alasdair Kergon <agk@redhat.com> - 0.4.2-1.0
- Initial import based on Christophe Varoqui's spec file.
