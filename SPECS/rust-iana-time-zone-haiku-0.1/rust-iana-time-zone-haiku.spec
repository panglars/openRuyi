# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name iana-time-zone-haiku
%global full_version 0.1.2
%global pkgname iana-time-zone-haiku-0.1

Name:           rust-iana-time-zone-haiku-0.1
Version:        0.1.2
Release:        %autorelease
Summary:        Rust crate "iana-time-zone-haiku"
License:        MIT OR Apache-2.0
URL:            https://github.com/strawlab/iana-time-zone
#!RemoteAsset:  sha256:f31827a206f56af32e590ba56d5d2d085f558508192593743f16b2306495269f
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1.0/default) >= 1.2.62
Provides:       crate(iana-time-zone-haiku) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "iana-time-zone-haiku"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
