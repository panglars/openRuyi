# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pkcs1
%global full_version 0.8.0-rc.4
%global pkgname pkcs1-0.8.0-rc.4

Name:           rust-pkcs1-0.8.0-rc.4
Version:        0.8.0
Release:        %autorelease
Summary:        Rust crate "pkcs1"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/formats/tree/master/pkcs1
#!RemoteAsset:  sha256:986d2e952779af96ea048f160fd9194e1751b4faea78bcf3ceb456efe008088e
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(der-0.8/default) >= 0.8.0
Requires:       crate(der-0.8/oid) >= 0.8.0
Requires:       crate(spki-0.8.0-rc.4/default) >= 0.8.0-rc.4
Provides:       crate(pkcs1) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "pkcs1"

%package     -n %{name}+alloc
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #1: RSA Cryptography Specifications Version 2.2 (RFC 8017) - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/zeroize)
Requires:       crate(der-0.8/alloc) >= 0.8.0
Requires:       crate(der-0.8/oid) >= 0.8.0
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust pkcs1 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pem
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #1: RSA Cryptography Specifications Version 2.2 (RFC 8017) - feature "pem"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(der-0.8/oid) >= 0.8.0
Requires:       crate(der-0.8/pem) >= 0.8.0
Provides:       crate(%{pkgname}/pem)

%description -n %{name}+pem
This metapackage enables feature "pem" for the Rust pkcs1 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #1: RSA Cryptography Specifications Version 2.2 (RFC 8017) - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(der-0.8/oid) >= 0.8.0
Requires:       crate(der-0.8/std) >= 0.8.0
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust pkcs1 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #1: RSA Cryptography Specifications Version 2.2 (RFC 8017) - feature "zeroize"
Requires:       crate(%{pkgname})
Requires:       crate(der-0.8/oid) >= 0.8.0
Requires:       crate(der-0.8/zeroize) >= 0.8.0
Provides:       crate(%{pkgname}/zeroize)

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust pkcs1 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
