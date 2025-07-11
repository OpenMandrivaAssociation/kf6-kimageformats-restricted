%define major %(echo %{version} |cut -d. -f1-2)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240217

Name: kf6-kimageformats
Version: 6.16.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/kimageformats/-/archive/master/kimageformats-master.tar.bz2#/kimageformats-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/frameworks/%{major}/kimageformats-%{version}.tar.xz
%endif
Summary: Plugins to allow QImage to support extra file formats.
URL: https://invent.kde.org/frameworks/kimageformats
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: pkgconfig(zlib)
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(libheif)
BuildSystem: cmake
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildOption: -DKIMAGEFORMATS_HEIF:BOOL=ON
BuildOption: -DKIMAGEFORMATS_JXL:BOOL=OFF
BuildOption: -DKIMAGEFORMATS_JXR:BOOL=OFF

%description
Plugins to allow QImage to support extra file formats.

%package heif
Summary: Qt 6.x support for images in the HEIF format
Group: System/Libraries
Supplements: %{name} = %{version}

%description heif
Qt 6.x support for images in the HEIF format

%files heif
%{_libdir}/qt6/plugins/imageformats/kimg_heif.so

%install -a
# We get the other imageformats from the kf6-kimageformats package in main,
# just package any restricted formats
cd %{buildroot}%{_qtdir}/plugins/imageformats
rm -f $(ls |grep -v heif)
rm -rf %{buildroot}%{_libdir}/cmake
