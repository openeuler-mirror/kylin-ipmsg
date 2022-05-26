%define debug_package %{nil}
Name:          kylin-ipmsg
Version:       1.1.25
Release:       2
Summary:       kylin-ipmsg
License:       GPL-3
URL:           https://github.com/UbuntuKylin/kylin-ipmsg
Source0:       %{name}-%{version}.tar.gz

BuildRequires: qt5-qtbase-devel
BuildRequires: qtchooser
BuildRequires: qt5-qtscript-devel
BuildRequires: qt5-qttools-devel
BuildRequires: qt5-linguist
BuildRequires: qt5-qtx11extras-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: gsettings-qt-devel
BuildRequires: glib2-devel
BuildRequires: peony libpeony-dev
BuildRequires: ukui-interface


%description
Messages is a LAN chat tool with beautiful Gui.

%prep
%setup -q

%build
export PATH=%{_qt5_bindir}:$PATH
mkdir qmake-build
pushd qmake-build
%{qmake_qt5} ..
%{make_build}
popd 

%install
pushd qmake-build
%{make_install} INSTALL_ROOT=%{buildroot}
popd 

%files
%{_bindir}/kylin-ipmsg
%{_datadir}/applications/kylin-ipmsg.desktop
%{_datadir}/glib-2.0/schemas/org.ukui.log4qt.kylin-ipmsg.gschema.xml
%{_datadir}/kylin-ipmsg/data/database/kylin-ipmsg.db
%{_datadir}/kylin-ipmsg/data/translations/kylin-ipmsg_zh_CN.qm
%{_datadir}/kylin-user-guide/*


%changelog
* Thu May 26 2022 peijiankang <peijiankang@kylinos.cn> - 1.1.25-2
- remove {%if 0 and %endif}

* Fri May 20 2022 peijiankang <peijiankang@kylinos.cn> - 1.1.25-1
- Init kylin-ipmsg package for openEuler
