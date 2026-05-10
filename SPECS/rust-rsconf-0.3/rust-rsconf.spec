# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rsconf
%global full_version 0.3.0
%global pkgname rsconf-0.3

Name:           rust-rsconf-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "rsconf"
License:        MIT OR Apache-2.0
URL:            https://github.com/mqudsi/rsconf/
#!RemoteAsset:  sha256:06cbd984e96cc891aa018958ac3d09986c0ea7635eedfff670b99a90970f159f
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1.0/default) >= 1.0.69
Provides:       crate(rsconf) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/nightly)

%description
A sane autoconf w/ build.rs helpers for testing for system headers, libraries, and symbols
Source code for takopackized Rust crate "rsconf"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
