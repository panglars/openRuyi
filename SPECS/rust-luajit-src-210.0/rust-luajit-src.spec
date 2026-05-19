# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name luajit-src
%global full_version 210.6.6+707c12b
%global pkgname luajit-src-210.0

Name:           rust-luajit-src-210.0
Version:        210.6.6
Release:        %autorelease
Summary:        Rust crate "luajit-src"
License:        MIT
URL:            https://github.com/mlua-rs/luajit-src-rs
#!RemoteAsset:  sha256:a86cc925d4053d0526ae7f5bc765dbd0d7a5d1a63d43974f4966cb349ca63295
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1.0/default) >= 1.2.62
Requires:       crate(which-8.0/default) >= 8.0.2
Provides:       crate(luajit-src) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "luajit-src"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
