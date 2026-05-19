# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name futures
%global full_version 0.3.32
%global pkgname futures-0.3

Name:           rust-futures-0.3
Version:        0.3.32
Release:        %autorelease
Summary:        Rust crate "futures"
License:        MIT OR Apache-2.0
URL:            https://rust-lang.github.io/futures-rs
#!RemoteAsset:  sha256:8b147ee9d1f6d097cef9ce628cd2ee62288d963e16fb287bd9286455b241382d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(futures-channel-0.3/sink) >= 0.3.32
Requires:       crate(futures-core-0.3) >= 0.3.32
Requires:       crate(futures-io-0.3) >= 0.3.32
Requires:       crate(futures-sink-0.3) >= 0.3.32
Requires:       crate(futures-task-0.3) >= 0.3.32
Requires:       crate(futures-util-0.3/sink) >= 0.3.32
Provides:       crate(futures) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/cfg-target-has-atomic)

%description
Source code for takopackized Rust crate "futures"

%package     -n %{name}+alloc
Summary:        Futures and streams featuring zero allocations, composability, and iterator-like interfaces - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(futures-channel-0.3/alloc) >= 0.3.32
Requires:       crate(futures-channel-0.3/sink) >= 0.3.32
Requires:       crate(futures-core-0.3/alloc) >= 0.3.32
Requires:       crate(futures-sink-0.3/alloc) >= 0.3.32
Requires:       crate(futures-task-0.3/alloc) >= 0.3.32
Requires:       crate(futures-util-0.3/alloc) >= 0.3.32
Requires:       crate(futures-util-0.3/sink) >= 0.3.32
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust futures crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-await
Summary:        Futures and streams featuring zero allocations, composability, and iterator-like interfaces - feature "async-await"
Requires:       crate(%{pkgname})
Requires:       crate(futures-util-0.3/async-await) >= 0.3.32
Requires:       crate(futures-util-0.3/async-await-macro) >= 0.3.32
Requires:       crate(futures-util-0.3/sink) >= 0.3.32
Provides:       crate(%{pkgname}/async-await)

%description -n %{name}+async-await
This metapackage enables feature "async-await" for the Rust futures crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bilock
Summary:        Futures and streams featuring zero allocations, composability, and iterator-like interfaces - feature "bilock"
Requires:       crate(%{pkgname})
Requires:       crate(futures-util-0.3/bilock) >= 0.3.32
Requires:       crate(futures-util-0.3/sink) >= 0.3.32
Provides:       crate(%{pkgname}/bilock)

%description -n %{name}+bilock
This metapackage enables feature "bilock" for the Rust futures crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+compat
Summary:        Futures and streams featuring zero allocations, composability, and iterator-like interfaces - feature "compat"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(futures-util-0.3/compat) >= 0.3.32
Requires:       crate(futures-util-0.3/sink) >= 0.3.32
Provides:       crate(%{pkgname}/compat)

%description -n %{name}+compat
This metapackage enables feature "compat" for the Rust futures crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Futures and streams featuring zero allocations, composability, and iterator-like interfaces - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/async-await)
Requires:       crate(%{pkgname}/executor)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust futures crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+executor
Summary:        Futures and streams featuring zero allocations, composability, and iterator-like interfaces - feature "executor"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(futures-executor-0.3/std) >= 0.3.32
Provides:       crate(%{pkgname}/executor)

%description -n %{name}+executor
This metapackage enables feature "executor" for the Rust futures crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-executor
Summary:        Futures and streams featuring zero allocations, composability, and iterator-like interfaces - feature "futures-executor"
Requires:       crate(%{pkgname})
Requires:       crate(futures-executor-0.3) >= 0.3.32
Provides:       crate(%{pkgname}/futures-executor)

%description -n %{name}+futures-executor
This metapackage enables feature "futures-executor" for the Rust futures crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+io-compat
Summary:        Futures and streams featuring zero allocations, composability, and iterator-like interfaces - feature "io-compat"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/compat)
Requires:       crate(futures-util-0.3/io-compat) >= 0.3.32
Requires:       crate(futures-util-0.3/sink) >= 0.3.32
Provides:       crate(%{pkgname}/io-compat)

%description -n %{name}+io-compat
This metapackage enables feature "io-compat" for the Rust futures crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+spin
Summary:        Futures and streams featuring zero allocations, composability, and iterator-like interfaces - feature "spin"
Requires:       crate(%{pkgname})
Requires:       crate(futures-util-0.3/sink) >= 0.3.32
Requires:       crate(futures-util-0.3/spin) >= 0.3.32
Provides:       crate(%{pkgname}/spin)

%description -n %{name}+spin
This metapackage enables feature "spin" for the Rust futures crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Futures and streams featuring zero allocations, composability, and iterator-like interfaces - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(futures-core-0.3/std) >= 0.3.32
Requires:       crate(futures-io-0.3/std) >= 0.3.32
Requires:       crate(futures-sink-0.3/std) >= 0.3.32
Requires:       crate(futures-task-0.3/std) >= 0.3.32
Requires:       crate(futures-util-0.3/channel) >= 0.3.32
Requires:       crate(futures-util-0.3/io) >= 0.3.32
Requires:       crate(futures-util-0.3/sink) >= 0.3.32
Requires:       crate(futures-util-0.3/std) >= 0.3.32
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust futures crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+thread-pool
Summary:        Futures and streams featuring zero allocations, composability, and iterator-like interfaces - feature "thread-pool"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/executor)
Requires:       crate(futures-executor-0.3/thread-pool) >= 0.3.32
Provides:       crate(%{pkgname}/thread-pool)

%description -n %{name}+thread-pool
This metapackage enables feature "thread-pool" for the Rust futures crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable
Summary:        Futures and streams featuring zero allocations, composability, and iterator-like interfaces - feature "unstable"
Requires:       crate(%{pkgname})
Requires:       crate(futures-channel-0.3/sink) >= 0.3.32
Requires:       crate(futures-channel-0.3/unstable) >= 0.3.32
Requires:       crate(futures-core-0.3/unstable) >= 0.3.32
Requires:       crate(futures-io-0.3/unstable) >= 0.3.32
Requires:       crate(futures-task-0.3/unstable) >= 0.3.32
Requires:       crate(futures-util-0.3/sink) >= 0.3.32
Requires:       crate(futures-util-0.3/unstable) >= 0.3.32
Provides:       crate(%{pkgname}/unstable)

%description -n %{name}+unstable
This metapackage enables feature "unstable" for the Rust futures crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+write-all-vectored
Summary:        Futures and streams featuring zero allocations, composability, and iterator-like interfaces - feature "write-all-vectored"
Requires:       crate(%{pkgname})
Requires:       crate(futures-util-0.3/sink) >= 0.3.32
Requires:       crate(futures-util-0.3/write-all-vectored) >= 0.3.32
Provides:       crate(%{pkgname}/write-all-vectored)

%description -n %{name}+write-all-vectored
This metapackage enables feature "write-all-vectored" for the Rust futures crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
