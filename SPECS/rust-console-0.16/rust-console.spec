# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name console
%global full_version 0.16.1
%global pkgname console-0.16

Name:           rust-console-0.16
Version:        0.16.1
Release:        %autorelease
Summary:        Rust crate "console"
License:        MIT
URL:            https://github.com/console-rs/console
#!RemoteAsset:  sha256:b430743a6eb14e9764d4260d4c0d8123087d504eeb9c48f2b2a5e810dd369df4
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(encode-unicode-1.0/default) >= 1.0.0
Requires:       crate(windows-sys-0.61/default) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-storage-filesystem) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-system-console) >= 0.61.0
Requires:       crate(windows-sys-0.61/win32-ui-input-keyboardandmouse) >= 0.61.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/ansi-parsing)
Provides:       crate(%{pkgname}/windows-console-colors)

%description
Source code for takopackized Rust crate "console"

%package     -n %{name}+default
Summary:        Terminal and console abstraction for Rust - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/ansi-parsing)
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/unicode-width)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust console crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Terminal and console abstraction for Rust - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(libc-0.2/default) >= 0.2.186
Requires:       crate(once-cell-1.0/default) >= 1.21.3
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust console crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-width
Summary:        Terminal and console abstraction for Rust - feature "unicode-width"
Requires:       crate(%{pkgname})
Requires:       crate(unicode-width-0.2/default) >= 0.2.2
Provides:       crate(%{pkgname}/unicode-width)

%description -n %{name}+unicode-width
This metapackage enables feature "unicode-width" for the Rust console crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
