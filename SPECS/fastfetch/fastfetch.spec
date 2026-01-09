# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:          fastfetch
Version:       2.56.1
Release:       %autorelease
Summary:       Display system information in a stylized manner
License:       MIT
URL:           https://github.com/fastfetch-cli/fastfetch
#!RemoteAsset: sha256:6ffd75c32b2a885fd8497867645ac837ed37d588c94e0df05408cdaa0c8fd2c7
Source:        https://github.com/fastfetch-cli/fastfetch/archive/refs/tags/%{version}.tar.gz

Patch0:        0001-Logo-Builtin-Add-openruyi.patch

BuildRequires: pkg-config
BuildRequires: python3
BuildRequires: cmake
BuildRequires: gcc-c++
BuildSystem:   cmake

# TODO: Add package yyjson.
# BuildOption(conf): -DENABLE_SYSTEM_YYJSON=ON
BuildOption(conf):  -DBUILD_FLASHFETCH=OFF
BuildOption(conf):  -DBUILD_TESTS=ON
BuildOption(conf):  -DINSTALL_LICENSE=OFF
Provides:           bundled(yyjson)

%description
Fastfetch is a tool for fetching system information and displaying it in
a stylized way.  Fastfetch displays this information next to a logo of the
system distribution, akin to many similar tools.

%files
%license LICENSE
%{_bindir}/fastfetch
%{_datadir}/fastfetch/*
%{_datadir}/bash-completion/completions/fastfetch
%{_datadir}/fish/vendor_completions.d/fastfetch.fish
%{_datadir}/zsh/site-functions/_fastfetch
%{_mandir}/man1/fastfetch.1*
%changelog
%{?autochangelog}
