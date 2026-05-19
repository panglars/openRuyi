# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name interpolate_name
%global full_version 0.2.4
%global pkgname interpolate-name-0.2

Name:           rust-interpolate-name-0.2
Version:        0.2.4
Release:        %autorelease
Summary:        Rust crate "interpolate_name"
License:        MIT
URL:            https://github.com/lu-zero/interpolate_name
#!RemoteAsset:  sha256:c34819042dc3d3971c46c2190835914dfbe0c3c13f61449b2997f4e9722dfa60
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1.0/default) >= 1.0.106
Requires:       crate(quote-1.0/default) >= 1.0.45
Requires:       crate(syn-2.0/default) >= 2.0.117
Requires:       crate(syn-2.0/fold) >= 2.0.117
Requires:       crate(syn-2.0/full) >= 2.0.117
Provides:       crate(interpolate-name) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "interpolate_name"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
