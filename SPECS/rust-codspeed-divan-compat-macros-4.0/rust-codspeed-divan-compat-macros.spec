# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name codspeed-divan-compat-macros
%global full_version 4.4.1
%global pkgname codspeed-divan-compat-macros-4.0

Name:           rust-codspeed-divan-compat-macros-4.0
Version:        4.4.1
Release:        %autorelease
Summary:        Rust crate "codspeed-divan-compat-macros"
License:        MIT OR Apache-2.0
URL:            https://codspeed.io
#!RemoteAsset:  sha256:78aae02f2a278588e16e8ca62ea1915b8ab30f8230a09926671bba19ede801a4
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(divan-macros-0.1/default) >= 0.1.17
Requires:       crate(itertools-0.14/default) >= 0.14.0
Requires:       crate(proc-macro-crate-3.0/default) >= 3.4.0
Requires:       crate(proc-macro2-1.0/default) >= 1.0.106
Requires:       crate(quote-1.0) >= 1.0.45
Requires:       crate(syn-2.0/clone-impls) >= 2.0.117
Requires:       crate(syn-2.0/extra-traits) >= 2.0.117
Requires:       crate(syn-2.0/full) >= 2.0.117
Requires:       crate(syn-2.0/parsing) >= 2.0.117
Requires:       crate(syn-2.0/printing) >= 2.0.117
Requires:       crate(syn-2.0/proc-macro) >= 2.0.117
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "codspeed-divan-compat-macros"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
