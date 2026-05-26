# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gif
%global full_version 0.14.2
%global pkgname gif-0.14

Name:           rust-gif-0.14
Version:        0.14.2
Release:        %autorelease
Summary:        Rust crate "gif"
License:        MIT OR Apache-2.0
URL:            https://github.com/image-rs/image-gif
#!RemoteAsset:  sha256:ee8cfcc411d9adbbaba82fb72661cc1bcca13e8bba98b364e62b2dba8f960159
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(weezl-0.1/default) >= 0.1.12
Provides:       crate(gif) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/raii-no-panic)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "gif"

%package     -n %{name}+color-quant
Summary:        GIF de- and encoder - feature "color_quant"
Requires:       crate(%{pkgname})
Requires:       crate(color-quant-1.0/default) >= 1.1.0
Provides:       crate(%{pkgname}/color-quant)

%description -n %{name}+color-quant
This metapackage enables feature "color_quant" for the Rust gif crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        GIF de- and encoder - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/color-quant)
Requires:       crate(%{pkgname}/raii-no-panic)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust gif crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
