# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ratatui-termion
%global full_version 0.1.0
%global pkgname ratatui-termion-0.1

Name:           rust-ratatui-termion-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "ratatui-termion"
License:        MIT
URL:            https://ratatui.rs
#!RemoteAsset:  sha256:4cade85a8591fbc911e147951422f0d6fd40f4948b271b6216c7dc01838996f8
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(instability-0.3/default) >= 0.3.12
Requires:       crate(ratatui-core-0.1/default) >= 0.1.0
Requires:       crate(termion-4.0/default) >= 4.0.6
Provides:       crate(ratatui-termion) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/unstable)
Provides:       crate(%{pkgname}/unstable-backend-writer)

%description
Source code for takopackized Rust crate "ratatui-termion"

%package     -n %{name}+document-features
Summary:        Termion backend for the Ratatui Terminal UI library - feature "document-features"
Requires:       crate(%{pkgname})
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features)

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust ratatui-termion crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+scrolling-regions
Summary:        Termion backend for the Ratatui Terminal UI library - feature "scrolling-regions"
Requires:       crate(%{pkgname})
Requires:       crate(ratatui-core-0.1/scrolling-regions) >= 0.1.0
Provides:       crate(%{pkgname}/scrolling-regions)

%description -n %{name}+scrolling-regions
This metapackage enables feature "scrolling-regions" for the Rust ratatui-termion crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Termion backend for the Ratatui Terminal UI library - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(termion-4.0/serde) >= 4.0.6
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust ratatui-termion crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
