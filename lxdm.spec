Summary: GUI login manager for LXDE
Name: lxdm
Version: 0.1.0
Release: %mkrel 3
License: GPLv2+
Group: Graphical desktop/Other
Source0: http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.gz
Patch0: lxdm-0.1.0-mdv-customize.patch
URL: http://www.lxde.org
BuildRequires: intltool
BuildRequires: consolekit-devel
BuildRequires: libxmu-devel
BuildRequires: pam-devel
BuildRequires: iso-codes
BuildRequires: gtk+2-devel
Requires: iso-codes
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A lightweight dropped-in replacement for GDM or KDM.

%prep
%setup -q
%patch0 -p0 -b .mdv

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%{find_lang} %{name}

%files -f %{name}.lang
%defattr(-, root, root)
%dir %{_sysconfdir}/lxdm
%{_sysconfdir}/lxdm/Xsession
%config(noreplace) %{_sysconfdir}/lxdm/lxdm.conf
%{_sysconfdir}/pam.d/*
%{_bindir}/*
%{_datadir}/%{name}
