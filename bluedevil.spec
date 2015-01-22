%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	The bluetooth stack for KDE 5
Name:		bluedevil5
Version:	5.1.95
Release:	1
Group:		Graphical desktop/KDE
License:	GPL
Url:		https://projects.kde.org/projects/extragear/base/bluedevil
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/plasma/%{version}/bluedevil-%{version}.tar.xz
Source100:	%{name}.rpmlintrc

BuildRequires:	extra-cmake-modules5
BuildRequires:	pkgconfig(bluedevil) >= 5.0
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	pkgconfig(shared-mime-info)
BuildRequires:	ninja
Provides:	bluez-pin
Requires:	bluez >= 4.28
Requires:	obexd

# Can't coexist with the KDE4 version because of hardcoded filenames
Conflicts:	bluedevil < 5.0

%description
BlueDevil is the new bluetooth stack for KDE, it's composed of:
KCM, KDED, KIO, Library and some other small applications.

%files
%{_bindir}/*
%{_libdir}/libexec/bluedevil-*
%{_libdir}/qt5/plugins/*.so
%{_datadir}/applications/*
%{_datadir}/bluedevilwizard
%{_datadir}/knotifications5/*
%{_datadir}/kservices5/*
%{_datadir}/mime/packages/bluedevil-mime.xml

#-----------------------------------------------------------------------------

%prep
%setup -qn bluedevil-%{version}

%build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
ninja

%install
DESTDIR="%{buildroot}" ninja install -C build

