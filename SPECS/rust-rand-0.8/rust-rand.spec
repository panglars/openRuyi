# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rand
%global full_version 0.8.6
%global pkgname rand-0.8

Name:           rust-rand-0.8
Version:        0.8.6
Release:        %autorelease
Summary:        Rust crate "rand"
License:        MIT OR Apache-2.0
URL:            https://rust-random.github.io/book
#!RemoteAsset:  sha256:5ca0ecfa931c29007047d1bc58e623ab12e5590e8c7cc53200d5202b69266d8a
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rand-core-0.6/default) >= 0.6.4
Provides:       crate(rand) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/log)
Provides:       crate(%{pkgname}/min-const-gen)
Provides:       crate(%{pkgname}/nightly)
Provides:       crate(%{pkgname}/small-rng)

%description
Source code for takopackized Rust crate "rand"

%package     -n %{name}+alloc
Summary:        Random number generators and other randomness functionality - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(rand-core-0.6/alloc) >= 0.6.4
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Random number generators and other randomness functionality - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/std-rng)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Random number generators and other randomness functionality - feature "getrandom"
Requires:       crate(%{pkgname})
Requires:       crate(rand-core-0.6/getrandom) >= 0.6.4
Provides:       crate(%{pkgname}/getrandom)

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        Random number generators and other randomness functionality - feature "libc"
Requires:       crate(%{pkgname})
Requires:       crate(libc-0.2) >= 0.2.186
Provides:       crate(%{pkgname}/libc)

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-chacha
Summary:        Random number generators and other randomness functionality - feature "rand_chacha" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(rand-chacha-0.3) >= 0.3.1
Provides:       crate(%{pkgname}/rand-chacha)
Provides:       crate(%{pkgname}/std-rng)

%description -n %{name}+rand-chacha
This metapackage enables feature "rand_chacha" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "std_rng" feature.

%package     -n %{name}+serde
Summary:        Random number generators and other randomness functionality - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.228
Requires:       crate(serde-1.0/derive) >= 1.0.228
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde1
Summary:        Random number generators and other randomness functionality - feature "serde1"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/serde)
Requires:       crate(rand-core-0.6/serde1) >= 0.6.4
Provides:       crate(%{pkgname}/serde1)

%description -n %{name}+serde1
This metapackage enables feature "serde1" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Random number generators and other randomness functionality - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/getrandom)
Requires:       crate(%{pkgname}/libc)
Requires:       crate(rand-chacha-0.3/std) >= 0.3.1
Requires:       crate(rand-core-0.6/std) >= 0.6.4
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust rand crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
