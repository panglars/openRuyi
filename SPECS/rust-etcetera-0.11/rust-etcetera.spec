# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name etcetera
%global full_version 0.11.0
%global pkgname etcetera-0.11

Name:           rust-etcetera-0.11
Version:        0.11.0
Release:        %autorelease
Summary:        Rust crate "etcetera"
License:        MIT OR Apache-2.0
URL:            https://github.com/lunacookies/etcetera
#!RemoteAsset:  sha256:de48cc4d1c1d97a20fd819def54b890cadde72ed3ad0c614822a0a433361be96
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1.0/default) >= 1.0.3
Requires:       crate(windows-sys-0.61/default) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-system-com) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-ui-shell) >= 0.61.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "etcetera"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
