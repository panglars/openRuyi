# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustc-demangle
%global full_version 0.1.27
%global pkgname rustc-demangle-0.1

Name:           rust-rustc-demangle-0.1
Version:        0.1.27
Release:        %autorelease
Summary:        Rust crate "rustc-demangle"
License:        MIT/Apache-2.0
URL:            https://github.com/rust-lang/rustc-demangle
#!RemoteAsset:  sha256:b50b8869d9fc858ce7266cce0194bd74df58b9d0e3f6df3a9fc8eb470d95c09d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(rustc-demangle) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/compiler-builtins)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "rustc-demangle"

%package     -n %{name}+core
Summary:        Rust compiler symbol demangling - feature "core" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(rustc-std-workspace-core-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/core)
Provides:       crate(%{pkgname}/rustc-dep-of-std)

%description -n %{name}+core
This metapackage enables feature "core" for the Rust rustc-demangle crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "rustc-dep-of-std" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
