# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond check 1

%global commit 8ed0da44d974c32c6877d2f4630c314da0717ecb
%global commit_short 8ed0da4

Name:           niri
Version:        26.04
Release:        %autorelease
Summary:        Scrollable-tiling Wayland compositor
License:        GPL-3.0-or-later
URL:            https://niri-wm.github.io/niri/
VCS:            git:https://github.com/niri-wm/niri.git
#!RemoteAsset:  sha256:134c602d8e0d53413a52d6cd58f9ce7e79a07d03288ee0a51ba1abd5db1b1ad9
Source0:        https://github.com/niri-wm/niri/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
#!RemoteAsset:  sha256:407c525cd78710e72455c48741756857ca47dc32910a42f82cd40992a34beed6
Source1:        https://github.com/niri-wm/niri/releases/download/v%{version}/%{name}-%{version}-vendored-dependencies.tar.xz
BuildSystem:    rust

BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig
BuildRequires:  bash-completion
BuildRequires:  clang
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libspa-0.2)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkeyboard-config)

Requires:       wayland
Requires:       xkeyboard-config

# required for portal support
# Recommends:     gnome-keyring
# Recommends:     xdg-desktop-portal-gnome
# Recommends:     xdg-desktop-portal-gtk

# applications bound by keyboard shortcuts in default configuration
# Recommends:     alacritty
# Recommends:     swaylock

%description
niri is a scrollable-tiling Wayland compositor. Windows are arranged in
columns on an infinite strip that extends horizontally.

%prep -a
tar xf %{SOURCE1}
mkdir -p .cargo
# use upstream vendor
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/Smithay/smithay.git?rev=ff5fa7df392cecfba049ffed55cdaa4e98a8e7ef"]
git = "https://github.com/Smithay/smithay.git"
rev = "ff5fa7df392cecfba049ffed55cdaa4e98a8e7ef"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
export NIRI_BUILD_COMMIT=%{commit_short}
cargo build --release --locked --offline --features default

target/release/niri completions bash > niri.bash
target/release/niri completions fish > niri.fish
target/release/niri completions zsh > _niri

%install
install -Dm0755 target/release/niri %{buildroot}%{_bindir}/niri
install -Dm0755 resources/niri-session %{buildroot}%{_bindir}/niri-session
install -Dm0644 resources/niri.desktop %{buildroot}%{_datadir}/wayland-sessions/niri.desktop
install -Dm0644 resources/niri-portals.conf %{buildroot}%{_datadir}/xdg-desktop-portal/niri-portals.conf
install -Dm0644 resources/niri.service %{buildroot}%{_userunitdir}/niri.service
install -Dm0644 resources/niri-shutdown.target %{buildroot}%{_userunitdir}/niri-shutdown.target

install -Dm0644 niri.bash %{buildroot}%{bash_completions_dir}/niri
install -Dm0644 niri.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/niri.fish
install -Dm0644 _niri %{buildroot}%{_datadir}/zsh/site-functions/_niri

%if %{with check}
%check
# limit test parallelism
export RAYON_NUM_THREADS=1
# skip tests that require a running session or EGL display
check_args=(--test-threads 1 --skip ::egl)
%ifarch riscv64
check_args+=(--skip tests::window_opening::target_output_and_workspaces)
%endif
cargo test --locked --offline --workspace --exclude niri-visual-tests --features default --jobs 1 -- "${check_args[@]}"
%endif

%post
%systemd_user_post niri.service

%preun
%systemd_user_preun niri.service

%files
%doc README.md
%license LICENSE
%{_bindir}/niri
%{_bindir}/niri-session
%{_datadir}/wayland-sessions/niri.desktop
%{_datadir}/xdg-desktop-portal/niri-portals.conf
%{_userunitdir}/niri.service
%{_userunitdir}/niri-shutdown.target
%{bash_completions_dir}/niri
%{_datadir}/fish/vendor_completions.d/niri.fish
%{_datadir}/zsh/site-functions/_niri

%changelog
%autochangelog
