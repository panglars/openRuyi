# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wezterm-dynamic-derive
%global full_version 0.1.1
%global pkgname wezterm-dynamic-derive-0.1

Name:           rust-wezterm-dynamic-derive-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "wezterm-dynamic-derive"
License:        MIT
URL:            https://github.com/wezterm/wezterm
#!RemoteAsset:  sha256:46c0cf2d539c645b448eaffec9ec494b8b19bd5077d9e58cb1ae7efece8d575b
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1.0/default) >= 1.0.106
Requires:       crate(quote-1.0/default) >= 1.0.45
Requires:       crate(syn-1.0/default) >= 1.0.109
Requires:       crate(syn-1.0/extra-traits) >= 1.0.109
Provides:       crate(wezterm-dynamic-derive) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "wezterm-dynamic-derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
