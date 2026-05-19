# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name signal-hook-mio
%global full_version 0.2.5
%global pkgname signal-hook-mio-0.2

Name:           rust-signal-hook-mio-0.2
Version:        0.2.5
Release:        %autorelease
Summary:        Rust crate "signal-hook-mio"
License:        MIT OR Apache-2.0
URL:            https://github.com/vorner/signal-hook
#!RemoteAsset:  sha256:b75a19a7a740b25bc7944bdee6172368f988763b744e3d4dfe753f6b4ece40cc
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.186
Requires:       crate(signal-hook-0.3/default) >= 0.3.18
Provides:       crate(signal-hook-mio) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "signal-hook-mio"

%package     -n %{name}+mio-0-6
Summary:        MIO support for signal-hook - feature "mio-0_6"
Requires:       crate(%{pkgname})
Requires:       crate(mio-1.0/default) >= 1.2.0
Provides:       crate(%{pkgname}/mio-0-6)

%description -n %{name}+mio-0-6
This metapackage enables feature "mio-0_6" for the Rust signal-hook-mio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mio-0-7
Summary:        MIO support for signal-hook - feature "mio-0_7" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(mio-1.0/default) >= 1.2.0
Requires:       crate(mio-1.0/os-util) >= 1.2.0
Requires:       crate(mio-1.0/uds) >= 1.2.0
Provides:       crate(%{pkgname}/mio-0-7)
Provides:       crate(%{pkgname}/support-v0-7)

%description -n %{name}+mio-0-7
This metapackage enables feature "mio-0_7" for the Rust signal-hook-mio crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "support-v0_7" feature.

%package     -n %{name}+mio-0-8
Summary:        MIO support for signal-hook - feature "mio-0_8" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(mio-1.0/default) >= 1.2.0
Requires:       crate(mio-1.0/net) >= 1.2.0
Requires:       crate(mio-1.0/os-ext) >= 1.2.0
Provides:       crate(%{pkgname}/mio-0-8)
Provides:       crate(%{pkgname}/support-v0-8)

%description -n %{name}+mio-0-8
This metapackage enables feature "mio-0_8" for the Rust signal-hook-mio crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "support-v0_8" feature.

%package     -n %{name}+mio-1-0
Summary:        MIO support for signal-hook - feature "mio-1_0" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(mio-1.0/default) >= 1.2.0
Requires:       crate(mio-1.0/net) >= 1.2.0
Requires:       crate(mio-1.0/os-ext) >= 1.2.0
Provides:       crate(%{pkgname}/mio-1-0)
Provides:       crate(%{pkgname}/support-v1-0)

%description -n %{name}+mio-1-0
This metapackage enables feature "mio-1_0" for the Rust signal-hook-mio crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "support-v1_0" feature.

%package     -n %{name}+mio-uds
Summary:        MIO support for signal-hook - feature "mio-uds"
Requires:       crate(%{pkgname})
Requires:       crate(mio-uds-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/mio-uds)

%description -n %{name}+mio-uds
This metapackage enables feature "mio-uds" for the Rust signal-hook-mio crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+support-v0-6
Summary:        MIO support for signal-hook - feature "support-v0_6"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/mio-0-6)
Requires:       crate(%{pkgname}/mio-uds)
Provides:       crate(%{pkgname}/support-v0-6)

%description -n %{name}+support-v0-6
This metapackage enables feature "support-v0_6" for the Rust signal-hook-mio crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
