%define name	kshutdown
%define version	2.0
%define betaver beta8
%define release	%mkrel -c %betaver 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:        Advanced shut down utility for KDE
Summary(fr):    KShutDown est un outils avancé de gestion de l'extinction  
License:        GPLv2+
Group:		Graphical desktop/KDE
Source:	        http://ovh.dl.sourceforge.net/sourceforge/%{name}/%{name}-source-%{version}%{betaver}.zip
Patch0:		kshutdown-2.0-drop-actions.patch
Requires:	kdebase4-workspace
BuildRequires:  kdebase4-workspace-devel
BuildRequires:  desktop-file-utils
BuildRoot:	%{_tmppath}/%{name}-buildroot

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

%prep
%setup -q -n %name-%version%betaver

%build
%cmake_kde4
%make

%install
rm -rf $RPM_BUILD_ROOT
cd build
%makeinstall_std
cd -

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="System" \
  --add-category="Monitor" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications/kde4 $RPM_BUILD_ROOT%{_datadir}/applications/kde4/*

%find_lang %name --with-html

%clean
rm -rf %{buildroot}

%post
%update_icon_cache hicolor

%postun
%clean_icon_cache hicolor

%files -f %name.lang
%defattr(-,root,root)
%doc TODO ChangeLog README.html
%attr(0755,root,root) %{_kde_bindir}/%{name}
%_kde_iconsdir/*/*/*/*
%_kde_datadir/applications/kde4/kshutdown.desktop
%_kde_datadir/apps/%{name}
