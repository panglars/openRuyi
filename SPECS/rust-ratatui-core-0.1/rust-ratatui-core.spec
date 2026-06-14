# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ratatui-core
%global full_version 0.1.0
%global pkgname ratatui-core-0.1

Name:           rust-ratatui-core-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "ratatui-core"
License:        MIT
URL:            https://ratatui.rs
#!RemoteAsset:  sha256:5ef8dea09a92caaf73bff7adb70b76162e5937524058a7e5bff37869cbbec293
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2.0/default) >= 2.11.1
Requires:       crate(compact-str-0.9) >= 0.9.0
Requires:       crate(hashbrown-0.16/default) >= 0.16.1
Requires:       crate(indoc-2.0/default) >= 2.0.7
Requires:       crate(itertools-0.14/use-alloc) >= 0.14.0
Requires:       crate(kasuari-0.4) >= 0.4.12
Requires:       crate(lru-0.16/default) >= 0.16.4
Requires:       crate(strum-0.27/derive) >= 0.27.2
Requires:       crate(thiserror-2.0) >= 2.0.18
Requires:       crate(unicode-segmentation-1.0/default) >= 1.13.2
Requires:       crate(unicode-truncate-2.0) >= 2.0.1
Requires:       crate(unicode-width-0.2/default) >= 0.2.2
Provides:       crate(ratatui-core) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/scrolling-regions)
Provides:       crate(%{pkgname}/underline-color)

%description
Widget libraries should use this crate. Applications should use the main Ratatui crate.
Source code for takopackized Rust crate "ratatui-core"

%package     -n %{name}+anstyle
Summary:        Core types and traits for the Ratatui Terminal UI library - feature "anstyle"
Requires:       crate(%{pkgname})
Requires:       crate(anstyle-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/anstyle)

%description -n %{name}+anstyle
Widget libraries should use this crate. Applications should use the main Ratatui crate.
This metapackage enables feature "anstyle" for the Rust ratatui-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+document-features
Summary:        Core types and traits for the Ratatui Terminal UI library - feature "document-features"
Requires:       crate(%{pkgname})
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features)

%description -n %{name}+document-features
Widget libraries should use this crate. Applications should use the main Ratatui crate.
This metapackage enables feature "document-features" for the Rust ratatui-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+palette
Summary:        Core types and traits for the Ratatui Terminal UI library - feature "palette"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(palette-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/palette)

%description -n %{name}+palette
Widget libraries should use this crate. Applications should use the main Ratatui crate.
This metapackage enables feature "palette" for the Rust ratatui-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+portable-atomic
Summary:        Core types and traits for the Ratatui Terminal UI library - feature "portable-atomic"
Requires:       crate(%{pkgname})
Requires:       crate(kasuari-0.4/portable-atomic) >= 0.4.12
Provides:       crate(%{pkgname}/portable-atomic)

%description -n %{name}+portable-atomic
Widget libraries should use this crate. Applications should use the main Ratatui crate.
This metapackage enables feature "portable-atomic" for the Rust ratatui-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Core types and traits for the Ratatui Terminal UI library - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(bitflags-2.0/serde) >= 2.11.1
Requires:       crate(compact-str-0.9/serde) >= 0.9.0
Requires:       crate(serde-1.0/default) >= 1.0.228
Requires:       crate(serde-1.0/derive) >= 1.0.228
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
Widget libraries should use this crate. Applications should use the main Ratatui crate.
This metapackage enables feature "serde" for the Rust ratatui-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Core types and traits for the Ratatui Terminal UI library - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(compact-str-0.9/std) >= 0.9.0
Requires:       crate(itertools-0.14/use-alloc) >= 0.14.0
Requires:       crate(itertools-0.14/use-std) >= 0.14.0
Requires:       crate(kasuari-0.4/std) >= 0.4.12
Requires:       crate(strum-0.27/derive) >= 0.27.2
Requires:       crate(strum-0.27/std) >= 0.27.2
Requires:       crate(thiserror-2.0/std) >= 2.0.18
Requires:       crate(unicode-truncate-2.0/std) >= 2.0.1
Provides:       crate(%{pkgname}/layout-cache)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
Widget libraries should use this crate. Applications should use the main Ratatui crate.
This metapackage enables feature "std" for the Rust ratatui-core crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "layout-cache" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
