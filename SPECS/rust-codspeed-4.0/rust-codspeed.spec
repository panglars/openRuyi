# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name codspeed
%global full_version 4.4.1
%global pkgname codspeed-4.0

Name:           rust-codspeed-4.0
Version:        4.4.1
Release:        %autorelease
Summary:        Rust crate "codspeed"
License:        MIT OR Apache-2.0
URL:            https://codspeed.io
#!RemoteAsset:  sha256:b684e94583e85a5ca7e1a6454a89d76a5121240f2fb67eb564129d9bafdb9db0
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1.0/default) >= 1.0.102
Requires:       crate(cc-1.0/default) >= 1.2.38
Requires:       crate(colored-2.0/default) >= 2.2.0
Requires:       crate(getrandom-0.2/default) >= 0.2.16
Requires:       crate(glob-0.3/default) >= 0.3.3
Requires:       crate(libc-0.2/default) >= 0.2.186
Requires:       crate(nix-0.31/default) >= 0.31.2
Requires:       crate(nix-0.31/time) >= 0.31.2
Requires:       crate(serde-1.0/default) >= 1.0.228
Requires:       crate(serde-1.0/derive) >= 1.0.228
Requires:       crate(serde-json-1.0/default) >= 1.0.149
Requires:       crate(statrs-0.18) >= 0.18.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "codspeed"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
