# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name png
%global full_version 0.18.1
%global pkgname png-0.18

Name:           rust-png-0.18
Version:        0.18.1
Release:        %autorelease
Summary:        Rust crate "png"
License:        MIT OR Apache-2.0
URL:            https://github.com/image-rs/image-png
#!RemoteAsset:  sha256:60769b8b31b2a9f263dae2776c37b1b28ae246943cf719eb6946a1db05128a61
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2.0/default) >= 2.11.1
Requires:       crate(crc32fast-1.0/default) >= 1.5.0
Requires:       crate(fdeflate-0.3/default) >= 0.3.7
Requires:       crate(flate2-1.0/default) >= 1.1.9
Requires:       crate(miniz-oxide-0.8/default) >= 0.8.9
Requires:       crate(miniz-oxide-0.8/simd) >= 0.8.9
Provides:       crate(png) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/benchmarks)
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "png"

%package     -n %{name}+unstable
Summary:        PNG decoding and encoding library in pure Rust - feature "unstable"
Requires:       crate(%{pkgname})
Requires:       crate(crc32fast-1.0/nightly) >= 1.5.0
Provides:       crate(%{pkgname}/unstable)

%description -n %{name}+unstable
This metapackage enables feature "unstable" for the Rust png crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zlib-rs
Summary:        PNG decoding and encoding library in pure Rust - feature "zlib-rs"
Requires:       crate(%{pkgname})
Requires:       crate(flate2-1.0/zlib-rs) >= 1.1.9
Provides:       crate(%{pkgname}/zlib-rs)

%description -n %{name}+zlib-rs
This metapackage enables feature "zlib-rs" for the Rust png crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
