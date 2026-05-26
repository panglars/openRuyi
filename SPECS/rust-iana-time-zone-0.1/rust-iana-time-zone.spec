# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name iana-time-zone
%global full_version 0.1.65
%global pkgname iana-time-zone-0.1

Name:           rust-iana-time-zone-0.1
Version:        0.1.65
Release:        %autorelease
Summary:        Rust crate "iana-time-zone"
License:        MIT OR Apache-2.0
URL:            https://github.com/strawlab/iana-time-zone
#!RemoteAsset:  sha256:e31bc9ad994ba00e440a8aa5c9ef0ec67d5cb5e5cb0cc7f8b744a35b389cc470
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(android-system-properties-0.1/default) >= 0.1.5
Requires:       crate(core-foundation-sys-0.8/default) >= 0.8.7
Requires:       crate(iana-time-zone-haiku-0.1/default) >= 0.1.2
Requires:       crate(js-sys-0.3/default) >= 0.3.98
Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(wasm-bindgen-0.2/default) >= 0.2.121
Requires:       crate(windows-core-0.62/default) >= 0.62.2
Provides:       crate(iana-time-zone) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/fallback)

%description
Source code for takopackized Rust crate "iana-time-zone"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
