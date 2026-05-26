# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           yazi
Version:        26.5.6
Release:        %autorelease
Summary:        Blazing fast terminal file manager written in Rust
License:        MIT
URL:            https://yazi-rs.github.io
VCS:            git:https://github.com/sxyazi/yazi.git
#!RemoteAsset:  sha256:a18445df86a20068f7b17609d12d6f635de488958579ae7a2b143a244ba7e63f
Source:         https://github.com/sxyazi/yazi/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    rust

BuildRequires:  cargo >= 1.95.0
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  rust >= 1.95.0
BuildRequires:  rust-rpm-macros
BuildRequires:  crate(avif-serialize-0.8.8/default) >= 0.8.8
BuildRequires:  crate(cc-1.2.61/default) >= 1.2.61
BuildRequires:  crate(crypto-common-0.1.7/default) >= 0.1.7
BuildRequires:  crate(generic-array-0.14.7/default) >= 0.14.7
BuildRequires:  crate(js-sys-0.3.97/default) >= 0.3.97
BuildRequires:  crate(no-std-io2-0.9.3/default) >= 0.9.3
BuildRequires:  crate(quick-xml-0.39.3/default) >= 0.39.3
BuildRequires:  crate(rfc6979-0.5.0-rc.5/default) >= 0.5.0
BuildRequires:  crate(semver-1.0.28/default) >= 1.0.28
BuildRequires:  crate(wasm-bindgen-0.2.120/default) >= 0.2.120
BuildRequires:  crate(wasm-bindgen-futures-0.4.70/default) >= 0.4.70
BuildRequires:  crate(wasm-bindgen-macro-0.2.120/default) >= 0.2.120
BuildRequires:  crate(wasm-bindgen-macro-support-0.2.120/default) >= 0.2.120
BuildRequires:  crate(wasm-bindgen-shared-0.2.120/default) >= 0.2.120
BuildRequires:  crate(ansi-to-tui-8.0/default) >= 8.0.1
BuildRequires:  crate(anyhow-1.0/default) >= 1.0.102
BuildRequires:  crate(arc-swap-1.0/default) >= 1.9.1
BuildRequires:  crate(arc-swap-1.0/serde) >= 1.9.1
BuildRequires:  crate(async-priority-channel-0.2/default) >= 0.2.0
BuildRequires:  crate(base64-0.22/default) >= 0.22.1
BuildRequires:  crate(better-panic-0.3/default) >= 0.3.0
BuildRequires:  crate(bitflags-2.0/default) >= 2.11.1
BuildRequires:  crate(bitflags-2.0/serde) >= 2.11.1
BuildRequires:  crate(chrono-0.4/default) >= 0.4.44
BuildRequires:  crate(clap-4.0/default) >= 4.6.1
BuildRequires:  crate(clap-4.0/derive) >= 4.6.1
BuildRequires:  crate(clap-complete-4.0/default) >= 4.6.3
BuildRequires:  crate(clap-complete-fig-4.0/default) >= 4.5.2
BuildRequires:  crate(clap-complete-nushell-4.0/default) >= 4.6.0
BuildRequires:  crate(clipboard-win-5.0/default) >= 5.4.1
BuildRequires:  crate(crossterm-0.28/default) >= 0.28.1
BuildRequires:  crate(crossterm-0.29/default) >= 0.29.0
BuildRequires:  crate(crossterm-0.29/event-stream) >= 0.29.0
BuildRequires:  crate(deadpool-0.13/managed) >= 0.13.0
BuildRequires:  crate(deadpool-0.13/rt-tokio-1) >= 0.13.0
BuildRequires:  crate(dirs-6.0/default) >= 6.0.0
BuildRequires:  crate(dyn-clone-1.0/default) >= 1.0.20
BuildRequires:  crate(either-1.0/default) >= 1.15.0
BuildRequires:  crate(fdlimit-0.3/default) >= 0.3.0
BuildRequires:  crate(foldhash-0.2/default) >= 0.2.0
BuildRequires:  crate(futures-0.3/default) >= 0.3.32
BuildRequires:  crate(globset-0.4/default) >= 0.4.18
BuildRequires:  crate(hashbrown-0.17/default) >= 0.17.0
BuildRequires:  crate(hashbrown-0.17/serde) >= 0.17.0
BuildRequires:  crate(image-0.25/avif) >= 0.25.10
BuildRequires:  crate(image-0.25/bmp) >= 0.25.10
BuildRequires:  crate(image-0.25/dds) >= 0.25.10
BuildRequires:  crate(image-0.25/exr) >= 0.25.10
BuildRequires:  crate(image-0.25/ff) >= 0.25.10
BuildRequires:  crate(image-0.25/gif) >= 0.25.10
BuildRequires:  crate(image-0.25/hdr) >= 0.25.10
BuildRequires:  crate(image-0.25/ico) >= 0.25.10
BuildRequires:  crate(image-0.25/jpeg) >= 0.25.10
BuildRequires:  crate(image-0.25/png) >= 0.25.10
BuildRequires:  crate(image-0.25/pnm) >= 0.25.10
BuildRequires:  crate(image-0.25/qoi) >= 0.25.10
BuildRequires:  crate(image-0.25/tga) >= 0.25.10
BuildRequires:  crate(image-0.25/tiff) >= 0.25.10
BuildRequires:  crate(image-0.25/webp) >= 0.25.10
BuildRequires:  crate(indexmap-1.0/default) >= 1.8.0
BuildRequires:  crate(indexmap-1.0/serde-1) >= 1.8.0
BuildRequires:  crate(indexmap-2.14.0/default) >= 2.14.0
BuildRequires:  crate(indexmap-2.14.0/serde) >= 2.14.0
BuildRequires:  crate(libc-0.2/default) >= 0.2.186
BuildRequires:  crate(lru-0.18/default) >= 0.18.0
BuildRequires:  crate(memchr-2.0/default) >= 2.8.0
BuildRequires:  crate(mlua-0.11/anyhow) >= 0.11.6
BuildRequires:  crate(mlua-0.11/async) >= 0.11.6
BuildRequires:  crate(mlua-0.11/default) >= 0.11.6
BuildRequires:  crate(mlua-0.11/error-send) >= 0.11.6
BuildRequires:  crate(mlua-0.11/lua55) >= 0.11.6
BuildRequires:  crate(mlua-0.11/macros) >= 0.11.6
BuildRequires:  crate(mlua-0.11/serde) >= 0.11.6
BuildRequires:  crate(mlua-0.11/vendored) >= 0.11.6
BuildRequires:  crate(moxcms-0.8/default) >= 0.8.1
BuildRequires:  crate(notify-8.0/macos-fsevent) >= 8.2.0
BuildRequires:  crate(ordered-float-5.0/default) >= 5.3.0
BuildRequires:  crate(ordered-float-5.0/serde) >= 5.3.0
BuildRequires:  crate(palette-0.7) >= 0.7.6
BuildRequires:  crate(parking-lot-0.12/default) >= 0.12.5
BuildRequires:  crate(paste-1.0/default) >= 1.0.15
BuildRequires:  crate(percent-encoding-2.0/default) >= 2.3.2
BuildRequires:  crate(proc-macro2-1.0/default) >= 1.0.106
BuildRequires:  crate(quantette-0.5) >= 0.5.1
BuildRequires:  crate(quote-1.0/default) >= 1.0.45
BuildRequires:  crate(rand-0.10/std) >= 0.10.1
BuildRequires:  crate(rand-0.10/sys-rng) >= 0.10.1
BuildRequires:  crate(ratatui-0.30/default) >= 0.30.0
BuildRequires:  crate(ratatui-0.30/serde) >= 0.30.0
BuildRequires:  crate(ratatui-0.30/unstable-rendered-line-info) >= 0.30.0
BuildRequires:  crate(ratatui-0.30/unstable-widget-ref) >= 0.30.0
BuildRequires:  crate(regex-1.0/default) >= 1.12.3
BuildRequires:  crate(russh-0.60/ring) >= 0.60.2
BuildRequires:  crate(russh-0.60/rsa) >= 0.60.2
BuildRequires:  crate(scopeguard-1.0/default) >= 1.2.0
BuildRequires:  crate(schemars-0.9) >= 0.9.0
BuildRequires:  crate(schemars-1.0) >= 1.2.1
BuildRequires:  crate(serde-1.0/default) >= 1.0.228
BuildRequires:  crate(serde-1.0/derive) >= 1.0.228
BuildRequires:  crate(serde-json-1.0/default) >= 1.0.149
BuildRequires:  crate(serde-with-3.0/default) >= 3.19.0
BuildRequires:  crate(signal-hook-tokio-0.4/default) >= 0.4.0
BuildRequires:  crate(signal-hook-tokio-0.4/futures-v0-3) >= 0.4.0
BuildRequires:  crate(strum-0.28/default) >= 0.28.0
BuildRequires:  crate(strum-0.28/derive) >= 0.28.0
BuildRequires:  crate(syn-2.0/default) >= 2.0.117
BuildRequires:  crate(syn-2.0/full) >= 2.0.117
BuildRequires:  crate(syntect-5.0/parsing) >= 5.3.0
BuildRequires:  crate(syntect-5.0/plist-load) >= 5.3.0
BuildRequires:  crate(syntect-5.0/regex-onig) >= 5.3.0
BuildRequires:  crate(thiserror-2.0/default) >= 2.0.18
BuildRequires:  crate(tikv-jemallocator-0.6/default) >= 0.61
BuildRequires:  crate(tokio-1.52.2/default) >= 1.52.2
BuildRequires:  crate(tokio-1.52.2/full) >= 1.52.2
BuildRequires:  crate(tokio-stream-0.1/default) >= 0.1.18
BuildRequires:  crate(tokio-util-0.7/default) >= 0.7.18
BuildRequires:  crate(toml-1.0/default) >= 1.1.2
BuildRequires:  crate(tracing-0.1/default) >= 0.1.44
BuildRequires:  crate(tracing-0.1/max-level-debug) >= 0.1.44
BuildRequires:  crate(tracing-0.1/release-max-level-debug) >= 0.1.44
BuildRequires:  crate(tracing-appender-0.2/default) >= 0.2.5
BuildRequires:  crate(tracing-subscriber-0.3/default) >= 0.3.23
BuildRequires:  crate(tracing-subscriber-0.3/env-filter) >= 0.3.23
BuildRequires:  crate(trash-5.0/default) >= 5.2.6
BuildRequires:  crate(twox-hash-2.0/random) >= 2.1.2
BuildRequires:  crate(twox-hash-2.0/std) >= 2.1.2
BuildRequires:  crate(twox-hash-2.0/xxhash3-128) >= 2.1.2
BuildRequires:  crate(typed-path-0.12/default) >= 0.12.3
BuildRequires:  crate(unicode-segmentation-1.0/default) >= 1.13.2
BuildRequires:  crate(unicode-width-0.2) >= 0.2.2
BuildRequires:  crate(uzers-0.12/default) >= 0.12.2
BuildRequires:  crate(vergen-gitcl-9.0/build) >= 9.1.0
BuildRequires:  crate(vergen-gitcl-9.0/default) >= 9.1.0
BuildRequires:  crate(vergen-gitcl-9.0/rustc) >= 9.1.0
BuildRequires:  crate(yazi-prebuilt-0.1/default) >= 0.1.0

Requires:       file

%description
Yazi is a terminal file manager written in Rust, based on non-blocking async I/O.
It provides a fast and customizable file management experience for terminal
workflows.

%build
# RPM-installed directory registry crates may not preserve crates.io package checksum metadata, while crate source archives are already verified by RPM Source hashes.
sed -i '/^checksum = /d' Cargo.lock

YAZI_GEN_COMPLETIONS=1 YAZI_NO_GITCL=1 cargo build --release --offline

%install -a
install -Dm0755 target/release/yazi %{buildroot}%{_bindir}/yazi
install -Dm0755 target/release/ya %{buildroot}%{_bindir}/ya

install -Dm0644 yazi-boot/completions/yazi.bash %{buildroot}%{_datadir}/bash-completion/completions/yazi
install -Dm0644 yazi-cli/completions/ya.bash %{buildroot}%{_datadir}/bash-completion/completions/ya
install -Dm0644 yazi-boot/completions/yazi.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/yazi.fish
install -Dm0644 yazi-cli/completions/ya.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/ya.fish
install -Dm0644 yazi-boot/completions/_yazi %{buildroot}%{_datadir}/zsh/site-functions/_yazi
install -Dm0644 yazi-cli/completions/_ya %{buildroot}%{_datadir}/zsh/site-functions/_ya

install -Dm0644 assets/yazi.desktop %{buildroot}%{_datadir}/applications/yazi.desktop
install -Dm0644 assets/logo.png %{buildroot}%{_datadir}/pixmaps/yazi.png

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/yazi.desktop
target/release/yazi --version
target/release/ya --version

%files
%doc README.md CHANGELOG.md
%license LICENSE LICENSE-ICONS
%{_bindir}/ya
%{_bindir}/yazi
%{_datadir}/applications/yazi.desktop
%{_datadir}/bash-completion/completions/ya
%{_datadir}/bash-completion/completions/yazi
%{_datadir}/fish/vendor_completions.d/ya.fish
%{_datadir}/fish/vendor_completions.d/yazi.fish
%{_datadir}/pixmaps/yazi.png
%{_datadir}/zsh/site-functions/_ya
%{_datadir}/zsh/site-functions/_yazi

%changelog
%autochangelog
