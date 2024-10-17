%define prerel beta4

Name:		kshutdown
Version:	3.0
Release:	0.%{prerel}.1
Summary:	Advanced shut down utility for KDE
License:	GPLv2+
Group:		Graphical desktop/KDE
URL:		https://kshutdown.sourceforge.net/
Source0:	http://ovh.dl.sourceforge.net/sourceforge/%{name}/%{name}-source-%{version}%{prerel}.zip
Requires:	kdebase4-workspace
BuildRequires:	kdebase4-workspace-devel
BuildRequires:	desktop-file-utils

%description
KShutDown is an advanced shut down utility for KDE.
Features:
- Shut Down (logout and halt the system)
- Reboot (logout and reboot the system)
- Lock Screen (lock the screen using a screen saver)
- Logout (end the session and logout the user)
- Extras (user commands)
- Wizard
- Time and delay options
- Command line support
- System tray
- Sounds
- Kiosk support
- And more...

%files -f %{name}.lang
%doc TODO ChangeLog README.html
%attr(0755,root,root) %{_kde_bindir}/%{name}
%{_kde_iconsdir}/hicolor/*/apps/kshutdown.png
%{_kde_iconsdir}/hicolor/*/apps/kshutdown.svgz
%{_kde_applicationsdir}/%{name}.desktop
%{_kde_appsdir}/%{name}

#------------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}%{prerel}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

desktop-file-install --vendor="" \
--remove-category="Application" \
--add-category="KDE" \
--add-category="System" \
--add-category="Monitor" \
--dir %{buildroot}/%{_datadir}/applications/kde4 %{buildroot}/%{_datadir}/applications/kde4/*

%find_lang %{name} --with-html

