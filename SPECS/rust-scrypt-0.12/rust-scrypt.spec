# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name scrypt
%global full_version 0.12.0
%global pkgname scrypt-0.12

Name:           rust-scrypt-0.12
Version:        0.12.0
Release:        %autorelease
Summary:        Rust crate "scrypt"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/password-hashes/tree/master/scrypt
#!RemoteAsset:  sha256:d87af57419b594aa23fa95f09f0e06d80d84ba01c26148c43844cad6ff4485f0
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Requires:       crate(pbkdf2-0.13/default) >= 0.13.0
Requires:       crate(salsa20-0.11) >= 0.11.0
Requires:       crate(sha2-0.11) >= 0.11.0
Provides:       crate(scrypt) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "scrypt"

%package     -n %{name}+alloc
Summary:        Scrypt password-based key derivation function - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(password-hash-0.6/alloc) >= 0.6.0
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust scrypt crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Scrypt password-based key derivation function - feature "getrandom"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/password-hash)
Requires:       crate(password-hash-0.6/getrandom) >= 0.6.0
Provides:       crate(%{pkgname}/getrandom)

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust scrypt crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+kdf
Summary:        Scrypt password-based key derivation function - feature "kdf"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(kdf-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/kdf)

%description -n %{name}+kdf
This metapackage enables feature "kdf" for the Rust scrypt crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mcf
Summary:        Scrypt password-based key derivation function - feature "mcf"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/phc)
Requires:       crate(ctutils-0.4/default) >= 0.4.0
Requires:       crate(mcf-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/mcf)

%description -n %{name}+mcf
This metapackage enables feature "mcf" for the Rust scrypt crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parallel
Summary:        Scrypt password-based key derivation function - feature "parallel"
Requires:       crate(%{pkgname})
Requires:       crate(rayon-1.0/default) >= 1.11
Provides:       crate(%{pkgname}/parallel)

%description -n %{name}+parallel
This metapackage enables feature "parallel" for the Rust scrypt crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+password-hash
Summary:        Scrypt password-based key derivation function - feature "password-hash"
Requires:       crate(%{pkgname})
Requires:       crate(password-hash-0.6) >= 0.6.0
Provides:       crate(%{pkgname}/password-hash)

%description -n %{name}+password-hash
This metapackage enables feature "password-hash" for the Rust scrypt crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+phc
Summary:        Scrypt password-based key derivation function - feature "phc"
Requires:       crate(%{pkgname})
Requires:       crate(password-hash-0.6/phc) >= 0.6.0
Provides:       crate(%{pkgname}/phc)

%description -n %{name}+phc
This metapackage enables feature "phc" for the Rust scrypt crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Scrypt password-based key derivation function - feature "rand_core"
Requires:       crate(%{pkgname})
Requires:       crate(password-hash-0.6/rand-core) >= 0.6.0
Provides:       crate(%{pkgname}/rand-core)

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust scrypt crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
