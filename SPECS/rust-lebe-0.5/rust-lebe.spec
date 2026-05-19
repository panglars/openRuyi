# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lebe
%global full_version 0.5.3
%global pkgname lebe-0.5

Name:           rust-lebe-0.5
Version:        0.5.3
Release:        %autorelease
Summary:        Rust crate "lebe"
License:        BSD-3-Clause
URL:            https://github.com/johannesvollmer/lebe
#!RemoteAsset:  sha256:7a79a3332a6609480d7d0c9eab957bca6b455b91bb84e66d19f5ff66294b85b8
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(lebe) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "lebe"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
