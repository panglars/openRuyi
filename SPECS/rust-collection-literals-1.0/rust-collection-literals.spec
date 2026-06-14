# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name collection_literals
%global full_version 1.0.2
%global pkgname collection-literals-1.0

Name:           rust-collection-literals-1.0
Version:        1.0.2
Release:        %autorelease
Summary:        Rust crate "collection_literals"
License:        MIT
URL:            https://github.com/staedoix/collection_literals
#!RemoteAsset:  sha256:26b3f65b8fb8e88ba339f7d23a390fe1b0896217da05e2a66c584c9b29a91df8
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "collection_literals"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
