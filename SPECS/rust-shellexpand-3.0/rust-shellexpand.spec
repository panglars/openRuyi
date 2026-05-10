# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name shellexpand
%global full_version 3.1.2
%global pkgname shellexpand-3.0

Name:           rust-shellexpand-3.0
Version:        3.1.2
Release:        %autorelease
Summary:        Rust crate "shellexpand"
License:        MIT/Apache-2.0
URL:            https://gitlab.com/ijackson/rust-shellexpand
#!RemoteAsset:  sha256:32824fab5e16e6c4d86dc1ba84489390419a39f97699852b66480bb87d297ed8
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(shellexpand) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/base-0)

%description
Source code for takopackized Rust crate "shellexpand"

%package     -n %{name}+bstr
Summary:        Shell-like expansions in strings - feature "bstr"
Requires:       crate(%{pkgname})
Requires:       crate(bstr-1.0.0-pre.2/default) >= 1.0.0-pre.2
Provides:       crate(%{pkgname}/bstr)

%description -n %{name}+bstr
This metapackage enables feature "bstr" for the Rust shellexpand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Shell-like expansions in strings - feature "default" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/base-0)
Requires:       crate(%{pkgname}/tilde)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/full-msrv-1-31)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust shellexpand crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "full-msrv-1-31" feature.

%package     -n %{name}+dirs
Summary:        Shell-like expansions in strings - feature "dirs" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(dirs-4.0/default) >= 4
Provides:       crate(%{pkgname}/dirs)
Provides:       crate(%{pkgname}/tilde)

%description -n %{name}+dirs
This metapackage enables feature "dirs" for the Rust shellexpand crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "tilde" feature.

%package     -n %{name}+full-msrv-1-51
Summary:        Shell-like expansions in strings - feature "full-msrv-1-51" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/full-msrv-1-31)
Requires:       crate(%{pkgname}/path)
Provides:       crate(%{pkgname}/full)
Provides:       crate(%{pkgname}/full-msrv-1-51)

%description -n %{name}+full-msrv-1-51
This metapackage enables feature "full-msrv-1-51" for the Rust shellexpand crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "full" feature.

%package     -n %{name}+os-str-bytes
Summary:        Shell-like expansions in strings - feature "os_str_bytes"
Requires:       crate(%{pkgname})
Requires:       crate(os-str-bytes-5.0/default) >= 5
Provides:       crate(%{pkgname}/os-str-bytes)

%description -n %{name}+os-str-bytes
This metapackage enables feature "os_str_bytes" for the Rust shellexpand crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+path
Summary:        Shell-like expansions in strings - feature "path"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bstr)
Requires:       crate(%{pkgname}/os-str-bytes)
Provides:       crate(%{pkgname}/path)

%description -n %{name}+path
This metapackage enables feature "path" for the Rust shellexpand crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
