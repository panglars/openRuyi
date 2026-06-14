# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tracing-appender
%global full_version 0.2.5
%global pkgname tracing-appender-0.2

Name:           rust-tracing-appender-0.2
Version:        0.2.5
Release:        %autorelease
Summary:        Rust crate "tracing-appender"
License:        MIT
URL:            https://tokio.rs
#!RemoteAsset:  sha256:050686193eb999b4bb3bc2acfa891a13da00f79734704c4b8b4ef1a10b368a3c
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crossbeam-channel-0.5/default) >= 0.5.15
Requires:       crate(symlink-0.1/default) >= 0.1.0
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Requires:       crate(time-0.3/formatting) >= 0.3.47
Requires:       crate(time-0.3/parsing) >= 0.3.47
Requires:       crate(tracing-subscriber-0.3/fmt) >= 0.3.23
Requires:       crate(tracing-subscriber-0.3/std) >= 0.3.23
Provides:       crate(tracing-appender) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "tracing-appender"

%package     -n %{name}+parking-lot
Summary:        Provides utilities for file appenders and making non-blocking writers - feature "parking_lot"
Requires:       crate(%{pkgname})
Requires:       crate(parking-lot-0.12/default) >= 0.12.1
Provides:       crate(%{pkgname}/parking-lot)

%description -n %{name}+parking-lot
This metapackage enables feature "parking_lot" for the Rust tracing-appender crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
