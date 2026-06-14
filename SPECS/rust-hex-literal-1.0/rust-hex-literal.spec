# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hex-literal
%global full_version 1.1.0
%global pkgname hex-literal-1.0

Name:           rust-hex-literal-1.0
Version:        1.1.0
Release:        %autorelease
Summary:        Rust crate "hex-literal"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/utils
#!RemoteAsset:  sha256:e712f64ec3850b98572bffac52e2c6f282b29fe6c5fa6d42334b30be438d95c1
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(hex-literal) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "hex-literal"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
