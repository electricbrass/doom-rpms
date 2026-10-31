%global forgeurl https://github.com/elf-alchemist/elfbsp/

Version: 1.3.0

%global tag elfbsp_v%{version}

%forgemeta -i -v

name:    elfbsp
Release: 1%{?dist}
Summary: Modern BSP tree builder for idTech1 games and source ports
License: GPL-2.0-or-later
URL:     https://elf-alchemist.github.io/elfbsp/

Source: %{forgesource}
Patch0: patches/use-system-zlib.patch

BuildRequires: cmake >= 3.15
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: zlib-ng

Requires: zlib-ng

%description
ELFBSP is a general purpose nodes builder for modern DOOM source ports.
It supports a wide variety of map formats, and compiled data formats.
The code is based on Andrew Apted’s AJBSP, itself based on
the Eureka level editor’s internal BSP code.

%prep
%forgeautosetup -p1

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DENABLE_LTO=ON -DENABLE_HARDENING=ON
%cmake_build

%install
%cmake_install

rm %{buildroot}%{_datadir}/doc/elfbsp/LICENSE.txt

%files
%{_bindir}/*
%{_datadir}/*
%license LICENSE.txt

%changelog
* Sat Oct 31 2026 Mia McMahill <electricbrass@proton.me> - 1.3.0-1
- Initial COPR package
