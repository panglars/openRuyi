# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name xterm-color
%global full_version 1.0.2
%global pkgname xterm-color-1.0

Name:           rust-xterm-color-1.0
Version:        1.0.2
Release:        %autorelease
Summary:        Rust crate "xterm-color"
License:        MIT OR Apache-2.0
URL:            https://github.com/tautropfli/terminal-colorsaurus
#!RemoteAsset:  sha256:7008a9d8ba97a7e47d9b2df63fcdb8dade303010c5a7cd5bf2469d4da6eba673
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(xterm-color) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "xterm-color"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
