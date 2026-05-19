# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name twox-hash
%global full_version 2.1.2
%global pkgname twox-hash-2.0

Name:           rust-twox-hash-2.0
Version:        2.1.2
Release:        %autorelease
Summary:        Rust crate "twox-hash"
License:        MIT
URL:            https://github.com/shepmaster/twox-hash
#!RemoteAsset:  sha256:9ea3136b675547379c4bd395ca6b938e5ad3c3d20fad76e7fe85f9e0d011419c
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(twox-hash) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/xxhash32)
Provides:       crate(%{pkgname}/xxhash3-128)
Provides:       crate(%{pkgname}/xxhash3-64)
Provides:       crate(%{pkgname}/xxhash64)

%description
Source code for takopackized Rust crate "twox-hash"

%package     -n %{name}+default
Summary:        The XXHash and XXH3 algorithms - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/random)
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/xxhash3-128)
Requires:       crate(%{pkgname}/xxhash3-64)
Requires:       crate(%{pkgname}/xxhash32)
Requires:       crate(%{pkgname}/xxhash64)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust twox-hash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+random
Summary:        The XXHash and XXH3 algorithms - feature "random"
Requires:       crate(%{pkgname})
Requires:       crate(rand-0.9/thread-rng) >= 0.9.4
Provides:       crate(%{pkgname}/random)

%description -n %{name}+random
This metapackage enables feature "random" for the Rust twox-hash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serialize
Summary:        The XXHash and XXH3 algorithms - feature "serialize"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serialize)

%description -n %{name}+serialize
This metapackage enables feature "serialize" for the Rust twox-hash crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
