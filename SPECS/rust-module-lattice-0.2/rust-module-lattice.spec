# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name module-lattice
%global full_version 0.2.2
%global pkgname module-lattice-0.2

Name:           rust-module-lattice-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "module-lattice"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/KEMs/tree/master/module-lattice
#!RemoteAsset:  sha256:dc7c90d33a0dac244570c26461d761ffaeadb3bfc2b17cc625ae2185cafdffae
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hybrid-array-0.4/default) >= 0.4.11
Requires:       crate(hybrid-array-0.4/extra-sizes) >= 0.4.11
Requires:       crate(num-traits-0.2) >= 0.2.19
Provides:       crate(module-lattice) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "module-lattice"

%package     -n %{name}+ctutils
Summary:        Functionality shared between the `ml-kem` and `ml-dsa` crates, including linear algebra with degree-256 polynomials over a prime-order field, vectors of such polynomials, and NTT polynomials and vectors, as well as packing of polynomials into coefficients with a specified number of bits - feature "ctutils"
Requires:       crate(%{pkgname})
Requires:       crate(ctutils-0.4/default) >= 0.4.2
Requires:       crate(hybrid-array-0.4/ctutils) >= 0.4.11
Requires:       crate(hybrid-array-0.4/extra-sizes) >= 0.4.11
Provides:       crate(%{pkgname}/ctutils)

%description -n %{name}+ctutils
This metapackage enables feature "ctutils" for the Rust module-lattice crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Functionality shared between the `ml-kem` and `ml-dsa` crates, including linear algebra with degree-256 polynomials over a prime-order field, vectors of such polynomials, and NTT polynomials and vectors, as well as packing of polynomials into coefficients with a specified number of bits - feature "zeroize"
Requires:       crate(%{pkgname})
Requires:       crate(hybrid-array-0.4/extra-sizes) >= 0.4.11
Requires:       crate(hybrid-array-0.4/zeroize) >= 0.4.11
Requires:       crate(zeroize-1.0) >= 1.8.1
Provides:       crate(%{pkgname}/zeroize)

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust module-lattice crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
