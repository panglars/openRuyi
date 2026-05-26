# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name vergen
%global full_version 9.1.0
%global pkgname vergen-9.0

Name:           rust-vergen-9.0
Version:        9.1.0
Release:        %autorelease
Summary:        Rust crate "vergen"
License:        MIT OR Apache-2.0
URL:            https://github.com/rustyhorde/vergen
#!RemoteAsset:  sha256:b849a1f6d8639e8de261e81ee0fc881e3e3620db1af9f2e0da015d4382ceaf75
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1.0/default) >= 1.0.102
Requires:       crate(derive-builder-0.20/default) >= 0.20.2
Requires:       crate(rustversion-1.0/default) >= 1.0.22
Requires:       crate(vergen-lib-9.0/default) >= 9.1.0
Provides:       crate(vergen) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "vergen"

%package     -n %{name}+build
Summary:        Generate 'cargo:rustc-env' instructions via 'build.rs' for use in your code via the 'env!' macro - feature "build"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/time)
Requires:       crate(vergen-lib-9.0/build) >= 9.1.0
Provides:       crate(%{pkgname}/build)

%description -n %{name}+build
This metapackage enables feature "build" for the Rust vergen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cargo
Summary:        Generate 'cargo:rustc-env' instructions via 'build.rs' for use in your code via the 'env!' macro - feature "cargo"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/cargo-metadata)
Requires:       crate(%{pkgname}/regex)
Requires:       crate(vergen-lib-9.0/cargo) >= 9.1.0
Provides:       crate(%{pkgname}/cargo)

%description -n %{name}+cargo
This metapackage enables feature "cargo" for the Rust vergen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cargo-metadata
Summary:        Generate 'cargo:rustc-env' instructions via 'build.rs' for use in your code via the 'env!' macro - feature "cargo_metadata"
Requires:       crate(%{pkgname})
Requires:       crate(cargo-metadata-0.23/default) >= 0.23.1
Provides:       crate(%{pkgname}/cargo-metadata)

%description -n %{name}+cargo-metadata
This metapackage enables feature "cargo_metadata" for the Rust vergen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+emit-and-set
Summary:        Generate 'cargo:rustc-env' instructions via 'build.rs' for use in your code via the 'env!' macro - feature "emit_and_set"
Requires:       crate(%{pkgname})
Requires:       crate(vergen-lib-9.0/emit-and-set) >= 9.1.0
Provides:       crate(%{pkgname}/emit-and-set)

%description -n %{name}+emit-and-set
This metapackage enables feature "emit_and_set" for the Rust vergen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+regex
Summary:        Generate 'cargo:rustc-env' instructions via 'build.rs' for use in your code via the 'env!' macro - feature "regex"
Requires:       crate(%{pkgname})
Requires:       crate(regex-1.0/default) >= 1.12.2
Provides:       crate(%{pkgname}/regex)

%description -n %{name}+regex
This metapackage enables feature "regex" for the Rust vergen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc
Summary:        Generate 'cargo:rustc-env' instructions via 'build.rs' for use in your code via the 'env!' macro - feature "rustc"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/rustc-version)
Requires:       crate(vergen-lib-9.0/rustc) >= 9.1.0
Provides:       crate(%{pkgname}/rustc)

%description -n %{name}+rustc
This metapackage enables feature "rustc" for the Rust vergen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc-version
Summary:        Generate 'cargo:rustc-env' instructions via 'build.rs' for use in your code via the 'env!' macro - feature "rustc_version"
Requires:       crate(%{pkgname})
Requires:       crate(rustc-version-0.4/default) >= 0.4.1
Provides:       crate(%{pkgname}/rustc-version)

%description -n %{name}+rustc-version
This metapackage enables feature "rustc_version" for the Rust vergen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+si
Summary:        Generate 'cargo:rustc-env' instructions via 'build.rs' for use in your code via the 'env!' macro - feature "si"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/sysinfo)
Requires:       crate(vergen-lib-9.0/si) >= 9.1.0
Provides:       crate(%{pkgname}/si)

%description -n %{name}+si
This metapackage enables feature "si" for the Rust vergen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sysinfo
Summary:        Generate 'cargo:rustc-env' instructions via 'build.rs' for use in your code via the 'env!' macro - feature "sysinfo"
Requires:       crate(%{pkgname})
Requires:       crate(sysinfo-0.37/default) >= 0.37.2
Provides:       crate(%{pkgname}/sysinfo)

%description -n %{name}+sysinfo
This metapackage enables feature "sysinfo" for the Rust vergen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+time
Summary:        Generate 'cargo:rustc-env' instructions via 'build.rs' for use in your code via the 'env!' macro - feature "time"
Requires:       crate(%{pkgname})
Requires:       crate(time-0.3/default) >= 0.3.47
Requires:       crate(time-0.3/formatting) >= 0.3.47
Requires:       crate(time-0.3/local-offset) >= 0.3.47
Requires:       crate(time-0.3/parsing) >= 0.3.47
Provides:       crate(%{pkgname}/time)

%description -n %{name}+time
This metapackage enables feature "time" for the Rust vergen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable
Summary:        Generate 'cargo:rustc-env' instructions via 'build.rs' for use in your code via the 'env!' macro - feature "unstable"
Requires:       crate(%{pkgname})
Requires:       crate(vergen-lib-9.0/unstable) >= 9.1.0
Provides:       crate(%{pkgname}/unstable)

%description -n %{name}+unstable
This metapackage enables feature "unstable" for the Rust vergen crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
