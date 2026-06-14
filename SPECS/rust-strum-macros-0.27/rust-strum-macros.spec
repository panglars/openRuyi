# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name strum_macros
%global full_version 0.27.2
%global pkgname strum-macros-0.27

Name:           rust-strum-macros-0.27
Version:        0.27.2
Release:        %autorelease
Summary:        Rust crate "strum_macros"
License:        MIT
URL:            https://github.com/Peternator7/strum
#!RemoteAsset:  sha256:7695ce3845ea4b33927c055a39dc438a45b059f7c1b3d91d38d10355fb8cbca7
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(heck-0.5/default) >= 0.5.0
Requires:       crate(proc-macro2-1.0/default) >= 1.0.106
Requires:       crate(quote-1.0/default) >= 1.0.45
Requires:       crate(syn-2.0/default) >= 2.0.117
Requires:       crate(syn-2.0/parsing) >= 2.0.117
Provides:       crate(strum-macros) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "strum_macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
