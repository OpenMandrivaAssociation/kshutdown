%define name	kshutdown
%define version	1.0
%define release	%mkrel 1
%define __libtoolize /bin/true
%define __cputoolize /bin/true

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:        KShutDown is an advanced shut down utility for KDE
Summary(fr):    KShutDown est un outils avancé de gestion de l'extinction  
License:        GPL
Group:		Graphical desktop/KDE
Source:	        http://ovh.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2	
Source10: 	%name-16.png
Source11: 	%name-32.png
Source12: 	%name-48.png



URL:		http://kshutdown.sourceforge.net/
Requires:	kdebase >= 3.3
BuildRequires:  kdelibs-devel >= 3.3
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
rm -rf %{buildroot}

%setup -q -n %{name}-%{version}


%build

export QTDIR=%_prefix/lib/qt3
export KDEDIR=%_prefix

export LD_LIBRARY_PATH=$QTDIR/%_lib:$KDEDIR/%_lib:$LD_LIBRARY_PATH
export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH

# Search for qt/kde libraries in the right directories (avoid patch)
# NOTE: please don't regenerate configure scripts below
perl -pi -e "s@/lib(\"|\b[^/])@/%_lib\1@g if /(kde|qt)_(libdirs|libraries)=/" configure

%configure --disable-rpath

%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot{%_menudir,%_miconsdir,%_iconsdir,%_liconsdir}
mkdir -p %buildroot%_datadir
mkdir -p %buildroot%_datadir/apps
mkdir -p %buildroot%_datadir/apps/kconf_update/


%makeinstall_std
cp %SOURCE10 %buildroot%_miconsdir/%name.png
cp %SOURCE11 %buildroot%_iconsdir/%name.png
cp %SOURCE12 %buildroot%_liconsdir/%name.png


desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="MandrivaLinux-System-Monitoring;System;Monitor;" \
  --add-category="System" \
  --add-category="Monitor" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications/kde $RPM_BUILD_ROOT%{_datadir}/applications/kde/*

%find_lang %name

%clean
rm -rf %{buildroot}

%post
%update_icon_cache hicolor

%postun
%clean_icon_cache hicolor

%files -f %name.lang
%defattr(-,root,root)
%doc COPYING TODO VERSION AUTHORS README
%attr(0755,root,root) %{_bindir}/%{name}
%_iconsdir/%{name}.png
%_iconsdir/*/%{name}.png
%_iconsdir/hicolor/*/apps/%{name}.png
%_datadir/applications/kshutdown.desktop
%_datadir/apps/kconf_update/%{name}.upd
%_datadir/apps/kicker/applets/kshutdownlockout.desktop
%_datadir/apps/%{name}/*

%dir %_docdir/HTML/en/kshutdown
%doc %_docdir/HTML/en/kshutdown/common
%doc %_docdir/HTML/en/kshutdown/index.cache.bz2
%doc %_docdir/HTML/en/kshutdown/index.docbook
%doc %_docdir/HTML/en/kshutdown/mainwindow.png

%dir %_docdir/HTML/de/kshutdown
%doc %_docdir/HTML/de/kshutdown/common
%doc %_docdir/HTML/de/kshutdown/index.cache.bz2
%doc %_docdir/HTML/de/kshutdown/index.docbook
%doc %_docdir/HTML/de/kshutdown/mainwindow.png


%_libdir/kde3/kshutdownlockout_panelapplet.la
%_libdir/kde3/kshutdownlockout_panelapplet.so



