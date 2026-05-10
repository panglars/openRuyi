# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unix_path
%global full_version 1.0.1
%global pkgname unix-path-1.0

Name:           rust-unix-path-1.0
Version:        1.0.1
Release:        %autorelease
Summary:        Rust crate "unix_path"
License:        MIT OR Apache-2.0
URL:            https://gitlab.com/SnejUgal/unix_path
#!RemoteAsset:  sha256:af8e291873ae77c4c8d9c9b34d0bee68a35b048fb39c263a5155e0e353783eaf
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(unix-str-1.0) >= 1.0.0
Provides:       crate(unix-path) = %{version}
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "unix_path"

%package     -n %{name}+alloc
Summary:        Unix-compatible paths regardless of platform - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(unix-str-1.0/alloc) >= 1.0.0
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust unix_path crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Unix-compatible paths regardless of platform - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust unix_path crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+shrink-to
Summary:        Unix-compatible paths regardless of platform - feature "shrink_to"
Requires:       crate(%{pkgname})
Requires:       crate(unix-str-1.0/shrink-to) >= 1.0.0
Provides:       crate(%{pkgname}/shrink-to)

%description -n %{name}+shrink-to
This metapackage enables feature "shrink_to" for the Rust unix_path crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Unix-compatible paths regardless of platform - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(unix-str-1.0/std) >= 1.0.0
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust unix_path crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
