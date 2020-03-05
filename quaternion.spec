Name:       quaternion
Version:    0.0.9.4c
Release:    1%{?dist}

Summary:    A Qt5-based IM client for Matrix
License:    GPLv3
URL:        https://github.com/quotient-im/Quaternion
Source0:     https://github.com/quotient-im/Quaternion/archive/%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: cmake

BuildRequires: cmake(Quotient)
BuildRequires: cmake(Qt5Widgets Qt5Network Qt5Quick Qt5Qml Qt5Gui Qt5LinguistTools Qt5Multimedia Qt5DBus)
BuildRequires: cmake(Qt5QuickWidgets)
BuildRequires: cmake(Qt5Keychain)

%description
Quaternion is a cross-platform desktop IM client for the Matrix protocol.

%prep
%autosetup
mkdir -p %{_target_platform}

%build
%cmake .. \
    -DUSE_INTREE_LIBQMC=0 \
    # -DCMAKE_INSTALL_PREFIX=%{buildroot}
%make_build

%install
%make_install

%files
%license
%doc 

%changelog
# let's skip this for now
