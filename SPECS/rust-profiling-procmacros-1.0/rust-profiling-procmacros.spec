# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name profiling-procmacros
%global full_version 1.0.18
%global pkgname profiling-procmacros-1.0

Name:           rust-profiling-procmacros-1.0
Version:        1.0.18
Release:        %autorelease
Summary:        Rust crate "profiling-procmacros"
License:        MIT OR Apache-2.0
URL:            https://github.com/aclysma/profiling
#!RemoteAsset:  sha256:4488a4a36b9a4ba6b9334a32a39971f77c1436ec82c38707bce707699cc3bbcb
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(quote-1.0) >= 1.0.45
Requires:       crate(syn-2.0/default) >= 2.0.117
Requires:       crate(syn-2.0/full) >= 2.0.117
Provides:       crate(profiling-procmacros) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/profile-with-optick)
Provides:       crate(%{pkgname}/profile-with-puffin)
Provides:       crate(%{pkgname}/profile-with-superluminal)
Provides:       crate(%{pkgname}/profile-with-tracing)
Provides:       crate(%{pkgname}/profile-with-tracy)

%description
Source code for takopackized Rust crate "profiling-procmacros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
