# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rust-embed
%global full_version 8.11.0
%global pkgname rust-embed-8.0

Name:           rust-rust-embed-8.0
Version:        8.11.0
Release:        %autorelease
Summary:        Rust crate "rust-embed"
License:        MIT
URL:            https://pyrossh.dev/repos/rust-embed
#!RemoteAsset:  sha256:04113cb9355a377d83f06ef1f0a45b8ab8cd7d8b1288160717d66df5c7988d27
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rust-embed-impl-8.0/default) >= 8.9.0
Requires:       crate(rust-embed-utils-8.0/default) >= 8.9.0
Requires:       crate(walkdir-2.0/default) >= 2.3.2
Provides:       crate(rust-embed) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "rust-embed"

%package     -n %{name}+actix
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "actix"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/actix-web)
Requires:       crate(%{pkgname}/mime-guess)
Provides:       crate(%{pkgname}/actix)

%description -n %{name}+actix
This metapackage enables feature "actix" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+actix-web
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "actix-web"
Requires:       crate(%{pkgname})
Requires:       crate(actix-web-4.0/default) >= 4.0.0
Provides:       crate(%{pkgname}/actix-web)

%description -n %{name}+actix-web
This metapackage enables feature "actix-web" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+axum
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "axum"
Requires:       crate(%{pkgname})
Requires:       crate(axum-0.8/http1) >= 0.8.0
Requires:       crate(axum-0.8/tokio) >= 0.8.0
Provides:       crate(%{pkgname}/axum)

%description -n %{name}+axum
This metapackage enables feature "axum" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+axum-ex
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "axum-ex"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/axum)
Requires:       crate(%{pkgname}/mime-guess)
Requires:       crate(%{pkgname}/tokio)
Provides:       crate(%{pkgname}/axum-ex)

%description -n %{name}+axum-ex
This metapackage enables feature "axum-ex" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+compression
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "compression"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/include-flate)
Requires:       crate(rust-embed-impl-8.0/compression) >= 8.9.0
Provides:       crate(%{pkgname}/compression)

%description -n %{name}+compression
This metapackage enables feature "compression" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+debug-embed
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "debug-embed"
Requires:       crate(%{pkgname})
Requires:       crate(rust-embed-impl-8.0/debug-embed) >= 8.9.0
Requires:       crate(rust-embed-utils-8.0/debug-embed) >= 8.9.0
Provides:       crate(%{pkgname}/debug-embed)

%description -n %{name}+debug-embed
This metapackage enables feature "debug-embed" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deterministic-timestamps
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "deterministic-timestamps"
Requires:       crate(%{pkgname})
Requires:       crate(rust-embed-impl-8.0/deterministic-timestamps) >= 8.9.0
Provides:       crate(%{pkgname}/deterministic-timestamps)

%description -n %{name}+deterministic-timestamps
This metapackage enables feature "deterministic-timestamps" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hex
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "hex"
Requires:       crate(%{pkgname})
Requires:       crate(hex-0.4/default) >= 0.4.3
Provides:       crate(%{pkgname}/hex)

%description -n %{name}+hex
This metapackage enables feature "hex" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+include-exclude
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "include-exclude"
Requires:       crate(%{pkgname})
Requires:       crate(rust-embed-impl-8.0/include-exclude) >= 8.9.0
Requires:       crate(rust-embed-utils-8.0/include-exclude) >= 8.9.0
Provides:       crate(%{pkgname}/include-exclude)

%description -n %{name}+include-exclude
This metapackage enables feature "include-exclude" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+include-flate
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "include-flate"
Requires:       crate(%{pkgname})
Requires:       crate(include-flate-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/include-flate)

%description -n %{name}+include-flate
This metapackage enables feature "include-flate" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+interpolate-folder-path
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "interpolate-folder-path"
Requires:       crate(%{pkgname})
Requires:       crate(rust-embed-impl-8.0/interpolate-folder-path) >= 8.9.0
Provides:       crate(%{pkgname}/interpolate-folder-path)

%description -n %{name}+interpolate-folder-path
This metapackage enables feature "interpolate-folder-path" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mime-guess
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "mime_guess"
Requires:       crate(%{pkgname})
Requires:       crate(mime-guess-2.0/default) >= 2.0.5
Requires:       crate(rust-embed-impl-8.0/mime-guess) >= 8.9.0
Requires:       crate(rust-embed-utils-8.0/mime-guess) >= 8.9.0
Provides:       crate(%{pkgname}/mime-guess)

%description -n %{name}+mime-guess
This metapackage enables feature "mime_guess" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+poem
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "poem"
Requires:       crate(%{pkgname})
Requires:       crate(poem-1.0/server) >= 1.3.30
Provides:       crate(%{pkgname}/poem)

%description -n %{name}+poem
This metapackage enables feature "poem" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+poem-ex
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "poem-ex"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/hex)
Requires:       crate(%{pkgname}/mime-guess)
Requires:       crate(%{pkgname}/poem)
Requires:       crate(%{pkgname}/tokio)
Provides:       crate(%{pkgname}/poem-ex)

%description -n %{name}+poem-ex
This metapackage enables feature "poem-ex" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rocket
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "rocket"
Requires:       crate(%{pkgname})
Requires:       crate(rocket-0.5.0-rc.2) >= 0.5.0-rc.2
Provides:       crate(%{pkgname}/rocket)

%description -n %{name}+rocket
This metapackage enables feature "rocket" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+salvo
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "salvo"
Requires:       crate(%{pkgname})
Requires:       crate(salvo-0.16) >= 0.16.0
Provides:       crate(%{pkgname}/salvo)

%description -n %{name}+salvo
This metapackage enables feature "salvo" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+salvo-ex
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "salvo-ex"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/hex)
Requires:       crate(%{pkgname}/mime-guess)
Requires:       crate(%{pkgname}/salvo)
Requires:       crate(%{pkgname}/tokio)
Provides:       crate(%{pkgname}/salvo-ex)

%description -n %{name}+salvo-ex
This metapackage enables feature "salvo-ex" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "tokio"
Requires:       crate(%{pkgname})
Requires:       crate(tokio-1.0/default) >= 1.0.0
Requires:       crate(tokio-1.0/macros) >= 1.0.0
Requires:       crate(tokio-1.0/rt-multi-thread) >= 1.0.0
Provides:       crate(%{pkgname}/tokio)

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+warp
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "warp"
Requires:       crate(%{pkgname})
Requires:       crate(warp-0.3) >= 0.3.0
Provides:       crate(%{pkgname}/warp)

%description -n %{name}+warp
This metapackage enables feature "warp" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+warp-ex
Summary:        Rust Custom Derive Macro which loads files into the rust binary at compile time during release and loads the file from the fs during dev - feature "warp-ex"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/mime-guess)
Requires:       crate(%{pkgname}/tokio)
Requires:       crate(%{pkgname}/warp)
Provides:       crate(%{pkgname}/warp-ex)

%description -n %{name}+warp-ex
This metapackage enables feature "warp-ex" for the Rust rust-embed crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
