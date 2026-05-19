# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name countme
%global full_version 3.0.1
%global pkgname countme-3.0

Name:           rust-countme-3.0
Version:        3.0.1
Release:        %autorelease
Summary:        Rust crate "countme"
License:        MIT OR Apache-2.0
URL:            https://github.com/matklad/countme
#!RemoteAsset:  sha256:7704b5fdd17b18ae31c4c1da5a2e0305a2bf17b5249300a9ee9ed7b72114c636
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "countme"

%package     -n %{name}+dashmap
Summary:        Counts the number of live instances of types - feature "dashmap"
Requires:       crate(%{pkgname})
Requires:       crate(dashmap-5.0/default) >= 5.0.0
Provides:       crate(%{pkgname}/dashmap)

%description -n %{name}+dashmap
This metapackage enables feature "dashmap" for the Rust countme crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+enable
Summary:        Counts the number of live instances of types - feature "enable" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/dashmap)
Requires:       crate(%{pkgname}/once-cell)
Requires:       crate(%{pkgname}/rustc-hash)
Provides:       crate(%{pkgname}/enable)
Provides:       crate(%{pkgname}/print-at-exit)

%description -n %{name}+enable
This metapackage enables feature "enable" for the Rust countme crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "print_at_exit" feature.

%package     -n %{name}+once-cell
Summary:        Counts the number of live instances of types - feature "once_cell"
Requires:       crate(%{pkgname})
Requires:       crate(once-cell-1.0/default) >= 1.5
Provides:       crate(%{pkgname}/once-cell)

%description -n %{name}+once-cell
This metapackage enables feature "once_cell" for the Rust countme crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-hash
Summary:        Counts the number of live instances of types - feature "rustc-hash"
Requires:       crate(%{pkgname})
Requires:       crate(rustc-hash-1.0/default) >= 1.1
Provides:       crate(%{pkgname}/rustc-hash)

%description -n %{name}+rustc-hash
This metapackage enables feature "rustc-hash" for the Rust countme crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
