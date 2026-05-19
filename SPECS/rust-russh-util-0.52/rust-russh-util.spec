# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name russh-util
%global full_version 0.52.0
%global pkgname russh-util-0.52

Name:           rust-russh-util-0.52
Version:        0.52.0
Release:        %autorelease
Summary:        Rust crate "russh-util"
License:        Apache-2.0
URL:            https://github.com/warp-tech/russh
#!RemoteAsset:  sha256:668424a5dde0bcb45b55ba7de8476b93831b4aa2fa6947e145f3b053e22c60b6
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(chrono-0.4/default) >= 0.4.44
Requires:       crate(tokio-1.0/default) >= 1.52.3
Requires:       crate(tokio-1.0/io-util) >= 1.52.3
Requires:       crate(tokio-1.0/macros) >= 1.52.3
Requires:       crate(tokio-1.0/rt) >= 1.52.3
Requires:       crate(tokio-1.0/rt-multi-thread) >= 1.52.3
Requires:       crate(tokio-1.0/sync) >= 1.52.3
Requires:       crate(wasm-bindgen-0.2/default) >= 0.2.121
Requires:       crate(wasm-bindgen-futures-0.4/default) >= 0.4.71
Provides:       crate(russh-util) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "russh-util"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
