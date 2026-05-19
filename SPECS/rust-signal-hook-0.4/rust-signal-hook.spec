# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name signal-hook
%global full_version 0.4.4
%global pkgname signal-hook-0.4

Name:           rust-signal-hook-0.4
Version:        0.4.4
Release:        %autorelease
Summary:        Rust crate "signal-hook"
License:        MIT OR Apache-2.0
URL:            https://github.com/vorner/signal-hook
#!RemoteAsset:  sha256:b2a0c28ca5908dbdbcd52e6fdaa00358ab88637f8ab33e1f188dd510eb44b53d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.186
Requires:       crate(signal-hook-registry-1.0/default) >= 1.4.8
Provides:       crate(signal-hook) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/channel)
Provides:       crate(%{pkgname}/iterator)

%description
Source code for takopackized Rust crate "signal-hook"

%package     -n %{name}+cc
Summary:        Unix signal handling - feature "cc" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(cc-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/cc)
Provides:       crate(%{pkgname}/extended-siginfo-raw)

%description -n %{name}+cc
This metapackage enables feature "cc" for the Rust signal-hook crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "extended-siginfo-raw" feature.

%package     -n %{name}+default
Summary:        Unix signal handling - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/channel)
Requires:       crate(%{pkgname}/iterator)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust signal-hook crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+extended-siginfo
Summary:        Unix signal handling - feature "extended-siginfo"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/channel)
Requires:       crate(%{pkgname}/extended-siginfo-raw)
Requires:       crate(%{pkgname}/iterator)
Provides:       crate(%{pkgname}/extended-siginfo)

%description -n %{name}+extended-siginfo
This metapackage enables feature "extended-siginfo" for the Rust signal-hook crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
