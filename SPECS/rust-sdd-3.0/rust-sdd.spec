# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sdd
%global full_version 3.0.10
%global pkgname sdd-3.0

Name:           rust-sdd-3.0
Version:        3.0.10
Release:        %autorelease
Summary:        Rust crate "sdd"
License:        Apache-2.0
URL:            https://github.com/wvwwvwwv/scalable-delayed-dealloc/
#!RemoteAsset:  sha256:490dcfcbfef26be6800d11870ff2df8774fa6e86d047e3e8c8a76b25655e41ca
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(sdd) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "sdd"

%package     -n %{name}+loom
Summary:        Scalable lock-free delayed memory reclaimer - feature "loom"
Requires:       crate(%{pkgname})
Requires:       crate(loom-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/loom)

%description -n %{name}+loom
This metapackage enables feature "loom" for the Rust sdd crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
