%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	The bluetooth stack for KDE 5
Name:		bluedevil5
Version:	5.5.5
Release:	1
Group:		Graphical desktop/KDE
License:	GPL
Url:		https://projects.kde.org/projects/extragear/base/bluedevil
Source0:	http://download.kde.org/%{stable}/plasma/%{version}/bluedevil-%{version}.tar.xz
Source100:	%{name}.rpmlintrc
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5BluezQt)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KDED)
BuildRequires:	pkgconfig(shared-mime-info)
Provides:	bluez-pin
Requires:	bluez >= 4.28
Requires:	obexd

# Can't coexist with the KDE4 version because of hardcoded filenames
Conflicts:	bluedevil < 5.0

%description
BlueDevil is the new bluetooth stack for KDE, it's composed of:
KCM, KDED, KIO, Library and some other small applications.

%files -f %{name}-all.lang
%{_bindir}/*
%{_libdir}/qt5/plugins/*.so
%{_datadir}/applications/*
%{_datadir}/bluedevilwizard
%{_datadir}/knotifications5/*
%{_datadir}/kservices5/*
%{_datadir}/mime/packages/bluedevil-mime.xml

%dir %{_libdir}/qt5/qml/org/kde/plasma/private/bluetooth
%{_libdir}/qt5/plugins/kf5/kded/*.so
%{_libdir}/qt5/qml/org/kde/plasma/private/bluetooth/libbluetoothplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/private/bluetooth/qmldir

%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.bluetooth
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.bluetooth/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.bluetooth/contents/code
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.bluetooth/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.bluetooth/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.bluetooth/contents/code/logic.js
%{_datadir}/plasma/plasmoids/org.kde.plasma.bluetooth/contents/ui/*.qml
%{_datadir}/remoteview/bluetooth-network.desktop

#-----------------------------------------------------------------------------

%prep
%setup -qn bluedevil-%{version}
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang bluedevil
%find_lang plasma_applet_org.kde.plasma.bluetooth
cat *.lang >%{name}-all.lang
