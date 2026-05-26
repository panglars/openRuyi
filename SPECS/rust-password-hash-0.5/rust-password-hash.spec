# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name password-hash
%global full_version 0.5.0
%global pkgname password-hash-0.5

Name:           rust-password-hash-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "password-hash"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/traits/tree/master/password-hash
#!RemoteAsset:  sha256:346f04948ba92c43e8469c1ee6736c7563d71012b17d40745260fe106aac2166
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base64ct-1.0/default) >= 1.8.3
Requires:       crate(subtle-2.0) >= 2.6.1
Provides:       crate(password-hash) = %{version}
Provides:       crate(%{pkgname})

%description
MCF)
Source code for takopackized Rust crate "password-hash"

%package     -n %{name}+alloc
Summary:        Traits which describe the functionality of password hashing algorithms, as well as a `no_std`-friendly implementation of the PHC string format (a well-defined subset of the Modular Crypt Format a.k.a - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(base64ct-1.0/alloc) >= 1.8.3
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
MCF)
This metapackage enables feature "alloc" for the Rust password-hash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Traits which describe the functionality of password hashing algorithms, as well as a `no_std`-friendly implementation of the PHC string format (a well-defined subset of the Modular Crypt Format a.k.a - feature "getrandom"
Requires:       crate(%{pkgname})
Requires:       crate(rand-core-0.6/getrandom) >= 0.6.4
Provides:       crate(%{pkgname}/getrandom)

%description -n %{name}+getrandom
MCF)
This metapackage enables feature "getrandom" for the Rust password-hash crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Traits which describe the functionality of password hashing algorithms, as well as a `no_std`-friendly implementation of the PHC string format (a well-defined subset of the Modular Crypt Format a.k.a - feature "rand_core" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(rand-core-0.6) >= 0.6.4
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/rand-core)

%description -n %{name}+rand-core
MCF)
This metapackage enables feature "rand_core" for the Rust password-hash crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+std
Summary:        Traits which describe the functionality of password hashing algorithms, as well as a `no_std`-friendly implementation of the PHC string format (a well-defined subset of the Modular Crypt Format a.k.a - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(base64ct-1.0/std) >= 1.8.3
Requires:       crate(rand-core-0.6/std) >= 0.6.4
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
MCF)
This metapackage enables feature "std" for the Rust password-hash crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
