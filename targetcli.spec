%global oname targetcli-fb

Name:           targetcli
License:        ASL 2.0
Group:          System Environment/Libraries
Summary:        An administration shell for storage targets
Version:        2.1.fb46
Release:        7%{?dist}
URL:            https://fedorahosted.org/targetcli-fb/
Source:         https://fedorahosted.org/released/targetcli-fb/%{oname}-%{version}.tar.gz
Patch0:         0001-Properly-detect-errors-when-writing-backup-files.-Cl.patch
Patch1:         0002-Read-number-of-backup-files-to-keep-from-file.patch
Patch2:         0003-config-defend-on-etc-target-backup-directory.patch
Patch3:         0004-config-backup-when-current-config-is-different-from-.patch
Patch4:         0005-config-rename-key-kept_backups-as-max_backup_files.patch
Patch5:         0006-backup-global-option-to-tune-max-no.-of-backup-conf-.patch
Patch6:         0007-Fix-default-max_backup_files-in-ui_command_saveconfi.patch
Patch7:         0008-config-add-saveconfig-command-to-StorageObject-level.patch
Patch8:         0009-Support-tcmu-hw-max-sectors.patch
Patch9:         0010-create-add-a-way-to-set-control-string.patch
Patch10:        0011-saveconfig-way-for-block-level-save-with-delete-comm.patch
Patch11:        0012-saveconfig-handle-backups-with-block-level-delete.patch
BuildArch:      noarch
BuildRequires:  python-devel python-setuptools
Requires:       python-rtslib >= 2.1.fb41, python-configshell, python-ethtool


%description
An administration shell for configuring iSCSI, FCoE, and other
SCSI targets, using the TCM/LIO kernel target subsystem. FCoE
users will also need to install and use fcoe-utils.


%prep
%setup -q -n %{oname}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1

%build
%{__python} setup.py build
gzip --stdout targetcli.8 > targetcli.8.gz

%install
%{__python} setup.py install --skip-build --root %{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/target/backup
mkdir -p %{buildroot}%{_mandir}/man8/
install -m 644 targetcli.8.gz %{buildroot}%{_mandir}/man8/

%files
%{python_sitelib}/*
%{_bindir}/targetcli
%dir %{_sysconfdir}/target
%dir %{_sysconfdir}/target/backup
%doc COPYING README.md
%{_mandir}/man8/targetcli.8.gz

%changelog
* Wed Aug 08 2018 Maurizio Lombardi <mlombard@redhat.com> - 2.1.fb46-7
- Respin a new release of targetcli to avoid problems with TPS tests.

* Wed Jun 13 2018 Maurizio Lombardi <mlombard@redhat.com> - 2.1.fb46-6
- handle backups with block-level delete

* Mon Jun 04 2018 Maurizio Lombardi <mlombard@redhat.com> - 2.1.fb46-5
- saveconfig: way for block-level save with delete command

* Mon Apr 23 2018 Maurizio Lombardi <mlombard@redhat.com> - 2.1.fb46-4
- Properly detect errors when writing backup files. (Closes: #80) (#81)
- Read number of backup files to keep from file
- config: defend on '/etc/target/backup' directory
- config: backup when current config is different from recent backup copy
- config: rename key 'kept_backups' as 'max_backup_files'
- backup: global option to tune max no. of backup conf files

* Fri Apr 13 2018 Maurizio Lombardi <mlombard@redhat.com> - 2.1.fb46-3
- Support tcmu hw max sectors
- create: add a way to set control string

* Wed Apr 11 2018 Maurizio Lombardi <mlombard@redhat.com> - 2.1.fb46-2
- Add saveconfig command to StorageObject level

* Thu Mar 2 2017 Andy Grover <agrover@redhat.com> - 2.1.fb46-1
- New upstream version
- Drop no-model-alias.patch
- Drop no-userbackstores.patch

* Tue Aug 18 2015 Andy Grover <agrover@redhat.com> - 2.1.fb41-3
- add no-model-alias.patch, LIO no longer supports for pscsi

* Wed Jul 15 2015 Andy Grover <agrover@redhat.com> - 2.1.fb41-2
- add no-userbackstores.patch to not show, since not supported on RHEL

* Wed Jul 15 2015 Andy Grover <agrover@redhat.com> - 2.1.fb41-1
- Update to latest in Fedora
- Remove patches as fixes are in upstream version

* Tue Nov 4 2014 Andy Grover <agrover@redhat.com> - 2.1.fb37-3
- add tpg-invalid-tag.patch
- add default-portal-pref.patch

* Tue Nov 4 2014 Andy Grover <agrover@redhat.com> - 2.1.fb37-2
- add fix-session-detail.patch

* Thu Oct 9 2014 Andy Grover <agrover@redhat.com> - 2.1.fb37-1
- New upstream version

* Mon Feb 24 2014 Andy Grover <agrover@redhat.com> - 2.1.fb34-1
- New upstream version. Fixes rhbz #1066695

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.1.fb31-2
- Mass rebuild 2013-12-27

* Fri Nov 1 2013 Andy Grover <agrover@redhat.com> - 2.1.fb31-1
- New upstream version
- Move service handling to python-rtslib
- Remove old packaging bits: clean, buildroot, defattr

* Wed Sep 11 2013 Andy Grover <agrover@redhat.com> - 2.1.fb30-1
- New upstream version

* Tue Sep 10 2013 Andy Grover <agrover@redhat.com> - 2.1.fb29-1
- New upstream release
- Remove no-longer-needed BuildRequires

* Mon Aug 5 2013 Andy Grover <agrover@redhat.com> - 2.1.fb28-1
- New upstream release

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.fb27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Andy Grover <agrover@redhat.com> - 2.1.fb27-1
- New upstream release
- License now Apache 2.0
- Remove patch modules-not-loaded.patch

* Tue Jun 18 2013 Andy Grover <agrover@redhat.com> - 2.1.fb26-2
- Add patch
  * modules-not-loaded.patch

* Fri Jun 7 2013 Andy Grover <agrover@redhat.com> - 2.1.fb26-1
- New upstream release

* Thu May 9 2013 Andy Grover <agrover@redhat.com> - 2.1.fb25-1
- New upstream release

* Thu May 2 2013 Andy Grover <agrover@redhat.com> - 2.1.fb24-1
- New upstream release
- Update source URL

* Fri Apr 12 2013 Andy Grover <agrover@redhat.com> - 2.1.fb23-1
- New upstream release

* Wed Apr 10 2013 Andy Grover <agrover@redhat.com> - 2.1.fb22-1
- New upstream release

* Mon Mar 4 2013 Andy Grover <agrover@redhat.com> - 2.0.fb21-1
- New upstream release

* Tue Feb 26 2013 Andy Grover <agrover@redhat.com> - 2.0.fb20-1
- New upstream release

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0rc1.fb19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 7 2013 Andy Grover <agrover@redhat.com> - 2.0rc1.fb19-1
- New upstream release

* Thu Jan 3 2013 Andy Grover <agrover@redhat.com> - 2.0rc1.fb18-2
- Add python-ethtool BuildRequires

* Thu Dec 20 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb18-1
- New upstream release
- Add python-ethtool requires
- Update Source0 to use Github tar-from-tag instead of Downloads

* Thu Dec 13 2012 Lukáš Nykrýn <lnykryn@redhat.com> - 2.0rc1.fb17-2
- Scriptlets replaced with new systemd macros (#850335)

* Mon Nov 12 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb17-1
- New upstream release

* Tue Aug 7 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb16-1
- New upstream release
- Update rtslib version dependency

* Tue Jul 31 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb15-1
- New upstream release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0rc1.fb14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb14-2
- Fix %files to claim /etc/target, not claim sitelib

* Thu Jun 28 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb14-1
- New upstream release

* Tue Jun 12 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb13-1
- New upstream release

* Wed May 30 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb12-1
- Update Source URL to proper tarball
- New upstream release

* Mon Apr 9 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb11-1
- New upstream release

* Wed Feb 29 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb10-1
- New upstream release

* Tue Feb 21 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb9-1
- New upstream release

* Thu Feb 16 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb8-1
- New upstream release

* Wed Feb 8 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb7-1
- New upstream release

* Fri Feb 3 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb6-1
- New upstream release

* Tue Jan 24 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb5-2
- Update After= in service file to wait for localfs and network
- Improve description in service file

* Tue Jan 24 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb5-1
- New upstream release

* Fri Jan 13 2012 Andy Grover <agrover@redhat.com> - 2.0rc1.fb4-1
- New upstream release

* Tue Dec 13 2011 Andy Grover <agrover@redhat.com> - 2.0rc1.fb3-2
- Fix service file to mount configfs before starting targetcli

* Tue Dec 13 2011 Andy Grover <agrover@redhat.com> - 2.0rc1.fb3-1
- New upstream release
- Fixup service file for new start/stop targetcli commands

* Tue Dec 6 2011 Andy Grover <agrover@redhat.com> - 2.0rc1.fb2-1
- New upstream source and release
- Remove patches:
  * targetcli-git-version.patch
  * 0001-Remove-ads-from-cli-welcome-msg.-Mention-help-is-ava.patch
  * 0002-bundle-lio-utils.patch
  * 0003-Hack.-dump-scripts-aren-t-in-PATH-anymore-so-call-th.patch
  * 0004-ignore-errors-from-failure-to-set-device-attributes.patch
  * 0005-fix-spec_root-path.patch
  * 0006-add-docs.patch
  * 0007-all-start.patch

* Mon Nov 21 2011 Andy Grover <agrover@redhat.com> - 1.99.2.gitb03ec79-4
- Update doc patch to include iscsi tutorial

* Wed Nov 2 2011 Andy Grover <agrover@redhat.com> - 1.99.2.gitb03ec79-3
- Add buildrequires for systemd-units
- use _unitdir
- remove preun, modify post

* Wed Nov 2 2011 Andy Grover <agrover@redhat.com> - 1.99.2.gitb03ec79-2
- Add patch
  * 0007-all-start.patch
- Replace sysv init with systemd init

* Fri Oct 7 2011 Andy Grover <agrover@redhat.com> - 1.99.2.gitb03ec79-1
- Initial Fedora packaging
