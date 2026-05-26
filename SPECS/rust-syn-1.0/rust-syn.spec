# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name syn
%global full_version 1.0.109
%global pkgname syn-1.0

Name:           rust-syn-1.0
Version:        1.0.109
Release:        %autorelease
Summary:        Rust crate "syn"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/syn
#!RemoteAsset:  sha256:72b64191b275b66ffe2469e8af2c1cfe3bafa67b529ead792a6d0160888b4237
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1.0) >= 1.0.106
Requires:       crate(unicode-ident-1.0/default) >= 1.0.24
Provides:       crate(syn) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/clone-impls)
Provides:       crate(%{pkgname}/derive)
Provides:       crate(%{pkgname}/extra-traits)
Provides:       crate(%{pkgname}/fold)
Provides:       crate(%{pkgname}/full)
Provides:       crate(%{pkgname}/parsing)
Provides:       crate(%{pkgname}/test)
Provides:       crate(%{pkgname}/visit)
Provides:       crate(%{pkgname}/visit-mut)

%description
Source code for takopackized Rust crate "syn"

%package     -n %{name}+default
Summary:        Parser for Rust source code - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/clone-impls)
Requires:       crate(%{pkgname}/derive)
Requires:       crate(%{pkgname}/parsing)
Requires:       crate(%{pkgname}/printing)
Requires:       crate(%{pkgname}/proc-macro)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust syn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proc-macro
Summary:        Parser for Rust source code - feature "proc-macro"
Requires:       crate(%{pkgname})
Requires:       crate(proc-macro2-1.0/proc-macro) >= 1.0.106
Requires:       crate(quote-1.0/proc-macro) >= 1.0.45
Provides:       crate(%{pkgname}/proc-macro)

%description -n %{name}+proc-macro
This metapackage enables feature "proc-macro" for the Rust syn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quote
Summary:        Parser for Rust source code - feature "quote" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(quote-1.0) >= 1.0.45
Provides:       crate(%{pkgname}/printing)
Provides:       crate(%{pkgname}/quote)

%description -n %{name}+quote
This metapackage enables feature "quote" for the Rust syn crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "printing" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
