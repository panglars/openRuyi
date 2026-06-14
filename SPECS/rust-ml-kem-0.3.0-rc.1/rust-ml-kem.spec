# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ml-kem
%global full_version 0.3.0-rc.1
%global pkgname ml-kem-0.3.0-rc.1

Name:           rust-ml-kem-0.3.0-rc.1
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "ml-kem"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/KEMs/tree/master/ml-kem
#!RemoteAsset:  sha256:8198b5db27ac9773534c371751a59dc18aec8b80aa141e69abfdd1dec2e3f78c
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hybrid-array-0.4/ctutils) >= 0.4.11
Requires:       crate(hybrid-array-0.4/default) >= 0.4.11
Requires:       crate(hybrid-array-0.4/extra-sizes) >= 0.4.11
Requires:       crate(kem-0.3/default) >= 0.3.0
Requires:       crate(module-lattice-0.2/ctutils) >= 0.2.2
Requires:       crate(module-lattice-0.2/default) >= 0.2.2
Requires:       crate(rand-core-0.10/default) >= 0.10.1
Requires:       crate(sha3-0.11) >= 0.11.0
Provides:       crate(ml-kem) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/hazmat)

%description
Source code for takopackized Rust crate "ml-kem"

%package     -n %{name}+alloc
Summary:        Pure Rust implementation of the Module-Lattice-Based Key-Encapsulation Mechanism Standard (formerly known as Kyber) as described in FIPS 203 - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(pkcs8-0.11.0-rc.11/alloc) >= 0.11.0-rc.11
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust ml-kem crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Pure Rust implementation of the Module-Lattice-Based Key-Encapsulation Mechanism Standard (formerly known as Kyber) as described in FIPS 203 - feature "getrandom"
Requires:       crate(%{pkgname})
Requires:       crate(kem-0.3/getrandom) >= 0.3.0
Provides:       crate(%{pkgname}/getrandom)

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust ml-kem crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pem
Summary:        Pure Rust implementation of the Module-Lattice-Based Key-Encapsulation Mechanism Standard (formerly known as Kyber) as described in FIPS 203 - feature "pem"
Requires:       crate(%{pkgname})
Requires:       crate(pkcs8-0.11.0-rc.11/pem) >= 0.11.0-rc.11
Provides:       crate(%{pkgname}/pem)

%description -n %{name}+pem
This metapackage enables feature "pem" for the Rust ml-kem crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkcs8
Summary:        Pure Rust implementation of the Module-Lattice-Based Key-Encapsulation Mechanism Standard (formerly known as Kyber) as described in FIPS 203 - feature "pkcs8"
Requires:       crate(%{pkgname})
Requires:       crate(const-oid-0.10/db) >= 0.10.1
Requires:       crate(pkcs8-0.11.0-rc.11) >= 0.11.0-rc.11
Provides:       crate(%{pkgname}/pkcs8)

%description -n %{name}+pkcs8
This metapackage enables feature "pkcs8" for the Rust ml-kem crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Pure Rust implementation of the Module-Lattice-Based Key-Encapsulation Mechanism Standard (formerly known as Kyber) as described in FIPS 203 - feature "zeroize"
Requires:       crate(%{pkgname})
Requires:       crate(module-lattice-0.2/ctutils) >= 0.2.2
Requires:       crate(module-lattice-0.2/zeroize) >= 0.2.2
Requires:       crate(zeroize-1.0) >= 1.8.1
Provides:       crate(%{pkgname}/zeroize)

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust ml-kem crate, by pulling in any additional dependencies needed by that feature.

%install -a
if [ -d "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}" ]; then
    mv "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}" \
       "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}"
fi

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
