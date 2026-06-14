# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name exr
%global full_version 1.74.0
%global pkgname exr-1.0

Name:           rust-exr-1.0
Version:        1.74.0
Release:        %autorelease
Summary:        Rust crate "exr"
License:        BSD-3-Clause
URL:            https://github.com/johannesvollmer/exrs
#!RemoteAsset:  sha256:4300e043a56aa2cb633c01af81ca8f699a321879a7854d3896a0ba89056363be
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bit-field-0.10/default) >= 0.10.3
Requires:       crate(half-2.0/default) >= 2.7.1
Requires:       crate(lebe-0.5/default) >= 0.5.3
Requires:       crate(miniz-oxide-0.8/default) >= 0.8.9
Requires:       crate(smallvec-1.0/default) >= 1.15.1
Requires:       crate(zune-inflate-0.2/zlib) >= 0.2.54
Provides:       crate(exr) = %{version}
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "exr"

%package     -n %{name}+rayon
Summary:        Read and write OpenEXR files without any unsafe code - feature "rayon" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(rayon-core-1.0/default) >= 1.11.0
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/rayon)

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust exr crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
