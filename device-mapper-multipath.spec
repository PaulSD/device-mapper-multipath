Summary: Tools to manage multipath devices using device-mapper.
Name: device-mapper-multipath
Version: 0.4.2
Release: 1.0
License: GPL
Group: System Environment/Base
URL: http://christophe.varoqui.free.fr/
Source0: multipath-tools-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
#BuildRequires: device-mapper >= 1.01
#BuildRequires: libselinux-devel
#BuildRequires: dlm
#Requires: lvm2 >= 2.01
#ExcludeArch: s390 s390x ppc
#%define _exec_prefix /usr

%description
%{name} provides tools to manage multipath devices by instructing the 
device-mapper multipath kernel module what to do. 
The tools are :
* multipath :   Scan the system for multipath devices and assemble them.
* multipathd :  Detects when paths fail and execs multipath to update things.
* kpartx :      Makes multipath devices partitionable.

%prep
%setup -q -n multipath-tools-%{version}

%build
#%configure --with-clvmd=all --with-cluster=shared --with-user= --with-group=
make DESTDIR=$RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

#mkdir -p -m755 $RPM_BUILD_ROOT/etc/rc.d/init.d
#install scripts/clvmd_init_rhel4 $RPM_BUILD_ROOT/etc/rc.d/init.d/clvmd

%clean
rm -rf $RPM_BUILD_ROOT

#%post
#/sbin/chkconfig --add clvmd

#%preun
#if [ "$1" = 0 ]; then
#        /sbin/chkconfig --del clvmd
#fi

%files
%defattr(-,root,root,-)
/sbin/multipath
/sbin/kpartx
/sbin/multipathd
%{_mandir}/man8/multipath.8.gz
%config /etc/hotplug.d/scsi/multipath.hotplug
%config /etc/rc.d/init.d/multipathd

%changelog
* Tue Mar 01 2005 Alasdair Kergon <agk@redhat.com> - 0.4.2-1.0
- Initial import based on Christophe Varoqui's spec file.
