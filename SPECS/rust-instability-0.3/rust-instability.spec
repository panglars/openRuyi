# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name instability
%global full_version 0.3.12
%global pkgname instability-0.3

Name:           rust-instability-0.3
Version:        0.3.12
Release:        %autorelease
Summary:        Rust crate "instability"
License:        MIT
URL:            https://github.com/ratatui/instability
#!RemoteAsset:  sha256:5eb2d60ef19920a3a9193c3e371f726ec1dafc045dac788d0fb3704272458971
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(darling-0.23/default) >= 0.23.0
Requires:       crate(indoc-2.0/default) >= 2.0.7
Requires:       crate(proc-macro2-1.0/default) >= 1.0.106
Requires:       crate(quote-1.0/default) >= 1.0.45
Requires:       crate(syn-2.0/default) >= 2.0.117
Requires:       crate(syn-2.0/derive) >= 2.0.117
Requires:       crate(syn-2.0/full) >= 2.0.117
Provides:       crate(instability) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
A fork of the `stability` crate.
Source code for takopackized Rust crate "instability"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
