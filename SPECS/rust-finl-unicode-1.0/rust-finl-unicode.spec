# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name finl_unicode
%global full_version 1.4.0
%global pkgname finl-unicode-1.0

Name:           rust-finl-unicode-1.0
Version:        1.4.0
Release:        %autorelease
Summary:        Rust crate "finl_unicode"
License:        (MIT OR Apache-2.0) AND Unicode-DFS-2016
URL:            https://finl.xyz
#!RemoteAsset:  sha256:9844ddc3a6e533d62bba727eb6c28b5d360921d5175e9ff0f1e621a5c590a4d5
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(finl-unicode) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/categories)
Provides:       crate(%{pkgname}/grapheme-clusters)

%description
Source code for takopackized Rust crate "finl_unicode"

%package     -n %{name}+default
Summary:        Handling Unicode functionality for finl (categories and grapheme segmentation) - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/categories)
Requires:       crate(%{pkgname}/grapheme-clusters)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust finl_unicode crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
