# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name line-clipping
%global full_version 0.3.7
%global pkgname line-clipping-0.3

Name:           rust-line-clipping-0.3
Version:        0.3.7
Release:        %autorelease
Summary:        Rust crate "line-clipping"
License:        MIT OR Apache-2.0
URL:            https://github.com/ratatui/line-clipping
#!RemoteAsset:  sha256:3f50e8f47623268b5407192d26876c4d7f89d686ca130fdc53bced4814cd29f8
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2.0/default) >= 2.11.1
Provides:       crate(line-clipping) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "line-clipping"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
