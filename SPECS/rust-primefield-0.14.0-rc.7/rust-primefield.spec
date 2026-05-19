# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name primefield
%global full_version 0.14.0-rc.7
%global pkgname primefield-0.14.0-rc.7

Name:           rust-primefield-0.14.0-rc.7
Version:        0.14.0
Release:        %autorelease
Summary:        Rust crate "primefield"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/elliptic-curves/tree/master/primefield
#!RemoteAsset:  sha256:93401c13cc7ff24684571cfca9d3cf9ebabfaf3d4b7b9963ade41ec54da196b5
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crypto-bigint-0.7.0-rc.28/hybrid-array) >= 0.7.0-rc.28
Requires:       crate(crypto-bigint-0.7.0-rc.28/rand-core) >= 0.7.0-rc.28
Requires:       crate(crypto-bigint-0.7.0-rc.28/subtle) >= 0.7.0-rc.28
Requires:       crate(crypto-common-0.2/default) >= 0.2.1
Requires:       crate(crypto-common-0.2/rand-core) >= 0.2.1
Requires:       crate(rand-core-0.10) >= 0.10.1
Requires:       crate(rustcrypto-ff-0.14.0-rc.1) >= 0.14.0-rc.1
Requires:       crate(subtle-2.0/const-generics) >= 2.6.1
Requires:       crate(zeroize-1.0) >= 1.8.2
Provides:       crate(primefield) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "primefield"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
