%define	gitdate	20121019

Summary:	GUI login manager for LXDE
Name:		lxdm
Version:	0.5.3
Release:	0.%{gitdate}.1
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://www.lxde.org
Source0:	http://dfn.dl.sourceforge.net/sourceforge/lxde/%{name}-%{version}.tar.xz
Source1:	27%{name}.conf
Patch0:		lxdm-0.2.0-mdv-customization.patch
BuildRequires:	intltool
BuildRequires:	iso-codes
BuildRequires:	pam-devel
BuildRequires:	pkgconfig(gtk+-x11-2.0)
BuildRequires:	pkgconfig(systemd)
BuildRequires:	pkgconfig(xmu)
Requires:	iso-codes

%description
A lightweight dropped-in replacement for GDM or KDM.

%prep
%setup -q
%patch0 -p0 -b .mdv~
#rm data/lxdm.conf

%build
%configure	--disable-consolekit
%make_build

%install
%make_install

# dm conf file
install -m644 %{SOURCE1} -D %{buildroot}%{_datadir}/X11/dm.d/27%{name}.conf

%find_lang %{name}

%files -f %{name}.lang
%dir %{_sysconfdir}/lxdm
%{_sysconfdir}/lxdm/Xsession
%config(noreplace) %{_sysconfdir}/lxdm/lxdm.conf
%config(noreplace) %{_sysconfdir}/lxdm/LoginReady
%config(noreplace) %{_sysconfdir}/lxdm/PostLogin
%config(noreplace) %{_sysconfdir}/lxdm/PostLogout
%config(noreplace) %{_sysconfdir}/lxdm/PreLogin
%config(noreplace) %{_sysconfdir}/lxdm/PreReboot
%config(noreplace) %{_sysconfdir}/lxdm/PreShutdown
%config(noreplace) %{_datadir}/X11/dm.d/27%{name}.conf
%{_sysconfdir}/pam.d/*
%{_libexecdir}/lxdm-greeter-gtk
%{_sbindir}/lxdm*
%{_datadir}/%{name}
%{_bindir}/lxdm-config
%{_libdir}/lxdm-greeter-gdk
%{_libdir}/lxdm-numlock
%{_unitdir}/lxdm.service

