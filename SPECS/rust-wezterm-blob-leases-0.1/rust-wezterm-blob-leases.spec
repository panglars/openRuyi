# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wezterm-blob-leases
%global full_version 0.1.1
%global pkgname wezterm-blob-leases-0.1

Name:           rust-wezterm-blob-leases-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "wezterm-blob-leases"
License:        MIT
URL:            https://github.com/wezterm/wezterm
#!RemoteAsset:  sha256:692daff6d93d94e29e4114544ef6d5c942a7ed998b37abdc19b17136ea428eb7
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(getrandom-0.3/default) >= 0.3.4
Requires:       crate(mac-address-1.0/default) >= 1.1.8
Requires:       crate(sha2-0.10/default) >= 0.10.9
Requires:       crate(thiserror-1.0/default) >= 1.0.69
Requires:       crate(uuid-1.0/default) >= 1.23.1
Requires:       crate(uuid-1.0/rng) >= 1.23.1
Requires:       crate(uuid-1.0/v1) >= 1.23.1
Provides:       crate(wezterm-blob-leases) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "wezterm-blob-leases"

%package     -n %{name}+serde
Summary:        Manage image blob caching/leasing for wezterm - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.228
Requires:       crate(serde-1.0/derive) >= 1.0.228
Requires:       crate(uuid-1.0/rng) >= 1.23.1
Requires:       crate(uuid-1.0/serde) >= 1.23.1
Requires:       crate(uuid-1.0/v1) >= 1.23.1
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust wezterm-blob-leases crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+simple-tempdir
Summary:        Manage image blob caching/leasing for wezterm - feature "simple_tempdir"
Requires:       crate(%{pkgname})
Requires:       crate(tempfile-3.0/default) >= 3.16
Provides:       crate(%{pkgname}/simple-tempdir)

%description -n %{name}+simple-tempdir
This metapackage enables feature "simple_tempdir" for the Rust wezterm-blob-leases crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
