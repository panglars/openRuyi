# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name inout
%global full_version 0.2.2
%global pkgname inout-0.2

Name:           rust-inout-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "inout"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/utils
#!RemoteAsset:  sha256:4250ce6452e92010fdf7268ccc5d14faa80bb12fc741938534c58f16804e03c7
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hybrid-array-0.4/default) >= 0.4.11
Provides:       crate(inout) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "inout"

%package     -n %{name}+block-padding
Summary:        Custom reference types for code generic over in-place and buffer-to-buffer modes of operation - feature "block-padding"
Requires:       crate(%{pkgname})
Requires:       crate(block-padding-0.4/default) >= 0.4.2
Provides:       crate(%{pkgname}/block-padding)

%description -n %{name}+block-padding
This metapackage enables feature "block-padding" for the Rust inout crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
