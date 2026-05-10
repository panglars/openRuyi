# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pcre2
%global full_version 0.2.9
%global pkgname pcre2-0.2
%global tag_version 0.2.9-utf32

Name:           rust-pcre2-0.2
Version:        0.2.9
Release:        %autorelease
Summary:        Rust crate "pcre2"
License:        Unlicense OR MIT
URL:            https://github.com/fish-shell/rust-pcre2
#!RemoteAsset:  sha256:e5af06d7b737b66f7476a223e8a6cd1e2b1ca834b38b3de58901d4dbcf0a054d
Source:         %{url}/archive/refs/tags/%{tag_version}.tar.gz#/rust-pcre2-%{tag_version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.146
Requires:       crate(log-0.4/default) >= 0.4.19
Requires:       crate(pcre2-sys-0.2/default) >= 0.2.9
Provides:       crate(pcre2) = %{version}
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "pcre2"

%package     -n %{name}+jit
Summary:        High level wrapper library for PCRE2, with UTF-32 support - feature "jit" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(pcre2-sys-0.2/jit) >= 0.2.9
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/jit)

%description -n %{name}+jit
This metapackage enables feature "jit" for the Rust pcre2 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+utf32
Summary:        High level wrapper library for PCRE2, with UTF-32 support - feature "utf32"
Requires:       crate(%{pkgname})
Requires:       crate(pcre2-sys-0.2/utf32) >= 0.2.9
Provides:       crate(%{pkgname}/utf32)

%description -n %{name}+utf32
This metapackage enables feature "utf32" for the Rust pcre2 crate, by pulling in any additional dependencies needed by that feature.

%prep
%autosetup -n rust-pcre2-%{tag_version}
sed -i '/^\[workspace\]/,/^$/d' Cargo.toml
sed -i 's/pcre2-sys = { version = "0.2.9", path = "pcre2-sys" }/pcre2-sys = "0.2.9"/' Cargo.toml
rm -rf pcre2-sys

%install
mkdir -p %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}
cp -a . %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}/
printf '{"files":{},"package":null}\n' > %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}/.cargo-checksum.json

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
