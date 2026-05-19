# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name toml_parser
%global full_version 1.1.2+spec-1.1.0
%global pkgname toml-parser-1.1.2

Name:           rust-toml-parser-1.1.2
Version:        1.1.2
Release:        %autorelease
Summary:        Rust crate "toml_parser"
License:        MIT OR Apache-2.0
URL:            https://github.com/toml-rs/toml
#!RemoteAsset:  sha256:a2abe9b86193656635d2411dc43050282ca48aa31c2451210f4202550afb7526
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(winnow-1.0.2) >= 1.0.2
Provides:       crate(toml-parser) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/unsafe)

%description
Source code for takopackized Rust crate "toml_parser"

%package     -n %{name}+debug
Summary:        Yet another format-preserving TOML parser - feature "debug"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(anstream-1.0/default) >= 1.0.0
Requires:       crate(anstyle-1.0/default) >= 1.0.14
Provides:       crate(%{pkgname}/debug)

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust toml_parser crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+simd
Summary:        Yet another format-preserving TOML parser - feature "simd"
Requires:       crate(%{pkgname})
Requires:       crate(winnow-1.0.2/simd) >= 1.0.2
Provides:       crate(%{pkgname}/simd)

%description -n %{name}+simd
This metapackage enables feature "simd" for the Rust toml_parser crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
