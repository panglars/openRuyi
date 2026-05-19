# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ratatui-widgets
%global full_version 0.3.0
%global pkgname ratatui-widgets-0.3

Name:           rust-ratatui-widgets-0.3
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "ratatui-widgets"
License:        MIT
URL:            https://ratatui.rs
#!RemoteAsset:  sha256:d7dbfa023cd4e604c2553483820c5fe8aa9d71a42eea5aa77c6e7f35756612db
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2.0/default) >= 2.11.1
Requires:       crate(hashbrown-0.16/default) >= 0.16.1
Requires:       crate(indoc-2.0/default) >= 2.0.7
Requires:       crate(instability-0.3/default) >= 0.3.12
Requires:       crate(itertools-0.14/use-alloc) >= 0.14.0
Requires:       crate(line-clipping-0.3/default) >= 0.3.7
Requires:       crate(ratatui-core-0.1/default) >= 0.1.0
Requires:       crate(strum-0.27/derive) >= 0.27.2
Requires:       crate(unicode-segmentation-1.0/default) >= 1.13.2
Requires:       crate(unicode-width-0.2/default) >= 0.2.2
Provides:       crate(ratatui-widgets) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/unstable)
Provides:       crate(%{pkgname}/unstable-rendered-line-info)

%description
Source code for takopackized Rust crate "ratatui-widgets"

%package     -n %{name}+calendar
Summary:        Collection of Ratatui widgets for building terminal user interfaces using Ratatui - feature "calendar" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(time-0.3) >= 0.3.47
Provides:       crate(%{pkgname}/all-widgets)
Provides:       crate(%{pkgname}/calendar)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+calendar
This metapackage enables feature "calendar" for the Rust ratatui-widgets crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "all-widgets", and "default" features.

%package     -n %{name}+document-features
Summary:        Collection of Ratatui widgets for building terminal user interfaces using Ratatui - feature "document-features"
Requires:       crate(%{pkgname})
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features)

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust ratatui-widgets crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Collection of Ratatui widgets for building terminal user interfaces using Ratatui - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(ratatui-core-0.1/serde) >= 0.1.0
Requires:       crate(serde-1.0/default) >= 1.0.228
Requires:       crate(serde-1.0/derive) >= 1.0.228
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust ratatui-widgets crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Collection of Ratatui widgets for building terminal user interfaces using Ratatui - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(time-0.3/local-offset) >= 0.3.47
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust ratatui-widgets crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
