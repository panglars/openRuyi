# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name spki
%global full_version 0.8.0-rc.4
%global pkgname spki-0.8.0-rc.4

Name:           rust-spki-0.8.0-rc.4
Version:        0.8.0
Release:        %autorelease
Summary:        Rust crate "spki"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/formats/tree/master/spki
#!RemoteAsset:  sha256:8baeff88f34ed0691978ec34440140e1572b68c7dd4a495fd14a3dc1944daa80
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(der-0.8/default) >= 0.8.0
Requires:       crate(der-0.8/oid) >= 0.8.0
Provides:       crate(spki) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
OIDs)
Source code for takopackized Rust crate "spki"

%package     -n %{name}+alloc
Summary:        X.509 Subject Public Key Info (RFC5280) describing public keys as well as their associated AlgorithmIdentifiers (i.e - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(base64ct-1.0/alloc) >= 1.8.3
Requires:       crate(der-0.8/alloc) >= 0.8.0
Requires:       crate(der-0.8/oid) >= 0.8.0
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
OIDs)
This metapackage enables feature "alloc" for the Rust spki crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+arbitrary
Summary:        X.509 Subject Public Key Info (RFC5280) describing public keys as well as their associated AlgorithmIdentifiers (i.e - feature "arbitrary"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(arbitrary-1.0/default) >= 1.4
Requires:       crate(arbitrary-1.0/derive) >= 1.4
Requires:       crate(der-0.8/arbitrary) >= 0.8.0
Requires:       crate(der-0.8/oid) >= 0.8.0
Provides:       crate(%{pkgname}/arbitrary)

%description -n %{name}+arbitrary
OIDs)
This metapackage enables feature "arbitrary" for the Rust spki crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+base64
Summary:        X.509 Subject Public Key Info (RFC5280) describing public keys as well as their associated AlgorithmIdentifiers (i.e - feature "base64"
Requires:       crate(%{pkgname})
Requires:       crate(base64ct-1.0) >= 1.8.3
Provides:       crate(%{pkgname}/base64)

%description -n %{name}+base64
OIDs)
This metapackage enables feature "base64" for the Rust spki crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+digest
Summary:        X.509 Subject Public Key Info (RFC5280) describing public keys as well as their associated AlgorithmIdentifiers (i.e - feature "digest"
Requires:       crate(%{pkgname})
Requires:       crate(digest-0.11.0-rc.0) >= 0.11.0-rc.0
Provides:       crate(%{pkgname}/digest)

%description -n %{name}+digest
OIDs)
This metapackage enables feature "digest" for the Rust spki crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fingerprint
Summary:        X.509 Subject Public Key Info (RFC5280) describing public keys as well as their associated AlgorithmIdentifiers (i.e - feature "fingerprint"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/digest)
Requires:       crate(%{pkgname}/sha2)
Provides:       crate(%{pkgname}/fingerprint)

%description -n %{name}+fingerprint
OIDs)
This metapackage enables feature "fingerprint" for the Rust spki crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pem
Summary:        X.509 Subject Public Key Info (RFC5280) describing public keys as well as their associated AlgorithmIdentifiers (i.e - feature "pem"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(der-0.8/oid) >= 0.8.0
Requires:       crate(der-0.8/pem) >= 0.8.0
Provides:       crate(%{pkgname}/pem)

%description -n %{name}+pem
OIDs)
This metapackage enables feature "pem" for the Rust spki crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha2
Summary:        X.509 Subject Public Key Info (RFC5280) describing public keys as well as their associated AlgorithmIdentifiers (i.e - feature "sha2"
Requires:       crate(%{pkgname})
Requires:       crate(sha2-0.11.0-rc.0) >= 0.11.0-rc.0
Provides:       crate(%{pkgname}/sha2)

%description -n %{name}+sha2
OIDs)
This metapackage enables feature "sha2" for the Rust spki crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        X.509 Subject Public Key Info (RFC5280) describing public keys as well as their associated AlgorithmIdentifiers (i.e - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(der-0.8/oid) >= 0.8.0
Requires:       crate(der-0.8/std) >= 0.8.0
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
OIDs)
This metapackage enables feature "std" for the Rust spki crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
