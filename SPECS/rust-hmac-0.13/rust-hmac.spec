# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hmac
%global full_version 0.13.0
%global pkgname hmac-0.13

Name:           rust-hmac-0.13
Version:        0.13.0
Release:        %autorelease
Summary:        Rust crate "hmac"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/MACs
#!RemoteAsset:  sha256:6303bc9732ae41b04cb554b844a762b4115a61bfaa81e3e83050991eeb56863f
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(digest-0.11/default) >= 0.11.3
Requires:       crate(digest-0.11/mac) >= 0.11.3
Provides:       crate(hmac) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "hmac"

%package     -n %{name}+zeroize
Summary:        Generic implementation of Hash-based Message Authentication Code (HMAC) - feature "zeroize"
Requires:       crate(%{pkgname})
Requires:       crate(digest-0.11/mac) >= 0.11.3
Requires:       crate(digest-0.11/zeroize) >= 0.11.3
Provides:       crate(%{pkgname}/zeroize)

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust hmac crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
