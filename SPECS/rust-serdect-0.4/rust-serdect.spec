# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serdect
%global full_version 0.4.3
%global pkgname serdect-0.4

Name:           rust-serdect-0.4
Version:        0.4.3
Release:        %autorelease
Summary:        Rust crate "serdect"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/formats/tree/master/serdect
#!RemoteAsset:  sha256:66cf8fedced2fcf12406bcb34223dffb92eaf34908ede12fed414c82b7f00b3e
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base16ct-1.0) >= 1.0.0
Requires:       crate(serde-1.0) >= 1.0.228
Provides:       crate(serdect) = %{version}
Provides:       crate(%{pkgname})

%description
cryptographic keys)
Source code for takopackized Rust crate "serdect"

%package     -n %{name}+alloc
Summary:        Constant-time serde serializer/deserializer helpers for data that potentially contains secrets (e.g - feature "alloc" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(base16ct-1.0/alloc) >= 1.0.0
Requires:       crate(serde-1.0/alloc) >= 1.0.228
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+alloc
cryptographic keys)
This metapackage enables feature "alloc" for the Rust serdect crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+derive
Summary:        Constant-time serde serializer/deserializer helpers for data that potentially contains secrets (e.g - feature "derive"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/derive) >= 1.0.228
Provides:       crate(%{pkgname}/derive)

%description -n %{name}+derive
cryptographic keys)
This metapackage enables feature "derive" for the Rust serdect crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Constant-time serde serializer/deserializer helpers for data that potentially contains secrets (e.g - feature "zeroize"
Requires:       crate(%{pkgname})
Requires:       crate(zeroize-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/zeroize)

%description -n %{name}+zeroize
cryptographic keys)
This metapackage enables feature "zeroize" for the Rust serdect crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
