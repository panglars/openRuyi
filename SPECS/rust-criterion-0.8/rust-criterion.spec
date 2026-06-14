# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name criterion
%global full_version 0.8.2
%global pkgname criterion-0.8

Name:           rust-criterion-0.8
Version:        0.8.2
Release:        %autorelease
Summary:        Rust crate "criterion"
License:        Apache-2.0 OR MIT
URL:            https://criterion-rs.github.io/book/index.html
#!RemoteAsset:  sha256:950046b2aa2492f9a536f5f4f9a3de7b9e2476e575e05bd6c333371add4d98f3
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(alloca-0.4/default) >= 0.4.0
Requires:       crate(anes-0.1/default) >= 0.1.6
Requires:       crate(cast-0.3/default) >= 0.3.0
Requires:       crate(ciborium-0.2/default) >= 0.2.2
Requires:       crate(clap-4.0/help) >= 4.6.1
Requires:       crate(clap-4.0/std) >= 4.6.1
Requires:       crate(criterion-plot-0.8/default) >= 0.8.2
Requires:       crate(itertools-0.13/default) >= 0.13.0
Requires:       crate(num-traits-0.2/std) >= 0.2.19
Requires:       crate(oorandom-11.0/default) >= 11.1.5
Requires:       crate(page-size-0.6/default) >= 0.6.0
Requires:       crate(regex-1.0/std) >= 1.12.3
Requires:       crate(serde-1.0/default) >= 1.0.228
Requires:       crate(serde-1.0/derive) >= 1.0.228
Requires:       crate(serde-json-1.0/default) >= 1.0.149
Requires:       crate(tinytemplate-1.0/default) >= 1.2.1
Requires:       crate(walkdir-2.0/default) >= 2.5.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/async)
Provides:       crate(%{pkgname}/cargo-bench-support)
Provides:       crate(%{pkgname}/html-reports)
Provides:       crate(%{pkgname}/real-blackbox)

%description
Source code for takopackized Rust crate "criterion"

%package     -n %{name}+async-futures
Summary:        Statistics-driven micro-benchmarking library - feature "async_futures"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/async)
Requires:       crate(futures-0.3/executor) >= 0.3.0
Provides:       crate(%{pkgname}/async-futures)

%description -n %{name}+async-futures
This metapackage enables feature "async_futures" for the Rust criterion crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-smol
Summary:        Statistics-driven micro-benchmarking library - feature "async_smol"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/async)
Requires:       crate(smol-2.0) >= 2.0.0
Provides:       crate(%{pkgname}/async-smol)

%description -n %{name}+async-smol
This metapackage enables feature "async_smol" for the Rust criterion crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-tokio
Summary:        Statistics-driven micro-benchmarking library - feature "async_tokio"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/async)
Requires:       crate(tokio-1.0/rt) >= 1.0.0
Provides:       crate(%{pkgname}/async-tokio)

%description -n %{name}+async-tokio
This metapackage enables feature "async_tokio" for the Rust criterion crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+csv-output
Summary:        Statistics-driven micro-benchmarking library - feature "csv_output"
Requires:       crate(%{pkgname})
Requires:       crate(csv-1.0/default) >= 1.1
Provides:       crate(%{pkgname}/csv-output)

%description -n %{name}+csv-output
This metapackage enables feature "csv_output" for the Rust criterion crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Statistics-driven micro-benchmarking library - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/cargo-bench-support)
Requires:       crate(%{pkgname}/plotters)
Requires:       crate(%{pkgname}/rayon)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust criterion crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+plotters
Summary:        Statistics-driven micro-benchmarking library - feature "plotters"
Requires:       crate(%{pkgname})
Requires:       crate(plotters-0.3/area-series) >= 0.3.2
Requires:       crate(plotters-0.3/line-series) >= 0.3.2
Requires:       crate(plotters-0.3/svg-backend) >= 0.3.2
Provides:       crate(%{pkgname}/plotters)

%description -n %{name}+plotters
This metapackage enables feature "plotters" for the Rust criterion crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        Statistics-driven micro-benchmarking library - feature "rayon"
Requires:       crate(%{pkgname})
Requires:       crate(rayon-1.0/default) >= 1.3
Provides:       crate(%{pkgname}/rayon)

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust criterion crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+stable
Summary:        Statistics-driven micro-benchmarking library - feature "stable"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/async-futures)
Requires:       crate(%{pkgname}/async-smol)
Requires:       crate(%{pkgname}/async-tokio)
Requires:       crate(%{pkgname}/csv-output)
Requires:       crate(%{pkgname}/html-reports)
Provides:       crate(%{pkgname}/stable)

%description -n %{name}+stable
This metapackage enables feature "stable" for the Rust criterion crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
