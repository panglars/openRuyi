# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name codspeed-divan-compat-walltime
%global full_version 4.4.1
%global pkgname codspeed-divan-compat-walltime-4.0

Name:           rust-codspeed-divan-compat-walltime-4.0
Version:        4.4.1
Release:        %autorelease
Summary:        Rust crate "codspeed-divan-compat-walltime"
License:        MIT OR Apache-2.0
URL:            https://codspeed.io
#!RemoteAsset:  sha256:59ffd32c0c59ab8b674b15be65ba7c59aebac047036cfa7fa1e11bc2c178b81f
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1.0/default) >= 1.0.3
Requires:       crate(clap-4.0/env) >= 4.6.1
Requires:       crate(clap-4.0/std) >= 4.6.1
Requires:       crate(codspeed-4.0/default) >= 4.4.1
Requires:       crate(condtype-1.0/default) >= 1.3.0
Requires:       crate(divan-macros-0.1/default) >= 0.1.17
Requires:       crate(libc-0.2/default) >= 0.2.186
Requires:       crate(regex-lite-0.1/std) >= 0.1.7
Requires:       crate(regex-lite-0.1/string) >= 0.1.7
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/dyn-thread-local)
Provides:       crate(%{pkgname}/internal-benches)

%description
Source code for takopackized Rust crate "codspeed-divan-compat-walltime"

%package     -n %{name}+help
Summary:        Temporary compatibility layer for CodSpeed to use Divan's walltime entrypoint - feature "help"
Requires:       crate(%{pkgname})
Requires:       crate(clap-4.0/env) >= 4.6.1
Requires:       crate(clap-4.0/help) >= 4.6.1
Requires:       crate(clap-4.0/std) >= 4.6.1
Provides:       crate(%{pkgname}/help)

%description -n %{name}+help
This metapackage enables feature "help" for the Rust codspeed-divan-compat-walltime crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wrap-help
Summary:        Temporary compatibility layer for CodSpeed to use Divan's walltime entrypoint - feature "wrap_help" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/help)
Requires:       crate(clap-4.0/env) >= 4.6.1
Requires:       crate(clap-4.0/std) >= 4.6.1
Requires:       crate(clap-4.0/wrap-help) >= 4.6.1
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/wrap-help)

%description -n %{name}+wrap-help
This metapackage enables feature "wrap_help" for the Rust codspeed-divan-compat-walltime crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
