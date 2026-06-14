# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name universal-hash
%global full_version 0.6.1
%global pkgname universal-hash-0.6

Name:           rust-universal-hash-0.6
Version:        0.6.1
Release:        %autorelease
Summary:        Rust crate "universal-hash"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/traits
#!RemoteAsset:  sha256:f4987bdc12753382e0bec4a65c50738ffaabc998b9cdd1f952fb5f39b0048a96
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crypto-common-0.2/default) >= 0.2.1
Requires:       crate(ctutils-0.4/default) >= 0.4.2
Provides:       crate(universal-hash) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "universal-hash"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
