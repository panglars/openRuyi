# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name termwiz
%global full_version 0.23.3
%global pkgname termwiz-0.23

Name:           rust-termwiz-0.23
Version:        0.23.3
Release:        %autorelease
Summary:        Rust crate "termwiz"
License:        MIT
URL:            https://github.com/wezterm/wezterm
#!RemoteAsset:  sha256:4676b37242ccbd1aabf56edb093a4827dc49086c0ffd764a5705899e0f35f8f7
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1.0/default) >= 1.0.102
Requires:       crate(base64-0.22/default) >= 0.22.1
Requires:       crate(bitflags-2.0/default) >= 2.11.1
Requires:       crate(fancy-regex-0.11/default) >= 0.11.0
Requires:       crate(filedescriptor-0.8/default) >= 0.8.3
Requires:       crate(finl-unicode-1.0/default) >= 1.4.0
Requires:       crate(fixedbitset-0.4/default) >= 0.4.2
Requires:       crate(hex-0.4/default) >= 0.4.3
Requires:       crate(lazy-static-1.0/default) >= 1.5.0
Requires:       crate(libc-0.2/default) >= 0.2.186
Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(memmem-0.1/default) >= 0.1.1
Requires:       crate(nix-0.29/default) >= 0.29.0
Requires:       crate(nix-0.29/fs) >= 0.29.0
Requires:       crate(nix-0.29/mman) >= 0.29.0
Requires:       crate(num-derive-0.4/default) >= 0.4.2
Requires:       crate(num-traits-0.2/default) >= 0.2.19
Requires:       crate(ordered-float-4.0/default) >= 4.6.0
Requires:       crate(pest-2.0/default) >= 2.8.6
Requires:       crate(pest-derive-2.0/default) >= 2.8.6
Requires:       crate(phf-0.11/default) >= 0.11.3
Requires:       crate(sha2-0.10/default) >= 0.10.9
Requires:       crate(signal-hook-0.3/default) >= 0.3.18
Requires:       crate(siphasher-1.0/default) >= 1.0.3
Requires:       crate(terminfo-0.9/default) >= 0.9.0
Requires:       crate(termios-0.3/default) >= 0.3.3
Requires:       crate(thiserror-1.0/default) >= 1.0.69
Requires:       crate(ucd-trie-0.1/default) >= 0.1.7
Requires:       crate(unicode-segmentation-1.0/default) >= 1.13.2
Requires:       crate(vtparse-0.6/default) >= 0.6.2
Requires:       crate(wezterm-bidi-0.2/default) >= 0.2.3
Requires:       crate(wezterm-blob-leases-0.1/default) >= 0.1.1
Requires:       crate(wezterm-color-types-0.3/default) >= 0.3.0
Requires:       crate(wezterm-dynamic-0.2/default) >= 0.2.1
Requires:       crate(wezterm-input-types-0.1/default) >= 0.1.0
Requires:       crate(winapi-0.3/consoleapi) >= 0.3.9
Requires:       crate(winapi-0.3/default) >= 0.3.9
Requires:       crate(winapi-0.3/fileapi) >= 0.3.9
Requires:       crate(winapi-0.3/handleapi) >= 0.3.9
Requires:       crate(winapi-0.3/impl-default) >= 0.3.9
Requires:       crate(winapi-0.3/memoryapi) >= 0.3.9
Requires:       crate(winapi-0.3/synchapi) >= 0.3.9
Requires:       crate(winapi-0.3/winbase) >= 0.3.9
Requires:       crate(winapi-0.3/winerror) >= 0.3.9
Requires:       crate(winapi-0.3/winnls) >= 0.3.9
Requires:       crate(winapi-0.3/winnt) >= 0.3.9
Requires:       crate(winapi-0.3/winuser) >= 0.3.9
Provides:       crate(termwiz) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "termwiz"

%package     -n %{name}+cassowary
Summary:        Terminal Wizardry for Unix and Windows - feature "cassowary"
Requires:       crate(%{pkgname})
Requires:       crate(cassowary-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/cassowary)

%description -n %{name}+cassowary
This metapackage enables feature "cassowary" for the Rust termwiz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+docs
Summary:        Terminal Wizardry for Unix and Windows - feature "docs"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/use-serde)
Requires:       crate(%{pkgname}/widgets)
Provides:       crate(%{pkgname}/docs)

%description -n %{name}+docs
This metapackage enables feature "docs" for the Rust termwiz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fnv
Summary:        Terminal Wizardry for Unix and Windows - feature "fnv"
Requires:       crate(%{pkgname})
Requires:       crate(fnv-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/fnv)

%description -n %{name}+fnv
This metapackage enables feature "fnv" for the Rust termwiz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+image
Summary:        Terminal Wizardry for Unix and Windows - feature "image" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(image-0.25/default) >= 0.25.0
Provides:       crate(%{pkgname}/image)
Provides:       crate(%{pkgname}/use-image)

%description -n %{name}+image
This metapackage enables feature "image" for the Rust termwiz crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "use_image" feature.

%package     -n %{name}+serde
Summary:        Terminal Wizardry for Unix and Windows - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.228
Requires:       crate(serde-1.0/derive) >= 1.0.228
Requires:       crate(serde-1.0/rc) >= 1.0.228
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust termwiz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+use-serde
Summary:        Terminal Wizardry for Unix and Windows - feature "use_serde"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/serde)
Requires:       crate(bitflags-2.0/serde) >= 2.11.1
Requires:       crate(wezterm-blob-leases-0.1/serde) >= 0.1.1
Requires:       crate(wezterm-color-types-0.3/use-serde) >= 0.3.0
Requires:       crate(wezterm-input-types-0.1/serde) >= 0.1.0
Provides:       crate(%{pkgname}/use-serde)

%description -n %{name}+use-serde
This metapackage enables feature "use_serde" for the Rust termwiz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+widgets
Summary:        Terminal Wizardry for Unix and Windows - feature "widgets"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/cassowary)
Requires:       crate(%{pkgname}/fnv)
Provides:       crate(%{pkgname}/widgets)

%description -n %{name}+widgets
This metapackage enables feature "widgets" for the Rust termwiz crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
