# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name signature
%global full_version 3.0.0
%global pkgname signature-3.0

Name:           rust-signature-3.0
Version:        3.0.0
Release:        %autorelease
Summary:        Rust crate "signature"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/traits
#!RemoteAsset:  sha256:28d567dcbaf0049cb8ac2608a76cd95ff9e4412e1899d389ee400918ca7537f5
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(signature) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)

%description
ECDSA, Ed25519)
Source code for takopackized Rust crate "signature"

%package     -n %{name}+digest
Summary:        Traits for cryptographic signature algorithms (e.g - feature "digest"
Requires:       crate(%{pkgname})
Requires:       crate(digest-0.11) >= 0.11.3
Provides:       crate(%{pkgname}/digest)

%description -n %{name}+digest
ECDSA, Ed25519)
This metapackage enables feature "digest" for the Rust signature crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Traits for cryptographic signature algorithms (e.g - feature "rand_core"
Requires:       crate(%{pkgname})
Requires:       crate(rand-core-0.10) >= 0.10.1
Provides:       crate(%{pkgname}/rand-core)

%description -n %{name}+rand-core
ECDSA, Ed25519)
This metapackage enables feature "rand_core" for the Rust signature crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
