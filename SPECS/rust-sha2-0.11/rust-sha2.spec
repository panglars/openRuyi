# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sha2
%global full_version 0.11.0
%global pkgname sha2-0.11

Name:           rust-sha2-0.11
Version:        0.11.0
Release:        %autorelease
Summary:        Rust crate "sha2"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/hashes
#!RemoteAsset:  sha256:446ba717509524cb3f22f17ecc096f10f4822d76ab5c0b9822c5f9c284e825f4
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Requires:       crate(cpufeatures-0.3/default) >= 0.3.0
Requires:       crate(digest-0.11/default) >= 0.11.3
Provides:       crate(sha2) = %{version}
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "sha2"

%package     -n %{name}+alloc
Summary:        Pure Rust implementation of the SHA-2 hash function family including SHA-224, SHA-256, SHA-384, and SHA-512 - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(digest-0.11/alloc) >= 0.11.3
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust sha2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Pure Rust implementation of the SHA-2 hash function family including SHA-224, SHA-256, SHA-384, and SHA-512 - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/oid)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust sha2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+oid
Summary:        Pure Rust implementation of the SHA-2 hash function family including SHA-224, SHA-256, SHA-384, and SHA-512 - feature "oid"
Requires:       crate(%{pkgname})
Requires:       crate(digest-0.11/oid) >= 0.11.3
Provides:       crate(%{pkgname}/oid)

%description -n %{name}+oid
This metapackage enables feature "oid" for the Rust sha2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Pure Rust implementation of the SHA-2 hash function family including SHA-224, SHA-256, SHA-384, and SHA-512 - feature "zeroize"
Requires:       crate(%{pkgname})
Requires:       crate(digest-0.11/zeroize) >= 0.11.3
Provides:       crate(%{pkgname}/zeroize)

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust sha2 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
