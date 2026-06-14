# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name md5
%global full_version 0.7.0
%global pkgname md5-0.7

Name:           rust-md5-0.7
Version:        0.7.0
Release:        %autorelease
Summary:        Rust crate "md5"
License:        Apache-2.0/MIT
URL:            https://github.com/stainless-steel/md5
#!RemoteAsset:  sha256:490cc448043f947bae3cbee9c203358d62dbee0db12107a74be5c30ccfd09771
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(md5) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "md5"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
