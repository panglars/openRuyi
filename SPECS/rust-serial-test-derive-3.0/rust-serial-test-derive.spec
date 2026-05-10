# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serial_test_derive
%global full_version 3.3.1
%global pkgname serial-test-derive-3.0

Name:           rust-serial-test-derive-3.0
Version:        3.3.1
Release:        %autorelease
Summary:        Rust crate "serial_test_derive"
License:        MIT
URL:            https://github.com/palfrey/serial_test/
#!RemoteAsset:  sha256:6f50427f258fb77356e4cd4aa0e87e2bd2c66dbcee41dc405282cae2bfc26c83
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1.0/proc-macro) >= 1.0.60
Requires:       crate(quote-1.0) >= 1.0.0
Requires:       crate(syn-2.0/clone-impls) >= 2.0.0
Requires:       crate(syn-2.0/full) >= 2.0.0
Requires:       crate(syn-2.0/parsing) >= 2.0.0
Requires:       crate(syn-2.0/printing) >= 2.0.0
Provides:       crate(serial-test-derive) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/async)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/file-locks)
Provides:       crate(%{pkgname}/test-logging)

%description
Source code for takopackized Rust crate "serial_test_derive"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
