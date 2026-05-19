# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name quantette
%global full_version 0.5.1
%global pkgname quantette-0.5

Name:           rust-quantette-0.5
Version:        0.5.1
Release:        %autorelease
Summary:        Rust crate "quantette"
License:        MIT OR Apache-2.0
URL:            https://github.com/IanManske/quantette
#!RemoteAsset:  sha256:c98fecda8b16396ff9adac67644a523dd1778c42b58606a29df5c31ca925d174
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitvec-1.0/alloc) >= 1.0.1
Requires:       crate(bytemuck-1.0/default) >= 1.25.0
Requires:       crate(bytemuck-1.0/derive) >= 1.25.0
Requires:       crate(bytemuck-1.0/extern-crate-alloc) >= 1.25.0
Requires:       crate(bytemuck-1.0/min-const-generics) >= 1.25.0
Requires:       crate(libm-0.2) >= 0.2.16
Requires:       crate(num-traits-0.2/libm) >= 0.2.19
Requires:       crate(ordered-float-5.0) >= 5.3.0
Requires:       crate(palette-0.7/alloc) >= 0.7.6
Requires:       crate(palette-0.7/bytemuck) >= 0.7.6
Requires:       crate(palette-0.7/libm) >= 0.7.6
Requires:       crate(ref-cast-1.0/default) >= 1.0.25
Requires:       crate(wide-0.8) >= 0.8.3
Provides:       crate(quantette) = %{version}
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "quantette"

%package     -n %{name}+default
Summary:        Fast and high quality image quantization and palette generation - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/image)
Requires:       crate(%{pkgname}/kmeans)
Requires:       crate(%{pkgname}/threads)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust quantette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+image
Summary:        Fast and high quality image quantization and palette generation - feature "image"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(image-0.25) >= 0.25.0
Provides:       crate(%{pkgname}/image)

%description -n %{name}+image
This metapackage enables feature "image" for the Rust quantette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+kmeans
Summary:        Fast and high quality image quantization and palette generation - feature "kmeans"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/rand)
Requires:       crate(%{pkgname}/rand-xoshiro)
Provides:       crate(%{pkgname}/kmeans)

%description -n %{name}+kmeans
This metapackage enables feature "kmeans" for the Rust quantette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        Fast and high quality image quantization and palette generation - feature "rand"
Requires:       crate(%{pkgname})
Requires:       crate(rand-0.9/alloc) >= 0.9.2
Provides:       crate(%{pkgname}/rand)

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust quantette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-xoshiro
Summary:        Fast and high quality image quantization and palette generation - feature "rand_xoshiro"
Requires:       crate(%{pkgname})
Requires:       crate(rand-xoshiro-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/rand-xoshiro)

%description -n %{name}+rand-xoshiro
This metapackage enables feature "rand_xoshiro" for the Rust quantette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        Fast and high quality image quantization and palette generation - feature "rayon"
Requires:       crate(%{pkgname})
Requires:       crate(rayon-1.0/default) >= 1.10.0
Provides:       crate(%{pkgname}/rayon)

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust quantette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Fast and high quality image quantization and palette generation - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(num-traits-0.2/libm) >= 0.2.19
Requires:       crate(num-traits-0.2/std) >= 0.2.19
Requires:       crate(wide-0.8/std) >= 0.8.3
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust quantette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tap
Summary:        Fast and high quality image quantization and palette generation - feature "tap"
Requires:       crate(%{pkgname})
Requires:       crate(tap-1.0) >= 1.0.1
Provides:       crate(%{pkgname}/tap)

%description -n %{name}+tap
This metapackage enables feature "tap" for the Rust quantette crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+threads
Summary:        Fast and high quality image quantization and palette generation - feature "threads"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/rayon)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/threads)

%description -n %{name}+threads
This metapackage enables feature "threads" for the Rust quantette crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
