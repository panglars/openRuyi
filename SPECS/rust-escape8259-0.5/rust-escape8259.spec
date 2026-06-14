# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name escape8259
%global full_version 0.5.3
%global pkgname escape8259-0.5

Name:           rust-escape8259-0.5
Version:        0.5.3
Release:        %autorelease
Summary:        Rust crate "escape8259"
License:        MIT
URL:            https://github.com/ericseppanen/escape8259
#!RemoteAsset:  sha256:5692dd7b5a1978a5aeb0ce83b7655c58ca8efdcb79d21036ea249da95afec2c6
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "escape8259"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
