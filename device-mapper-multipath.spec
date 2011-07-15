Summary: Tools to manage multipath devices using device-mapper
Name: device-mapper-multipath
Version: 0.4.9
Release: 16%{?dist}
License: GPL+
Group: System Environment/Base
URL: http://christophe.varoqui.free.fr/

Source0: multipath-tools-091027.tar.gz
Source1: multipath.conf
# patch that should go upstream
Patch1: 0001-for-upstream-add-tpg_pref-prioritizer.patch
Patch2: 0002-for-upstream-add-tmo-config-options.patch
Patch3: 0003-for-upstream-default-configs.patch
# local patches
Patch1001: 0001-RH-queue-without-daemon.patch
Patch1002: 0002-RH-path-checker.patch
Patch1003: 0003-RH-root-init-script.patch
Patch1004: 0004-RH-fix-kpartx.patch
Patch1005: 0005-RH-cciss_id.patch
Patch1006: 0006-RH-move-bindings.patch
Patch1007: 0007-RH-do-not-remove.patch
Patch1008: 0008-RH-Make-build-system-RH-Fedora-friendly.patch
Patch1009: 0009-RH-multipathd-blacklist-all-by-default.patch
Patch1010: 0010-RH-multipath-rules-udev-changes.patch
Patch1011: 0011-RH-fix-init-script-LSB-headers.patch
Patch1012: 0012-RH-udev-sync-support.patch
Patch1013: 0013-RH-add-weighted_prio-prioritizer.patch
Patch1014: 0014-RH-add-hp_tur-checker.patch
Patch1015: 0015-RH-add-multipathd-count-paths-cmd.patch
Patch1016: 0016-RHBZ-554561-fix-init-error-msg.patch
Patch1017: 0017-RHBZ-554592-man-page-note.patch
Patch1018: 0018-RHBZ-554596-SUN-6540-config.patch
Patch1019: 0019-RHBZ-554598-fix-multipath-locking.patch
Patch1020: 0020-RHBZ-554605-fix-manual-failover.patch
Patch1021: 0021-RHBZ-548874-add-find-multipaths.patch
Patch1022: 0022-RHBZ-557845-RHEL5-style-partitions.patch
Patch1023: 0023-RHBZ-557810-emc-invista-config.patch
Patch1024: 0024-RHBZ-565933-checker-timeout.patch
Patch1025: 0025-RHBZ-508827-update-multipathd-manpage.patch
Patch1026: 0026-RHBZ-549636-default-path-selector.patch
Patch1027: 0027-RHBZ-509443-enhance-show-config.patch
Patch1028: 0028-RHBZ-452617-add-revision-parameter.patch
Patch1029: 0029-RHBZ-567219-recalculate-pgs-in-checkerloop.patch
Patch1030: 0030-RHBZ-558636-check-if-multipath-owns-path.patch
Patch1031: 0031-RHBZ-570546-display-avg-pg-prio.patch
Patch1032: 0032-RHBZ-575767-ontap_prio.patch
Patch1033: 0033-RHBZ-573715-eurologic-config.patch
Patch1034: 0034-RHBZ-579575-add-q-multipath-option.patch
Patch1035: 0035-RHBZ-467709-add-followover.patch
Patch1036: 0036-RH-clear-messages.patch
Patch1037: 0037-RH-adopt-paths.patch
Patch1038: 0038-RHBZ-587201-IBM-SGI.patch
Patch1039: 0039-RHBZ-589153-manpage-update.patch
Patch1040: 0040-RHBZ-587695-add-checker-msg-alias.patch
Patch1041: 0041-RHBZ-587695-add-rdac-message.patch
Patch1042: 0042-RHBZ-590038-fix-fast-io-fail-tmo.patch
Patch1043: 0043-RHBZ-590028-close-sysfs_attr_fd.patch
Patch1044: 0044-RHBZ-591940-dont-clear-daemon.patch
Patch1045: 0045-RHBZ-593379-dont-add-unknown-paths.patch
Patch1046: 0046-RHBZ-593426-move-adopt-path.patch
Patch1047: 0047-RHBZ-591608-only-switch-pgs-once.patch
Patch1048: 0048-RHBZ-592494-fix-user-configs.patch
Patch1049: 0049-RHBZ-591644-enhance-mpathconf.patch
Patch1050: 0050-RHBZ-595400-fix-checker-tmo.patch
Patch1051: 0051-RHBZ-596156-mpathconf-man-page.patch
Patch1052: 0052-RHBZ-601247-fix-path-adoption.patch
Patch1053: 0053-RHBZ-596323-remember_more_wwids.patch
Patch1054: 0054-RHBZ-596319-rules-cleanup.patch
Patch1055: 0055-RHBZ-602257-update-on-show-topology.patch
Patch1056: 0056-RHBZ-603812-better-type-check.patch
Patch1057: 0057-RHBZ-607869-fix-resize.patch
Patch1058: 0058-RHBZ-601665-assemble-features.patch
Patch1059: 0059-RHBZ-607874-handle-offlined-paths.patch
Patch1060: 0060-RHBZ-606420-fix-remove-map.patch
Patch1061: 0061-RHBZ-620479-find-rport.patch
Patch1062: 0062-RHBZ-592998-hpsc-config.patch
Patch1063: 0063-RHBZ-595719-udev_link_priority.patch
Patch1064: 0064-RHBZ-612173-fix-reverse-lookup.patch
Patch1065: 0065-RHBZ-635088-update-priority.patch
Patch1066: 0066-RHBZ-636071-mpathconf-variable_names.patch
Patch1067: 0067-RHBZ-622569-symmetrix-config.patch
Patch1068: 0068-RHBZ-632734-nvdisk-config.patch
Patch1069: 0069-RHBZ-636246-hp-open-config.patch
Patch1070: 0070-RHBZ-639037-hitachi-open-config.patch
Patch1071: 0071-RHBZ-611779-fix-whitespace-crash.patch
Patch1072: 0072-RHBZ-651389-change-scsi-tmo-order.patch
Patch1073: 0073-RHBZ-650664-clarify-error-msg.patch
Patch1074: 0074-RHBZ-602883-dont-print-change.patch
Patch1075: 0075-RHBZ-576919-log-checker-err.patch
Patch1076: 0076-RHBZ-599690-update-multipath-conf.patch
Patch1077: 0077-RHBZ-622608-nvdisk-config.patch
Patch1078: 0078-RHBZ-628095-config-warnings.patch
Patch1079: 0079-RHBZ-650797-display-iscsi-tgt-name.patch
Patch1080: 0080-RHBZ-662731-fix-no-config-value-segfault.patch
Patch1081: 0081-RHBZ-623644-fix-sysfs-caching.patch
Patch1083: 0083-RHBZ-636213-633643-new-configs.patch
Patch1084: 0084-RHBZ-644111-read-only-bindings.patch
Patch1085: 0085-RHBZ-645605-fix-offline-check.patch
Patch1086: 0086-RHBZ-681144-sysfs-device-cleanup.patch
Patch1087: 0087-RHBZ-680480-skip-if-no-sysdev.patch
Patch1088: 0088-RHBZ-693524-fix-prio-segfault.patch
Patch1089: 0089-RHBZ-694602-RSSM-config.patch
Patch1090: 0090-RHBZ-700169-fix-nr-active.patch
Patch1091: 0091-RHBZ-699577-manpage-clarification.patch
Patch1092: 0092-RHBZ-689504-rdac-retry.patch
Patch1093: 0093-RHBZ-677449-dont-remove-map-on-enomem.patch
Patch1094: 0094-RHBZ-707560-check-return-value.patch
Patch1095: 0095-RHBZ-678673-no-path-groups.patch
Patch1096: 0096-RHBZ-683616-ioship-support.patch
Patch1097: 0097-RHBZ-697386-fix-shutdown-crash.patch
Patch1098: 0098-RHBZ-706555-dont-update-pgs-in-manual.patch
Patch1099: 0099-RHBZ-705854-warn-on-bad-dev-loss-tmo.patch
Patch1100: 0100-RHBZ-710478-deprecate-uid-gid-mode.patch
Patch1101: 0101-RHBZ-631009-disable-udev-disk-rules-on-reload.patch
Patch1102: 0102-RHBZ-690828-systemd-unit-file.patch

# runtime
Requires: %{name}-libs = %{version}-%{release}
Requires: kpartx = %{version}-%{release}
Requires: device-mapper >= 1.02.39-1
Requires: udev initscripts
Requires(post): systemd-units systemd-sysv chkconfig
Requires(preun): systemd-units
Requires(postun): systemd-units

# build/setup
BuildRequires: libaio-devel, device-mapper-devel >= 1.02.39-1
BuildRequires: libselinux-devel, libsepol-devel
BuildRequires: readline-devel, ncurses-devel
BuildRequires: systemd-units

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
%{name} provides tools to manage multipath devices by
instructing the device-mapper multipath kernel module what to do. 
The tools are :
* multipath - Scan the system for multipath devices and assemble them.
* multipathd - Detects when paths fail and execs multipath to update things.

%package libs
Summary: The %{name} modules and shared library
License: GPL+
Group: System Environment/Libraries

%description libs
The %{name}-libs provides the path checker
and prioritizer modules. It also contains the multipath shared library,
libmultipath.

%package sysvinit
Summary: SysV init script for device-mapper-multipath
Group: System Environment/Libraries

%description sysvinit
SysV style init script for device-mapper-multipth. It needs to be
installed only if systemd is not used as the system init process.

%package -n kpartx
Summary: Partition device manager for device-mapper devices
Group: System Environment/Base

%description -n kpartx
kpartx manages partition creation and removal for device-mapper devices.

%prep
%setup -q -n multipath-tools
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch1001 -p1
%patch1002 -p1
%patch1003 -p1
%patch1004 -p1
%patch1005 -p1
%patch1006 -p1
%patch1007 -p1
%patch1008 -p1
%patch1009 -p1
%patch1010 -p1
%patch1011 -p1
%patch1012 -p1
%patch1013 -p1
%patch1014 -p1
%patch1015 -p1
%patch1016 -p1
%patch1017 -p1
%patch1018 -p1
%patch1019 -p1
%patch1020 -p1
%patch1021 -p1
%patch1022 -p1
%patch1023 -p1
%patch1024 -p1
%patch1025 -p1
%patch1026 -p1
%patch1027 -p1
%patch1028 -p1
%patch1029 -p1
%patch1030 -p1
%patch1031 -p1
%patch1032 -p1
%patch1033 -p1
%patch1034 -p1
%patch1035 -p1
%patch1036 -p1
%patch1037 -p1
%patch1038 -p1
%patch1039 -p1
%patch1040 -p1
%patch1041 -p1
%patch1042 -p1
%patch1043 -p1
%patch1044 -p1
%patch1045 -p1
%patch1046 -p1
%patch1047 -p1
%patch1048 -p1
%patch1049 -p1
%patch1050 -p1
%patch1051 -p1
%patch1052 -p1
%patch1053 -p1
%patch1054 -p1
%patch1055 -p1
%patch1056 -p1
%patch1057 -p1
%patch1058 -p1
%patch1059 -p1
%patch1060 -p1
%patch1061 -p1
%patch1062 -p1
%patch1063 -p1
%patch1064 -p1
%patch1065 -p1
%patch1066 -p1
%patch1067 -p1
%patch1068 -p1
%patch1069 -p1
%patch1070 -p1
%patch1071 -p1
%patch1072 -p1
%patch1073 -p1
%patch1074 -p1
%patch1075 -p1
%patch1076 -p1
%patch1077 -p1
%patch1078 -p1
%patch1079 -p1
%patch1080 -p1
%patch1081 -p1
%patch1083 -p1
%patch1084 -p1
%patch1085 -p1
%patch1086 -p1
%patch1087 -p1
%patch1088 -p1
%patch1089 -p1
%patch1090 -p1
%patch1091 -p1
%patch1092 -p1
%patch1093 -p1
%patch1094 -p1
%patch1095 -p1
%patch1096 -p1
%patch1097 -p1
%patch1098 -p1
%patch1099 -p1
%patch1100 -p1
%patch1101 -p1
%patch1102 -p1
cp %{SOURCE1} .

%build
%define _sbindir /sbin
%define _libdir /%{_lib}
%define _libmpathdir %{_libdir}/multipath
make %{?_smp_mflags} LIB=%{_lib}

%install
rm -rf %{buildroot}

make install \
	DESTDIR=%{buildroot} \
	bindir=%{_sbindir} \
	syslibdir=%{_libdir} \
	libdir=%{_libmpathdir} \
	rcdir=%{_initrddir} \
	unitdir=%{_unitdir}

# tree fix up
# install -m 0644 %{SOURCE1} %{buildroot}/etc/multipath.conf
install -d %{buildroot}/etc/multipath

%clean
rm -rf %{buildroot}

%post
if [ $1 -eq 1 ] ; then
	/bin/systemctl enable multipathd.service >/dev/null 2>&1 || :
fi

%preun
if [ $1 -eq 0 ] ; then
	/bin/systemctl --no-reload disable multipathd.service > /dev/null 2>&1 || :
	bin/systemctl stop multipathd.service > /dev/null 2>&1 || :
fi

%postun
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
	/bin/systemctl try-restart multipathd.service >/dev/null 2>&1 || :
fi

%triggerun --  %{name} < 0.4.9-16
%{_bindir}/systemd-sysv-convert --save multipathd >/dev/null 2>&1 ||: 
bin/systemctl --no-reload enable multipathd.service >/dev/null 2>&1 ||:
/sbin/chkconfig --del multipathd >/dev/null 2>&1 || :
/bin/systemctl try-restart multipathd.service >/dev/null 2>&1 || :

%triggerpostun -n %{name}-sysvinit -- %{name} < 0.4.9-16
/sbin/chkconfig --add mdmonitor >/dev/null 2>&1 || :

%files
%defattr(-,root,root,-)
%{_sbindir}/multipath
%{_sbindir}/multipathd
%{_sbindir}/cciss_id
%{_sbindir}/mpathconf
%{_unitdir}/multipathd.service
%{_mandir}/man5/multipath.conf.5.gz
%{_mandir}/man8/multipath.8.gz
%{_mandir}/man8/multipathd.8.gz
%{_mandir}/man8/mpathconf.8.gz
%config /lib/udev/rules.d/40-multipath.rules
%doc AUTHOR COPYING FAQ
%doc multipath.conf multipath.conf.annotated
%doc multipath.conf.defaults multipath.conf.synthetic
%dir /etc/multipath

%files libs
%defattr(-,root,root,-)
%doc AUTHOR COPYING
%{_libdir}/libmultipath.so
%dir %{_libmpathdir}
%{_libmpathdir}/*

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files sysvinit
%{_initrddir}/multipathd

%files -n kpartx
%defattr(-,root,root,-)
/sbin/kpartx
%{_mandir}/man8/kpartx.8.gz

%changelog
* Fri Jul 15 2011 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9-16
- Modify 0012-RH-udev-sync-support.patch
- Modify 0021-RHBZ-548874-add-find-multipaths.patch
- Modify 0022-RHBZ-557845-RHEL5-style-partitions.patch
- Add 0025-RHBZ-508827-update-multipathd-manpage.patch through
      0101-RHBZ-631009-disable-udev-disk-rules-on-reload.patch
  * sync with current state of RHEL6. Next release should include a updated
    source tarball with most of these fixes rolled in.
- Add 0102-RHBZ-690828-systemd-unit-file.patch
  * Add Jóhann B. Guðmundsson's unit file for systemd.
  * Add sub-package sysvinit for SysV init script.
- Resolves: bz #690828

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb 16 2010 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9-14
- Modify 0021-RHBZ-548874-add-find-multipaths.patch
  * fix bug where mpathconf wouldn't create a multpath.conf file unless one
    already existed.

* Tue Feb 16 2010 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9-13
- Replace 0012-RH-explicitly-disable-dm-udev-sync-support-in-kpartx.patch
  with 0012-RH-udev-sync-support.patch
  * Add udev sync support to kpartx and multipath. In kpartx it is disabled
    unless you use the -s option.
- Refresh 0013-RH-add-weighted_prio-prioritizer.patch
- Refresh 0021-RHBZ-548874-add-find-multipaths.patch
- Modify 0022-RHBZ-557845-RHEL5-style-partitions.patch
  * kpartx now creates a 2 sector large device for dos extended
    partitions, just like the kernel does on the regular block devices.
- Add 0023-RHBZ-557810-emc-invista-config.patch
- Add 0024-RHBZ-565933-checker-timeout.patch
  * Multipath has a new option checker_timeout. If this is not set, 
    all path checker functions with explicit timeouts use
    /sys/block/sd<x>/device/timeout. If this is set, they use it instead.

* Fri Jan 22 2010 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9-12
- Refresh 0001-RH-queue-without-daemon.patch
- Refresh 0002-RH-path-checker.patch
- Modify 0010-RH-multipath-rules-udev-changes.patch
  * Fix udev rules to use DM_SBIN_PATH when calling kpartx
  * install udev rules to /lib/udev/rules.d instead of /etc/udev/rules.d
- Modify 0014-RH-add-hp_tur-checker.patch
- Add 0003-for-upstream-default-configs.patch
- Add 0016-RHBZ-554561-fix-init-error-msg.patch
- Add 0017-RHBZ-554592-man-page-note.patch
- Add 0018-RHBZ-554596-SUN-6540-config.patch
- Add 0019-RHBZ-554598-fix-multipath-locking.patch
- Add 0020-RHBZ-554605-fix-manual-failover.patch
- Add 0021-RHBZ-548874-add-find-multipaths.patch
  * Added find_multipaths multipath.conf option
  * Added /sbin/mpathconf for simple editting of multipath.conf
- Add 0022-RHBZ-557845-RHEL5-style-partitions.patch
  * Make kpartx deal with logical partitions like it did in RHEL5.
    Don't create a dm-device for the extended partition itself.
    Create the logical partitions on top of the dm-device for the whole disk.

* Mon Nov 16 2009 Benjamin Marzinski <bmarzins@redhat.com> -0.4.9-11
- Add 0002-for-upstream-add-tmo-config-options.patch
  * Add fail_io_fail_tmo and dev_loss_tmo multipath.conf options
- Add 0013-RH-add-weighted_prio-prioritizer.patch
- Add 0014-RH-add-hp_tur-checker.patch
- Add 0015-RH-add-multipathd-count-paths-cmd.patch
- rename multipath.conf.redhat to multipath.conf, and remove the default
  blacklist.

* Tue Oct 27 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.4.9-10
- Updated to latest upstream 0.4.9 code : multipath-tools-091027.tar.gz
  (git commit id: a946bd4e2a529e5fba9c9547d03d3f91806618a3)
- Drop unrequired for-upstream patches.
- BuildRequires and Requires new device-mapper version for udev sync support.

* Tue Oct 20 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.4.9-9
- 0012-RH-explicitly-disable-dm-udev-sync-support-in-kpartx.patch

* Mon Oct 19 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.4.9-8
- Split patches in "for-upstream" and "RH" series.
- Replace 0011-RH-multipathd-blacklist-all-by-default.patch with
  version from Benjamin Marzinski.
- Update udev rules 0010-RH-multipath-rules-udev-changes.patch.
- rpmlint cleanup:
  * Drop useless-provides kpartx.
  * Cleanup tab vs spaces usage.
  * Summary not capitalized.
  * Missing docs in libs package.
  * Fix init script LSB headers.
- Drop README* files from doc sections (they are empty).

* Thu Oct 15 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.4.9-7
- Add patch 0010-RH-Set-friendly-defaults.patch:
  * set rcdir to fedora default.
  * do not install kpartx udev bits.
  * install redhat init script.
  * Cleanup spec file install target.
- Add patch 0011-RH-multipathd-blacklist-all-by-default.patch:
  * Fix BZ#528059
  * Stop installing default config in /etc and move it to the doc dir.

* Tue Oct 13 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.4.9-6
- Updated to latest upstream 0.4.9 code : multipath-tools-091013.tar.gz
  (git commit id: aa0a885e1f19359c41b63151bfcface38ccca176)
- Drop, now upstream, patches:
  * fix_missed_uevs.patch.
  * log_all_messages.patch.
  * uninstall.patch.
  * select_lib.patch.
  * directio_message_cleanup.patch.
  * stop_warnings.patch.
- Drop redhatification.patch in favour of spec file hacks.
- Drop mpath_wait.patch: no longer required.
- Merge multipath_rules.patch and udev_change.patch.
- Rename all patches based on source.
- Add patch 0009-RH-fix-hp-sw-hardware-table-entries.patch to fix
  default entry for hp_sw and match current kernel.
- Add multipath.conf.redhat as source instead of patch.
- spec file:
  * divide runtime and build/setup bits.
  * update BuildRoot.
  * update install section to apply all the little hacks here and there,
    in favour of patches against upstream.
  * move ldconfig invokation to libs package where it belong.
  * fix libs package directory ownership and files.

* Thu Aug 20 2009 Benjamin Marzinski <bmarzins@redhat.com> - 0.4.9-5
- Fixed problem where maps were being added and then removed.
- Changed the udev rules to fix some issues.

* Thu Jul 30 2009 Benjamin Marzinski <bmarzins@redhat.com> - 0.4.9-4
- Fixed build issue on i686 machines.

* Wed Jul 29 2009 Benjamin Marzinski <bmarzins@redhat.com> - 0.4.9-3
- Updated to latest upstream 0.4.9 code : multipath-tools-090729.tgz
  (git commit id: d678c139719d5631194b50e49f16ca97162ecd0f)
- moved multipath bindings file from /var/lib/multipath to /etc/multipath
- Fixed 354961, 432520

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 6 2009 Mike Snitzer <snitzer@redhat.com> - 0.4.9-1
- Updated to latest upstream 0.4.9 code: multipath-tools-090429.tgz
  (git commit id: 7395bcda3a218df2eab1617df54628af0dc3456e)
- split the multipath libs out to a device-mapper-multipath-libs package
- if appropriate, install multipath libs in /lib64 and /lib64/multipath

* Thu Apr 7 2009 Milan Broz <mbroz@redhat.com> - 0.4.8-10
- Fix insecure permissions on multipathd.sock (CVE-2009-0115)

* Fri Mar 6 2009 Milan Broz <mbroz@redhat.com> - 0.4.8-9
- Fix kpartx extended partition handling (475283)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep 26 2008 Benjamin Marzinski <bmarzins@redhat.com> 0.4.8-7
- Since libaio is now in /lib, not /usr/lib, multipath no longer needs to
  statically link against it. Fixed an error with binding file and WWIDs
  that include spaces. Cleaned up the messages from the directio checker
  function.  Fixed the udev rules. Fixed a regression in multipath.conf
  parsing
- Fixed 457530, 457589

* Wed Aug 20 2008 Benjamin Marzinski <bmarzins@redhat.com> 0.4.8-6
- Updated to latest upstream 0.4.8 code: multipath-tools-080804.tgz
  (git commit id: eb87cbd0df8adf61d1c74c025f7326d833350f78)
- fixed 451817, 456397 (scsi_id_change.patch), 457530 (config_space_fix.patch)
  457589 (static_libaio.patch)

* Fri Jun 13 2008 Alasdair Kergon <agk@redhat.com> - 0.4.8-5
- Rebuild (rogue vendor tag). (451292)

* Mon May 19 2008 Benjamin Marzinksi <bmarzins@redhat.com> 0.4.8-4
- Fixed Makefile issues.

* Mon May 19 2008 Benjamin Marzinksi <bmarzins@redhat.com> 0.4.8-3
- Fixed ownership build error.

* Mon May 19 2008 Benjamin Marzinksi <bmarzins@redhat.com> 0.4.8-2
- Forgot to commit some patches.

* Mon May 19 2008 Benjamin Marzinski <bmarzins@redhat.com> 0.4.8-1
- Updated to latest Upstream 0.4.8 code: multipath-tools-080519.tgz
  (git commit id: 42704728855376d2f7da2de1967d7bc71bc54a2f)

* Tue May 06 2008 Alasdair Kergon <agk@redhat.com> - 0.4.7-15
- Remove unnecessary multipath & kpartx static binaries. (bz 234928)

* Fri Feb 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.4.7-14
- fix sparc64
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.7-13
- Autorebuild for GCC 4.3

* Wed Nov 14 2007 Benjamin Marzinski <bmarzins@redhat.com> - 0.4.7-12
- Fixed the dist tag so building will work properly.

* Mon Feb 05 2007 Alasdair Kergon <agk@redhat.com> - 0.4.7-11.fc7
- Add build dependency on new device-mapper-devel package.
- Add dependency on device-mapper.

* Wed Jan 31 2007 Benjamin Marzinksi <bmarzins@redhat.com> - 0.4.7-10.fc7
- Update BuildRoot and PreReq lines.

* Mon Jan 15 2007 Benjamin Marzinksi <bmarzins@redhat.com> - 0.4.7-9.fc7
- Fixed spec file.

* Mon Jan 15 2007 Benjamin Marzinski <bmarzins@redhat.com> - 0.4.7-8.fc7
- Update to latest code (t0_4_7_head2)

* Wed Dec 13 2006 Benjamin Marzinski <bmarzins@redhat.com> - 0.4.7-7.fc7
- Update to latest code (t0_4_7_head1)

* Thu Sep  7 2006 Peter Jones <pjones@redhat.com> - 0.4.7-5
- Fix kpartx to handle with drives >2TB correctly.

* Thu Aug 31 2006 Peter Jones <pjones@redhat.com> - 0.4.7-4.1
- Split kpartx out into its own package so dmraid can use it without
  installing multipathd
- Fix a segfault in kpartx

* Mon Jul 17 2006 Benjamin Marzinski <bmarzins@redhat.com> 0.4.7-4.0
- Updated to latest source. Fixes bug in default multipath.conf

* Wed Jul 12 2006 Benjamin Marzinski <bmarzins@redhat.com> 0.4.7-3.1
- Added ncurses-devel to BuildRequires

* Wed Jul 12 2006 Benjamin Marzinski <bmarzins@redhat.com> 0.4.7-3.0
- Updated to latest source. deals with change in libsysfs API

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.4.7-2.2.1
- rebuild

* Mon Jul 10 2006 Benjamin Marzinski <bmarzins@redhat.com> 0.4.7-2.2
- fix tagging issue.

* Mon Jul 10 2006 Benjamin Marzinski <bmarzins@redhat.com> 0.4.7-2.1
- changed BuildRequires from sysfsutils-devel to libsysfs-devel

* Wed Jun 28 2006 Benjamin Marzinski <bmarzins@redhat.com> 0.4.7-2.0
- Updated to latest upstream source, fixes kpartx udev rule issue

* Mon Jun 06 2006 Benjamin Marzinski <bmarzins@redhat.com> 0.4.7-1.0
- Updated to Christophe's latest source

* Mon May 22 2006 Alasdair Kergon <agk@redhat.com> - 0.4.5-16.0
- Newer upstream source (t0_4_5_post59).

* Mon May 22 2006 Alasdair Kergon <agk@redhat.com> - 0.4.5-12.3
- BuildRequires: libsepol-devel, readline-devel

* Mon Feb 27 2006 Benjamin Marzinski <bmarzins@redhat.com> 0.4.5-12.2
- Prereq: chkconfig

* Mon Feb 20 2006 Karsten Hopp <karsten@redhat.de> 0.4.5-12.1
- BuildRequires: libselinux-devel

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.4.5-12.0.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Benjamin Marzinski <bmarzins@redhat.com> -0.4.5-12.0
- Updated to latest upstream source (t0_4_5_post56)

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
