# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name assert_matches
%global full_version 1.5.0
%global pkgname assert-matches-1.0

Name:           rust-assert-matches-1.0
Version:        1.5.0
Release:        %autorelease
Summary:        Rust crate "assert_matches"
License:        MIT/Apache-2.0
URL:            https://github.com/murarth/assert_matches
#!RemoteAsset:  sha256:9b34d609dfbaf33d6889b2b7106d3ca345eacad44200913df5ba02bfd31d2ba9
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(assert-matches) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "assert_matches"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
