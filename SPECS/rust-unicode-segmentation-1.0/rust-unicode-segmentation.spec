# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name unicode-segmentation
%global full_version 1.12.0
%global pkgname unicode-segmentation-1.0

Name:           rust-unicode-segmentation-1.0
Version:        1.12.0
Release:        %autorelease
Summary:        Rust crate "unicode-segmentation"
License:        MIT OR Apache-2.0
URL:            https://github.com/unicode-rs/unicode-segmentation
#!RemoteAsset:  sha256:f6ccf251212114b54433ec949fd6a7841275f9ada20dddd2f29e9ceea4501493
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(unicode-segmentation) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/no-std)

%description
Source code for takopackized Rust crate "unicode-segmentation"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
