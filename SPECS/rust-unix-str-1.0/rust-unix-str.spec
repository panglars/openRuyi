# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unix_str
%global full_version 1.0.0
%global pkgname unix-str-1.0

Name:           rust-unix-str-1.0
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "unix_str"
License:        MIT OR Apache-2.0
URL:            https://gitlab.com/SnejUgal/unix_str
#!RemoteAsset:  sha256:2ace0b4755d0a2959962769239d56267f8a024fef2d9b32666b3dcd0946b0906
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(unix-str) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/shrink-to)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/toowned-clone-into)
Provides:       crate(%{pkgname}/unixstring-ascii)

%description
Source code for takopackized Rust crate "unix_str"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
