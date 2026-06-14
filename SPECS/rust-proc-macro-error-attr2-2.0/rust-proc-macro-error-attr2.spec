# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name proc-macro-error-attr2
%global full_version 2.0.0
%global pkgname proc-macro-error-attr2-2.0

Name:           rust-proc-macro-error-attr2-2.0
Version:        2.0.0
Release:        %autorelease
Summary:        Rust crate "proc-macro-error-attr2"
License:        MIT OR Apache-2.0
URL:            https://github.com/GnomedDev/proc-macro-error-2
#!RemoteAsset:  sha256:96de42df36bb9bba5542fe9f1a054b8cc87e172759a1868aa05c1f3acc89dfc5
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1.0/default) >= 1.0.106
Requires:       crate(quote-1.0/default) >= 1.0.45
Provides:       crate(proc-macro-error-attr2) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "proc-macro-error-attr2"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
