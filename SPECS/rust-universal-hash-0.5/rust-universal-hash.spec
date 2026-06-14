# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name universal-hash
%global full_version 0.5.1
%global pkgname universal-hash-0.5

Name:           rust-universal-hash-0.5
Version:        0.5.1
Release:        %autorelease
Summary:        Rust crate "universal-hash"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/traits
#!RemoteAsset:  sha256:fc1de2c688dc15305988b563c3854064043356019f97a4b46276fe734c4f07ea
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crypto-common-0.1/default) >= 0.1.7
Requires:       crate(subtle-2.0) >= 2.6.1
Provides:       crate(universal-hash) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "universal-hash"

%package     -n %{name}+std
Summary:        Traits which describe the functionality of universal hash functions (UHFs) - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(crypto-common-0.1/std) >= 0.1.7
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust universal-hash crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
