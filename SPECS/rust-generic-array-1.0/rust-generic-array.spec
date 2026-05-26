# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name generic-array
%global full_version 1.4.1
%global pkgname generic-array-1.0

Name:           rust-generic-array-1.0
Version:        1.4.1
Release:        %autorelease
Summary:        Rust crate "generic-array"
License:        MIT
URL:            https://github.com/fizyk20/generic-array.git
#!RemoteAsset:  sha256:dab9e9188e97a93276e1fe7b56401b851e2b45a46d045ca658100c1303ada649
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rustversion-1.0/default) >= 1.0.22
Requires:       crate(typenum-1.0/const-generics) >= 1.20.0
Requires:       crate(typenum-1.0/default) >= 1.20.0
Provides:       crate(generic-array) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/internals)

%description
Source code for takopackized Rust crate "generic-array"

%package     -n %{name}+arbitrary
Summary:        Generic types implementing functionality of arrays - feature "arbitrary"
Requires:       crate(%{pkgname})
Requires:       crate(arbitrary-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/arbitrary)

%description -n %{name}+arbitrary
This metapackage enables feature "arbitrary" for the Rust generic-array crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+as-slice
Summary:        Generic types implementing functionality of arrays - feature "as_slice"
Requires:       crate(%{pkgname})
Requires:       crate(as-slice-0.2) >= 0.2.0
Provides:       crate(%{pkgname}/as-slice)

%description -n %{name}+as-slice
This metapackage enables feature "as_slice" for the Rust generic-array crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bitvec
Summary:        Generic types implementing functionality of arrays - feature "bitvec"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/const-default)
Requires:       crate(bitvec-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/bitvec)

%description -n %{name}+bitvec
This metapackage enables feature "bitvec" for the Rust generic-array crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytemuck
Summary:        Generic types implementing functionality of arrays - feature "bytemuck"
Requires:       crate(%{pkgname})
Requires:       crate(bytemuck-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/bytemuck)

%description -n %{name}+bytemuck
This metapackage enables feature "bytemuck" for the Rust generic-array crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+compat-0-14
Summary:        Generic types implementing functionality of arrays - feature "compat-0_14"
Requires:       crate(%{pkgname})
Provides:       crate(%{pkgname}/compat-0-14)

%description -n %{name}+compat-0-14
This metapackage enables feature "compat-0_14" for the Rust generic-array crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+const-default
Summary:        Generic types implementing functionality of arrays - feature "const-default"
Requires:       crate(%{pkgname})
Requires:       crate(const-default-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/const-default)

%description -n %{name}+const-default
This metapackage enables feature "const-default" for the Rust generic-array crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+faster-hex
Summary:        Generic types implementing functionality of arrays - feature "faster-hex"
Requires:       crate(%{pkgname})
Requires:       crate(faster-hex-0.10) >= 0.10.0
Provides:       crate(%{pkgname}/faster-hex)

%description -n %{name}+faster-hex
This metapackage enables feature "faster-hex" for the Rust generic-array crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hybrid-array-0-4
Summary:        Generic types implementing functionality of arrays - feature "hybrid-array-0_4"
Requires:       crate(%{pkgname})
Requires:       crate(hybrid-array-0.4) >= 0.4.0
Provides:       crate(%{pkgname}/hybrid-array-0-4)

%description -n %{name}+hybrid-array-0-4
This metapackage enables feature "hybrid-array-0_4" for the Rust generic-array crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Generic types implementing functionality of arrays - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-core-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust generic-array crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+subtle
Summary:        Generic types implementing functionality of arrays - feature "subtle"
Requires:       crate(%{pkgname})
Requires:       crate(subtle-2.0) >= 2.0.0
Provides:       crate(%{pkgname}/subtle)

%description -n %{name}+subtle
This metapackage enables feature "subtle" for the Rust generic-array crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Generic types implementing functionality of arrays - feature "zeroize"
Requires:       crate(%{pkgname})
Requires:       crate(zeroize-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/zeroize)

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust generic-array crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
