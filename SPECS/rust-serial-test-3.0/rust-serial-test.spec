# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serial_test
%global full_version 3.3.1
%global pkgname serial-test-3.0

Name:           rust-serial-test-3.0
Version:        3.3.1
Release:        %autorelease
Summary:        Rust crate "serial_test"
License:        MIT
URL:            https://github.com/palfrey/serial_test/
#!RemoteAsset:  sha256:0d0b343e184fc3b7bb44dff0705fffcf4b3756ba6aff420dddd8b24ca145e555
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(once-cell-1.0/std) >= 1.19
Requires:       crate(parking-lot-0.12) >= 0.12.0
Requires:       crate(scc-2.0) >= 2.0.0
Requires:       crate(serial-test-derive-3.0/default) >= 3.3.1
Provides:       crate(serial-test) = %{version}
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "serial_test"

%package     -n %{name}+async
Summary:        Allows for the creation of serialised Rust tests - feature "async"
Requires:       crate(%{pkgname})
Requires:       crate(futures-executor-0.3/std) >= 0.3.0
Requires:       crate(futures-util-0.3/std) >= 0.3.0
Requires:       crate(serial-test-derive-3.0/async) >= 3.3.1
Provides:       crate(%{pkgname}/async)

%description -n %{name}+async
This metapackage enables feature "async" for the Rust serial_test crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Allows for the creation of serialised Rust tests - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/async)
Requires:       crate(%{pkgname}/logging)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust serial_test crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+docsrs
Summary:        Allows for the creation of serialised Rust tests - feature "docsrs"
Requires:       crate(%{pkgname})
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/docsrs)

%description -n %{name}+docsrs
This metapackage enables feature "docsrs" for the Rust serial_test crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+file-locks
Summary:        Allows for the creation of serialised Rust tests - feature "file_locks"
Requires:       crate(%{pkgname})
Requires:       crate(fslock-0.2/std) >= 0.2.0
Provides:       crate(%{pkgname}/file-locks)

%description -n %{name}+file-locks
This metapackage enables feature "file_locks" for the Rust serial_test crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+logging
Summary:        Allows for the creation of serialised Rust tests - feature "logging"
Requires:       crate(%{pkgname})
Requires:       crate(log-0.4/default) >= 0.4.4
Provides:       crate(%{pkgname}/logging)

%description -n %{name}+logging
This metapackage enables feature "logging" for the Rust serial_test crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+test-logging
Summary:        Allows for the creation of serialised Rust tests - feature "test_logging"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/logging)
Requires:       crate(env-logger-0.6) >= 0.6.1
Requires:       crate(serial-test-derive-3.0/test-logging) >= 3.3.1
Provides:       crate(%{pkgname}/test-logging)

%description -n %{name}+test-logging
This metapackage enables feature "test_logging" for the Rust serial_test crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
