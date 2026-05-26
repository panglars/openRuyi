# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rfc6979
%global full_version 0.5.0
%global pkgname rfc6979-0.5

Name:           rust-rfc6979-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "rfc6979"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/signatures/tree/master/rfc6979
#!RemoteAsset:  sha256:5236ce872cac07e0fb3969b0cbf468c7d2f37d432f1b627dcb7b8d34563fb0c3
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hmac-0.13) >= 0.13.0
Requires:       crate(subtle-2.0) >= 2.6.1
Provides:       crate(rfc6979) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "rfc6979"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
