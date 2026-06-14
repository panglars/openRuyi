# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name console_error_panic_hook
%global full_version 0.1.7
%global pkgname console-error-panic-hook-0.1

Name:           rust-console-error-panic-hook-0.1
Version:        0.1.7
Release:        %autorelease
Summary:        Rust crate "console_error_panic_hook"
License:        Apache-2.0/MIT
URL:            https://github.com/rustwasm/console_error_panic_hook
#!RemoteAsset:  sha256:a06aeb73f470f66dcdbf7223caeebb85984942f22f1adb2a088cf9668146bbbc
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1.0/default) >= 1.0.3
Requires:       crate(wasm-bindgen-0.2/default) >= 0.2.105
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "console_error_panic_hook"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
