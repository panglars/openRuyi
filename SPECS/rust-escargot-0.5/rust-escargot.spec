# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name escargot
%global full_version 0.5.15
%global pkgname escargot-0.5

Name:           rust-escargot-0.5
Version:        0.5.15
Release:        %autorelease
Summary:        Rust crate "escargot"
License:        MIT OR Apache-2.0
URL:            https://github.com/crate-ci/escargot
#!RemoteAsset:  sha256:11c3aea32bc97b500c9ca6a72b768a26e558264303d101d3409cf6d57a9ed0cf
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(serde-1.0/default) >= 1.0.228
Requires:       crate(serde-1.0/derive) >= 1.0.228
Requires:       crate(serde-json-1.0/default) >= 1.0.149
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/cargo-unstable)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/print)
Provides:       crate(%{pkgname}/strict-unstable)
Provides:       crate(%{pkgname}/test-unstable)

%description
Source code for takopackized Rust crate "escargot"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
