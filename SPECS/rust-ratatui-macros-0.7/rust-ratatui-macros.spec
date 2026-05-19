# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ratatui-macros
%global full_version 0.7.0
%global pkgname ratatui-macros-0.7

Name:           rust-ratatui-macros-0.7
Version:        0.7.0
Release:        %autorelease
Summary:        Rust crate "ratatui-macros"
License:        MIT
URL:            https://github.com/ratatui/ratatui
#!RemoteAsset:  sha256:a7f1342a13e83e4bb9d0b793d0ea762be633f9582048c892ae9041ef39c936f4
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ratatui-core-0.1/default) >= 0.1.0
Requires:       crate(ratatui-widgets-0.3/default) >= 0.3.0
Provides:       crate(ratatui-macros) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "ratatui-macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
