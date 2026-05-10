# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rust-embed-impl
%global full_version 8.11.0
%global pkgname rust-embed-impl-8.0

Name:           rust-rust-embed-impl-8.0
Version:        8.11.0
Release:        %autorelease
Summary:        Rust crate "rust-embed-impl"
License:        MIT
URL:            https://pyrossh.dev/repos/rust-embed
#!RemoteAsset:  sha256:da0902e4c7c8e997159ab384e6d0fc91c221375f6894346ae107f47dd0f3ccaa
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1.0/default) >= 1.0.0
Requires:       crate(quote-1.0/default) >= 1.0.0
Requires:       crate(rust-embed-utils-8.0/default) >= 8.11.0
Requires:       crate(syn-2.0/derive) >= 2.0.0
Requires:       crate(syn-2.0/parsing) >= 2.0.0
Requires:       crate(syn-2.0/printing) >= 2.0.0
Requires:       crate(syn-2.0/proc-macro) >= 2.0.0
Requires:       crate(walkdir-2.0/default) >= 2.3.1
Provides:       crate(rust-embed-impl) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/compression)
Provides:       crate(%{pkgname}/debug-embed)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/deterministic-timestamps)

%description
Source code for takopackized Rust crate "rust-embed-impl"

%package     -n %{name}+include-exclude
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "include-exclude"
Requires:       crate(%{pkgname})
Requires:       crate(rust-embed-utils-8.0/include-exclude) >= 8.11.0
Provides:       crate(%{pkgname}/include-exclude)

%description -n %{name}+include-exclude
This metapackage enables feature "include-exclude" for the Rust rust-embed-impl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mime-guess
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "mime-guess"
Requires:       crate(%{pkgname})
Requires:       crate(rust-embed-utils-8.0/mime-guess) >= 8.11.0
Provides:       crate(%{pkgname}/mime-guess)

%description -n %{name}+mime-guess
This metapackage enables feature "mime-guess" for the Rust rust-embed-impl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+shellexpand
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "shellexpand" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(shellexpand-3.0/default) >= 3.0.0
Provides:       crate(%{pkgname}/interpolate-folder-path)
Provides:       crate(%{pkgname}/shellexpand)

%description -n %{name}+shellexpand
This metapackage enables feature "shellexpand" for the Rust rust-embed-impl crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "interpolate-folder-path" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
