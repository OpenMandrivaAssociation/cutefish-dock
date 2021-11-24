%define oname dock

Name:           cutefish-dock
Version:        0.5
Release:        1
Summary:        Application Dock for Cutefish
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/cutefishos/dock
Source:         https://github.com/cutefishos/dock/archive/refs/tags/%{version}/%{oname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(FishUI)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(dbusmenu-qt5)

Requires:       cutefish
Requires:       fishui

%description
CutefishOS application dock.

%lang_package

%prep
%autosetup -n %{oname}-%{version} -p1

%build
%cmake
%make_build

%install
%make_install -C build

%find_lang %{name} --all-name --with-qt

%files -f %{name}.lang
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/%{name}-list.conf
%{_bindir}/%{name}
