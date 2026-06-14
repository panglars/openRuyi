# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name image
%global full_version 0.25.10
%global pkgname image-0.25

Name:           rust-image-0.25
Version:        0.25.10
Release:        %autorelease
Summary:        Rust crate "image"
License:        MIT OR Apache-2.0
URL:            https://github.com/image-rs/image
#!RemoteAsset:  sha256:85ab80394333c02fe689eaf900ab500fbd0c2213da414687ebf995a65d5a6104
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytemuck-1.0/default) >= 1.25.0
Requires:       crate(bytemuck-1.0/extern-crate-alloc) >= 1.25.0
Requires:       crate(byteorder-lite-0.1/default) >= 0.1.0
Requires:       crate(moxcms-0.8/default) >= 0.8.1
Requires:       crate(num-traits-0.2/default) >= 0.2.19
Provides:       crate(image) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/benchmarks)
Provides:       crate(%{pkgname}/bmp)
Provides:       crate(%{pkgname}/dds)
Provides:       crate(%{pkgname}/ff)
Provides:       crate(%{pkgname}/hdr)
Provides:       crate(%{pkgname}/pnm)
Provides:       crate(%{pkgname}/tga)

%description
Provides basic image processing and encoders/decoders for common image formats.
Source code for takopackized Rust crate "image"

%package     -n %{name}+avif
Summary:        Imaging library - feature "avif"
Requires:       crate(%{pkgname})
Requires:       crate(ravif-0.13) >= 0.13.0
Requires:       crate(rgb-0.8) >= 0.8.53
Provides:       crate(%{pkgname}/avif)

%description -n %{name}+avif
Provides basic image processing and encoders/decoders for common image formats.
This metapackage enables feature "avif" for the Rust image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+avif-native
Summary:        Imaging library - feature "avif-native"
Requires:       crate(%{pkgname})
Requires:       crate(dav1d-0.11/default) >= 0.11.0
Requires:       crate(mp4parse-0.17/default) >= 0.17.0
Provides:       crate(%{pkgname}/avif-native)

%description -n %{name}+avif-native
Provides basic image processing and encoders/decoders for common image formats.
This metapackage enables feature "avif-native" for the Rust image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+color-quant
Summary:        Imaging library - feature "color_quant"
Requires:       crate(%{pkgname})
Requires:       crate(color-quant-1.0/default) >= 1.1.0
Provides:       crate(%{pkgname}/color-quant)

%description -n %{name}+color-quant
Provides basic image processing and encoders/decoders for common image formats.
This metapackage enables feature "color_quant" for the Rust image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Imaging library - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/default-formats)
Requires:       crate(%{pkgname}/rayon)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
Provides basic image processing and encoders/decoders for common image formats.
This metapackage enables feature "default" for the Rust image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default-formats
Summary:        Imaging library - feature "default-formats"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/avif)
Requires:       crate(%{pkgname}/bmp)
Requires:       crate(%{pkgname}/dds)
Requires:       crate(%{pkgname}/exr)
Requires:       crate(%{pkgname}/ff)
Requires:       crate(%{pkgname}/gif)
Requires:       crate(%{pkgname}/hdr)
Requires:       crate(%{pkgname}/ico)
Requires:       crate(%{pkgname}/jpeg)
Requires:       crate(%{pkgname}/png)
Requires:       crate(%{pkgname}/pnm)
Requires:       crate(%{pkgname}/qoi)
Requires:       crate(%{pkgname}/tga)
Requires:       crate(%{pkgname}/tiff)
Requires:       crate(%{pkgname}/webp)
Provides:       crate(%{pkgname}/default-formats)

%description -n %{name}+default-formats
Provides basic image processing and encoders/decoders for common image formats.
This metapackage enables feature "default-formats" for the Rust image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+exr
Summary:        Imaging library - feature "exr"
Requires:       crate(%{pkgname})
Requires:       crate(exr-1.0) >= 1.74.0
Provides:       crate(%{pkgname}/exr)

%description -n %{name}+exr
Provides basic image processing and encoders/decoders for common image formats.
This metapackage enables feature "exr" for the Rust image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gif
Summary:        Imaging library - feature "gif"
Requires:       crate(%{pkgname})
Requires:       crate(color-quant-1.0/default) >= 1.1.0
Requires:       crate(gif-0.14/default) >= 0.14.2
Provides:       crate(%{pkgname}/gif)

%description -n %{name}+gif
Provides basic image processing and encoders/decoders for common image formats.
This metapackage enables feature "gif" for the Rust image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ico
Summary:        Imaging library - feature "ico"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bmp)
Requires:       crate(%{pkgname}/png)
Provides:       crate(%{pkgname}/ico)

%description -n %{name}+ico
Provides basic image processing and encoders/decoders for common image formats.
This metapackage enables feature "ico" for the Rust image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+jpeg
Summary:        Imaging library - feature "jpeg"
Requires:       crate(%{pkgname})
Requires:       crate(zune-core-0.5) >= 0.5.1
Requires:       crate(zune-jpeg-0.5/default) >= 0.5.15
Provides:       crate(%{pkgname}/jpeg)

%description -n %{name}+jpeg
Provides basic image processing and encoders/decoders for common image formats.
This metapackage enables feature "jpeg" for the Rust image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nasm
Summary:        Imaging library - feature "nasm"
Requires:       crate(%{pkgname})
Requires:       crate(ravif-0.13/asm) >= 0.13.0
Provides:       crate(%{pkgname}/nasm)

%description -n %{name}+nasm
Provides basic image processing and encoders/decoders for common image formats.
This metapackage enables feature "nasm" for the Rust image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+png
Summary:        Imaging library - feature "png"
Requires:       crate(%{pkgname})
Requires:       crate(png-0.18/default) >= 0.18.1
Provides:       crate(%{pkgname}/png)

%description -n %{name}+png
Provides basic image processing and encoders/decoders for common image formats.
This metapackage enables feature "png" for the Rust image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+qoi
Summary:        Imaging library - feature "qoi"
Requires:       crate(%{pkgname})
Requires:       crate(qoi-0.4/default) >= 0.4.1
Provides:       crate(%{pkgname}/qoi)

%description -n %{name}+qoi
Provides basic image processing and encoders/decoders for common image formats.
This metapackage enables feature "qoi" for the Rust image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        Imaging library - feature "rayon"
Requires:       crate(%{pkgname})
Requires:       crate(exr-1.0/rayon) >= 1.74.0
Requires:       crate(ravif-0.13/threading) >= 0.13.0
Requires:       crate(rayon-1.0/default) >= 1.7.0
Provides:       crate(%{pkgname}/rayon)

%description -n %{name}+rayon
Provides basic image processing and encoders/decoders for common image formats.
This metapackage enables feature "rayon" for the Rust image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Imaging library - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.214
Requires:       crate(serde-1.0/derive) >= 1.0.214
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
Provides basic image processing and encoders/decoders for common image formats.
This metapackage enables feature "serde" for the Rust image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tiff
Summary:        Imaging library - feature "tiff"
Requires:       crate(%{pkgname})
Requires:       crate(tiff-0.11/default) >= 0.11.3
Provides:       crate(%{pkgname}/tiff)

%description -n %{name}+tiff
Provides basic image processing and encoders/decoders for common image formats.
This metapackage enables feature "tiff" for the Rust image crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+webp
Summary:        Imaging library - feature "webp"
Requires:       crate(%{pkgname})
Requires:       crate(image-webp-0.2/default) >= 0.2.4
Provides:       crate(%{pkgname}/webp)

%description -n %{name}+webp
Provides basic image processing and encoders/decoders for common image formats.
This metapackage enables feature "webp" for the Rust image crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
