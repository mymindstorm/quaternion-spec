Name:       quaternion
Version:    0.0.9.4c
Release:    1%{?dist}

Summary:    A Qt5-based IM client for Matrix
License:    GPLv3
URL:        https://github.com/quotient-im/Quaternion
Source0:    https://github.com/quotient-im/Quaternion/archive/%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: desktop-file-utils

BuildRequires: cmake(Olm)
BuildRequires: cmake(QtOlm)
BuildRequires: cmake(QMatrixClient)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5Multimedia)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5QuickWidgets)
BuildRequires: cmake(Qt5Keychain)

%description
Quaternion is a cross-platform desktop IM client for the Matrix protocol.

%prep
%autosetup -n Quaternion-%{version}
mkdir -p %{_target_platform}

%build
%cmake \
    -DUSE_INTREE_LIBQMC=NO
%make_build

%install
%make_install
%find_lang %{name} --with-qt

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/com.github.quaternion.desktop

%files -f %{name}.lang
%license COPYING
%doc README.md BUILDING.md
%{_bindir}/%{name}
%{_datadir}/applications/com.github.quaternion.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svgz
%{_datadir}/metainfo/com.github.quaternion.appdata.xml

%changelog
* Thu Mar 05 2020 Brendan Early <mymindstorm@evermiss.net> - 0.0.9.4c-1.fc31
- Version 0.9.4c

