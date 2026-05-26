# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name windows-interface
%global full_version 0.59.3
%global pkgname windows-interface-0.59

Name:           rust-windows-interface-0.59
Version:        0.59.3
Release:        %autorelease
Summary:        Rust crate "windows-interface"
License:        MIT OR Apache-2.0
URL:            https://github.com/microsoft/windows-rs
#!RemoteAsset:  sha256:3f316c4a2570ba26bbec722032c4099d8c8bc095efccdc15688708623367e358
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1.0) >= 1.0.106
Requires:       crate(quote-1.0) >= 1.0.45
Requires:       crate(syn-2.0/clone-impls) >= 2.0.117
Requires:       crate(syn-2.0/full) >= 2.0.117
Requires:       crate(syn-2.0/parsing) >= 2.0.117
Requires:       crate(syn-2.0/printing) >= 2.0.117
Requires:       crate(syn-2.0/proc-macro) >= 2.0.117
Provides:       crate(windows-interface) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "windows-interface"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
