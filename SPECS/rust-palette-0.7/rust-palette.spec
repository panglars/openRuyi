# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name palette
%global full_version 0.7.6
%global pkgname palette-0.7

Name:           rust-palette-0.7
Version:        0.7.6
Release:        %autorelease
Summary:        Rust crate "palette"
License:        MIT OR Apache-2.0
URL:            https://github.com/Ogeon/palette
#!RemoteAsset:  sha256:4cbf71184cc5ecc2e4e1baccdb21026c20e5fc3dcf63028a086131b3ab00b6e6
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(fast-srgb8-1.0/default) >= 1.0.0
Requires:       crate(palette-derive-0.7/default) >= 0.7.6
Provides:       crate(palette) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/named)

%description
Source code for takopackized Rust crate "palette"

%package     -n %{name}+approx
Summary:        Convert and manage colors with a focus on correctness, flexibility and ease of use - feature "approx"
Requires:       crate(%{pkgname})
Requires:       crate(approx-0.5) >= 0.5.0
Provides:       crate(%{pkgname}/approx)

%description -n %{name}+approx
This metapackage enables feature "approx" for the Rust palette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytemuck
Summary:        Convert and manage colors with a focus on correctness, flexibility and ease of use - feature "bytemuck"
Requires:       crate(%{pkgname})
Requires:       crate(bytemuck-1.0/default) >= 1.25.0
Provides:       crate(%{pkgname}/bytemuck)

%description -n %{name}+bytemuck
This metapackage enables feature "bytemuck" for the Rust palette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Convert and manage colors with a focus on correctness, flexibility and ease of use - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/approx)
Requires:       crate(%{pkgname}/named-from-str)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust palette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+find-crate
Summary:        Convert and manage colors with a focus on correctness, flexibility and ease of use - feature "find-crate"
Requires:       crate(%{pkgname})
Requires:       crate(palette-derive-0.7/find-crate) >= 0.7.6
Provides:       crate(%{pkgname}/find-crate)

%description -n %{name}+find-crate
This metapackage enables feature "find-crate" for the Rust palette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libm
Summary:        Convert and manage colors with a focus on correctness, flexibility and ease of use - feature "libm"
Requires:       crate(%{pkgname})
Requires:       crate(libm-0.2) >= 0.2.16
Provides:       crate(%{pkgname}/libm)

%description -n %{name}+libm
This metapackage enables feature "libm" for the Rust palette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+named-from-str
Summary:        Convert and manage colors with a focus on correctness, flexibility and ease of use - feature "named_from_str"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/named)
Requires:       crate(%{pkgname}/phf)
Provides:       crate(%{pkgname}/named-from-str)

%description -n %{name}+named-from-str
This metapackage enables feature "named_from_str" for the Rust palette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+phf
Summary:        Convert and manage colors with a focus on correctness, flexibility and ease of use - feature "phf"
Requires:       crate(%{pkgname})
Requires:       crate(phf-0.11/macros) >= 0.11.0
Provides:       crate(%{pkgname}/phf)

%description -n %{name}+phf
This metapackage enables feature "phf" for the Rust palette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        Convert and manage colors with a focus on correctness, flexibility and ease of use - feature "rand" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(rand-0.8) >= 0.8.0
Provides:       crate(%{pkgname}/rand)
Provides:       crate(%{pkgname}/random)

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust palette crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "random" feature.

%package     -n %{name}+serde
Summary:        Convert and manage colors with a focus on correctness, flexibility and ease of use - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.0
Requires:       crate(serde-1.0/serde-derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust palette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serializing
Summary:        Convert and manage colors with a focus on correctness, flexibility and ease of use - feature "serializing"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/serde)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/serializing)

%description -n %{name}+serializing
This metapackage enables feature "serializing" for the Rust palette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Convert and manage colors with a focus on correctness, flexibility and ease of use - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(approx-0.5/std) >= 0.5.0
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust palette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wide
Summary:        Convert and manage colors with a focus on correctness, flexibility and ease of use - feature "wide"
Requires:       crate(%{pkgname})
Requires:       crate(wide-0.7) >= 0.7.3
Provides:       crate(%{pkgname}/wide)

%description -n %{name}+wide
This metapackage enables feature "wide" for the Rust palette crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
