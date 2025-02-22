#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeframever	6.11
%define		qtver		5.15.2
%define		kfname		kquickcharts

Summary:	Plugin for beautiful and interactive charts
Name:		kf6-%{kfname}
Version:	6.11.0
Release:	2
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	3b5c13512812315c913e936d8c14298d
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel
BuildRequires:	Qt6Network-devel >= 5.11.1
BuildRequires:	Qt6Qml-devel
BuildRequires:	Qt6Quick-devel
BuildRequires:	cmake >= 3.16
BuildRequires:	kf6-extra-cmake-modules >= %{kdeframever}
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
#Obsoletes:	kf5-%{kfname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt Quick plugin for beautiful and interactive charts.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
#Obsoletes:	kf5-%{kfname}-devel < %{version}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
%ninja_build -C build test
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/qt6/qml/org/kde/quickcharts
%dir %{_libdir}/qt6/qml/org/kde/quickcharts/controls
%{_datadir}/qlogging-categories6/kquickcharts.categories
%ghost %{_libdir}/libQuickCharts.so.1
%attr(755,root,root) %{_libdir}/libQuickCharts.so.*.*
%ghost %{_libdir}/libQuickChartsControls.so.1
%attr(755,root,root) %{_libdir}/libQuickChartsControls.so.*.*
%{_libdir}/qt6/qml/org/kde/quickcharts/QuickCharts.qmltypes
%{_libdir}/qt6/qml/org/kde/quickcharts/controls/KirigamiTheme.qml
%{_libdir}/qt6/qml/org/kde/quickcharts/controls/Legend.qml
%{_libdir}/qt6/qml/org/kde/quickcharts/controls/LegendDelegate.qml
%{_libdir}/qt6/qml/org/kde/quickcharts/controls/LineChartControl.qml
%{_libdir}/qt6/qml/org/kde/quickcharts/controls/PieChartControl.qml
%{_libdir}/qt6/qml/org/kde/quickcharts/controls/QuickChartsControls.qmltypes
%{_libdir}/qt6/qml/org/kde/quickcharts/controls/Theme.qml
%{_libdir}/qt6/qml/org/kde/quickcharts/controls/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/quickcharts/controls/libQuickChartsControlsplugin.so
%{_libdir}/qt6/qml/org/kde/quickcharts/controls/qmldir
%{_libdir}/qt6/qml/org/kde/quickcharts/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/quickcharts/libQuickChartsplugin.so
%{_libdir}/qt6/qml/org/kde/quickcharts/qmldir


%files devel
%defattr(644,root,root,755)
%{_libdir}/cmake/KF6QuickCharts
%{_libdir}/libQuickCharts.so
%{_libdir}/libQuickChartsControls.so
