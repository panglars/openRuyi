# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name loop9
%global full_version 0.1.5
%global pkgname loop9-0.1

Name:           rust-loop9-0.1
Version:        0.1.5
Release:        %autorelease
Summary:        Rust crate "loop9"
License:        MIT
URL:            https://lib.rs/crates/loop9
#!RemoteAsset:  sha256:0fae87c125b03c1d2c0150c90365d7d6bcc53fb73a9acaef207d2d065860f062
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(imgref-1.0/default) >= 1.12.1
Provides:       crate(loop9) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Duplicates pixels on the edges.
Source code for takopackized Rust crate "loop9"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
