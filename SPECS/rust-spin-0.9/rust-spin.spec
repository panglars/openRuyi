# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name spin
%global full_version 0.9.8
%global pkgname spin-0.9

Name:           rust-spin-0.9
Version:        0.9.8
Release:        %autorelease
Summary:        Rust crate "spin"
License:        MIT
URL:            https://github.com/mvdnes/spin-rs.git
#!RemoteAsset:  sha256:6980e8d7511241f8acf4aebddbb1ff938df5eebe98691418c4468d0b72a96a67
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(spin) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/barrier)
Provides:       crate(%{pkgname}/fair-mutex)
Provides:       crate(%{pkgname}/lazy)
Provides:       crate(%{pkgname}/mutex)
Provides:       crate(%{pkgname}/once)
Provides:       crate(%{pkgname}/rwlock)
Provides:       crate(%{pkgname}/spin-mutex)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/ticket-mutex)

%description
Source code for takopackized Rust crate "spin"

%package     -n %{name}+default
Summary:        Spin-based synchronization primitives - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/barrier)
Requires:       crate(%{pkgname}/lazy)
Requires:       crate(%{pkgname}/lock-api)
Requires:       crate(%{pkgname}/mutex)
Requires:       crate(%{pkgname}/once)
Requires:       crate(%{pkgname}/rwlock)
Requires:       crate(%{pkgname}/spin-mutex)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust spin crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lock-api-crate
Summary:        Spin-based synchronization primitives - feature "lock_api_crate" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(lock-api-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/lock-api)
Provides:       crate(%{pkgname}/lock-api-crate)

%description -n %{name}+lock-api-crate
This metapackage enables feature "lock_api_crate" for the Rust spin crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "lock_api" feature.

%package     -n %{name}+portable-atomic
Summary:        Spin-based synchronization primitives - feature "portable_atomic"
Requires:       crate(%{pkgname})
Requires:       crate(portable-atomic-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/portable-atomic)

%description -n %{name}+portable-atomic
This metapackage enables feature "portable_atomic" for the Rust spin crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+use-ticket-mutex
Summary:        Spin-based synchronization primitives - feature "use_ticket_mutex"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/mutex)
Requires:       crate(%{pkgname}/ticket-mutex)
Provides:       crate(%{pkgname}/use-ticket-mutex)

%description -n %{name}+use-ticket-mutex
This metapackage enables feature "use_ticket_mutex" for the Rust spin crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
