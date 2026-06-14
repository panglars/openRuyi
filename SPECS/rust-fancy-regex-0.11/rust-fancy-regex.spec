# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fancy-regex
%global full_version 0.11.0
%global pkgname fancy-regex-0.11

Name:           rust-fancy-regex-0.11
Version:        0.11.0
Release:        %autorelease
Summary:        Rust crate "fancy-regex"
License:        MIT
URL:            https://github.com/fancy-regex/fancy-regex
#!RemoteAsset:  sha256:b95f7c0680e4142284cf8b22c14a476e87d61b004a3a0861872b32ef7ead40a2
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bit-set-0.5/default) >= 0.5.3
Requires:       crate(regex-1.0/std) >= 1.12.3
Provides:       crate(fancy-regex) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/track-caller)

%description
Source code for takopackized Rust crate "fancy-regex"

%package     -n %{name}+default
Summary:        Regexes, supporting a relatively rich set of features, including backreferences and look-around - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/perf)
Requires:       crate(%{pkgname}/unicode)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust fancy-regex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+perf
Summary:        Regexes, supporting a relatively rich set of features, including backreferences and look-around - feature "perf"
Requires:       crate(%{pkgname})
Requires:       crate(regex-1.0/perf) >= 1.12.3
Requires:       crate(regex-1.0/std) >= 1.12.3
Provides:       crate(%{pkgname}/perf)

%description -n %{name}+perf
This metapackage enables feature "perf" for the Rust fancy-regex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+perf-cache
Summary:        Regexes, supporting a relatively rich set of features, including backreferences and look-around - feature "perf-cache"
Requires:       crate(%{pkgname})
Requires:       crate(regex-1.0/perf-cache) >= 1.12.3
Requires:       crate(regex-1.0/std) >= 1.12.3
Provides:       crate(%{pkgname}/perf-cache)

%description -n %{name}+perf-cache
This metapackage enables feature "perf-cache" for the Rust fancy-regex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+perf-dfa
Summary:        Regexes, supporting a relatively rich set of features, including backreferences and look-around - feature "perf-dfa"
Requires:       crate(%{pkgname})
Requires:       crate(regex-1.0/perf-dfa) >= 1.12.3
Requires:       crate(regex-1.0/std) >= 1.12.3
Provides:       crate(%{pkgname}/perf-dfa)

%description -n %{name}+perf-dfa
This metapackage enables feature "perf-dfa" for the Rust fancy-regex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+perf-inline
Summary:        Regexes, supporting a relatively rich set of features, including backreferences and look-around - feature "perf-inline"
Requires:       crate(%{pkgname})
Requires:       crate(regex-1.0/perf-inline) >= 1.12.3
Requires:       crate(regex-1.0/std) >= 1.12.3
Provides:       crate(%{pkgname}/perf-inline)

%description -n %{name}+perf-inline
This metapackage enables feature "perf-inline" for the Rust fancy-regex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+perf-literal
Summary:        Regexes, supporting a relatively rich set of features, including backreferences and look-around - feature "perf-literal"
Requires:       crate(%{pkgname})
Requires:       crate(regex-1.0/perf-literal) >= 1.12.3
Requires:       crate(regex-1.0/std) >= 1.12.3
Provides:       crate(%{pkgname}/perf-literal)

%description -n %{name}+perf-literal
This metapackage enables feature "perf-literal" for the Rust fancy-regex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode
Summary:        Regexes, supporting a relatively rich set of features, including backreferences and look-around - feature "unicode"
Requires:       crate(%{pkgname})
Requires:       crate(regex-1.0/std) >= 1.12.3
Requires:       crate(regex-1.0/unicode) >= 1.12.3
Provides:       crate(%{pkgname}/unicode)

%description -n %{name}+unicode
This metapackage enables feature "unicode" for the Rust fancy-regex crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
