# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pcre2-sys
%global full_version 0.2.9
%global pkgname pcre2-sys-0.2
%global tag_version 0.2.9-utf32

Name:           rust-pcre2-sys-0.2
Version:        0.2.9
Release:        %autorelease
Summary:        Rust crate "pcre2-sys"
License:        Unlicense OR MIT
URL:            https://github.com/fish-shell/rust-pcre2
#!RemoteAsset:  sha256:e5af06d7b737b66f7476a223e8a6cd1e2b1ca834b38b3de58901d4dbcf0a054d
Source:         %{url}/archive/refs/tags/%{tag_version}.tar.gz#/rust-pcre2-%{tag_version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1.0/default) >= 1.0.73
Requires:       crate(cc-1.0/parallel) >= 1.0.73
Requires:       crate(libc-0.2/default) >= 0.2.146
Requires:       crate(pkg-config-0.3/default) >= 0.3.27
Requires:       pkgconfig(libpcre2-8)
Provides:       crate(pcre2-sys) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/jit)

%description
Source code for takopackized Rust crate "pcre2-sys"

%package     -n %{name}+utf32
Summary:        Low level bindings to PCRE2 - feature "utf32"
Requires:       crate(%{pkgname})
Requires:       pkgconfig(libpcre2-32)
Provides:       crate(%{pkgname}/utf32)

%description -n %{name}+utf32
This metapackage enables feature "utf32" for the Rust pcre2-sys crate, by pulling in any additional dependencies needed by that feature.

%prep
%autosetup -n rust-pcre2-%{tag_version}

%install
mkdir -p %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}
cp -a pcre2-sys/. %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}/
printf '{"files":{},"package":null}\n' > %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}/.cargo-checksum.json

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
