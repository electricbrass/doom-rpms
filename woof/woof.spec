name:    woof
Version: 16.0.0
Release: 1%{?dist}
Summary: Modern continuation of the MBF Doom engine
License: GPL-2.0-or-later
URL:     https://fabiangreffrath.github.io/woof/

Source0: https://github.com/fabiangreffrath/woof/archive/refs/tags/woof_%{version}.tar.gz

BuildRequires: cmake >= 3.15
BuildRequires: gcc
BuildRequires: make

BuildRequires: SDL3-devel >= 3.4.0
BuildRequires: openal-soft-devel >= 1.22.0
BuildRequires: libsndfile-devel >= 1.1.0
BuildRequires: libebur128-devel >= 1.2.0
BuildRequires: yyjson-devel >= 0.10.0
BuildRequires: fluidsynth-devel >= 2.2.0
BuildRequires: libxmp-devel
BuildRequires: libspng-devel

Requires: SDL3 >= 3.4.0
Requires: openal-soft >= 1.22.0
Requires: libsndfile >= 1.1.0
Requires: libebur128 >= 1.2.0
Requires: yyjson >= 0.10.0
Requires: fluidsynth >= 2.2.0
Requires: libxmp
Requires: libspng

%description
Modern continuation of the MBF Doom engine.
Woof remains faithful to class gameplay while
providing support for modding features such as
DEHEXTRA, DSDHacked, UMAPINFO, and MBF21.

%prep
%autosetup -n woof-woof_%{version}

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmake_install

rm %{buildroot}%{_datadir}/doc/woof/COPYING

%files
%{_bindir}/*
%{_datadir}/*
%license COPYING

%changelog
* Wed Jul 01 2026 Mia McMahill <electricbrass@proton.me> - 16.0.0-1
- Update to Woof 16.0.0

%changelog
* Wed Jul 01 2026 Mia McMahill <electricbrass@proton.me> - 15.3.0-1
- Initial COPR package
