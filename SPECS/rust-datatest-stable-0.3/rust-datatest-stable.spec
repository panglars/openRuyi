# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name datatest-stable
%global full_version 0.3.3
%global pkgname datatest-stable-0.3

Name:           rust-datatest-stable-0.3
Version:        0.3.3
Release:        %autorelease
Summary:        Rust crate "datatest-stable"
License:        MIT OR Apache-2.0
URL:            https://github.com/nextest-rs/datatest-stable
#!RemoteAsset:  sha256:a867d7322eb69cf3a68a5426387a25b45cb3b9c5ee41023ee6cea92e2afadd82
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(camino-1.0/default) >= 1.2.2
Requires:       crate(fancy-regex-0.14/default) >= 0.14.0
Requires:       crate(libtest-mimic-0.8/default) >= 0.8.1
Requires:       crate(walkdir-2.0/default) >= 2.5.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "datatest-stable"

%package     -n %{name}+include-dir
Summary:        Data-driven tests that work on stable Rust - feature "include-dir"
Requires:       crate(%{pkgname})
Requires:       crate(include-dir-0.7/default) >= 0.7.4
Provides:       crate(%{pkgname}/include-dir)

%description -n %{name}+include-dir
This metapackage enables feature "include-dir" for the Rust datatest-stable crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
