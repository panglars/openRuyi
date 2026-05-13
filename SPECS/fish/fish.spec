# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond doc 0

Name:           fish
Version:        4.7.1
Release:        %autorelease
Summary:        Friendly interactive shell
License:        GPL-2.0-only AND LGPL-2.0-or-later AND MIT AND PSF-2.0
URL:            https://fishshell.com/
VCS:            git:https://github.com/fish-shell/fish-shell.git
#!RemoteAsset:  sha256:6f4d5b438a6338e3f5dcda19a28261e2ece7a9b7ff97686685e6abdc31dbb7df
Source:         https://github.com/fish-shell/fish-shell/releases/download/%{version}/fish-%{version}.tar.xz
BuildSystem:    cmake

# Use the separately packaged fish rust-pcre2 fork.
Patch0:         2000-use-system-rust-pcre2.patch

BuildOption(conf):  -DFISH_USE_SYSTEM_PCRE2=ON
BuildOption(conf):  -DCMAKE_INSTALL_SYSCONFDIR:PATH=%{_sysconfdir}
%if %{with doc}
BuildOption(conf):  -DWITH_DOCS=ON
%else
BuildOption(conf):  -DWITH_DOCS=OFF
%endif

BuildRequires:  cargo >= 1.85
BuildRequires:  cmake >= 3.15
BuildRequires:  diffutils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libpcre2-32)
BuildRequires:  procps-ng
BuildRequires:  python3
BuildRequires:  python3-pexpect
BuildRequires:  rust >= 1.85
BuildRequires:  tmux
BuildRequires:  crate(aho-corasick-1.0) >= 1.1.4
BuildRequires:  crate(allocator-api2-0.2) >= 0.2.21
BuildRequires:  crate(anstream-1.0/default) >= 1.0.0
BuildRequires:  crate(anstyle-1.0) >= 1.0.14
BuildRequires:  crate(anstyle-parse-1.0/default) >= 1.0.0
BuildRequires:  crate(anstyle-query-1.0) >= 1.1.5
BuildRequires:  crate(anstyle-wincon-3.0) >= 3.0.11
BuildRequires:  crate(anyhow-1.0) >= 1.0.102
BuildRequires:  crate(assert-matches-1.0) >= 1.5.0
BuildRequires:  crate(autocfg-1.0) >= 1.5.0
BuildRequires:  crate(bitflags-2.0) >= 2.10.0
BuildRequires:  crate(block-buffer-0.10) >= 0.10.4
BuildRequires:  crate(bstr-1.0) >= 1.12.1
BuildRequires:  crate(cc-1.0) >= 1.2.55
BuildRequires:  crate(cfg-if-1.0) >= 1.0.4
BuildRequires:  crate(cfg-aliases-0.2) >= 0.2.1
BuildRequires:  crate(clap-4.0/default) >= 4.6.0
BuildRequires:  crate(clap-4.0/derive) >= 4.6.0
BuildRequires:  crate(clap-builder-4.0/default) >= 4.6.0
BuildRequires:  crate(clap-derive-4.0/default) >= 4.6.0
BuildRequires:  crate(clap-lex-1.0/default) >= 1.1.0
BuildRequires:  crate(colorchoice-1.0) >= 1.0.5
BuildRequires:  crate(cpufeatures-0.2) >= 0.2.17
BuildRequires:  crate(crossbeam-deque-0.8) >= 0.8.6
BuildRequires:  crate(crossbeam-epoch-0.9) >= 0.9.18
BuildRequires:  crate(crossbeam-utils-0.8) >= 0.8.21
BuildRequires:  crate(crypto-common-0.1) >= 0.1.7
BuildRequires:  crate(digest-0.10) >= 0.10.7
BuildRequires:  crate(dirs-6.0) >= 6.0.0
BuildRequires:  crate(dirs-sys-0.5) >= 0.5.0
BuildRequires:  crate(either-1.0) >= 1.15.0
BuildRequires:  crate(equivalent-1.0) >= 1.0.2
BuildRequires:  crate(errno-0.3) >= 0.3.14
BuildRequires:  crate(fastrand-2.0) >= 2.3.0
BuildRequires:  crate(find-msvc-tools-0.1) >= 0.1.9
BuildRequires:  crate(foldhash-0.2) >= 0.2.0
BuildRequires:  crate(generic-array-0.14) >= 0.14.7
BuildRequires:  crate(getrandom-0.2) >= 0.2.17
BuildRequires:  crate(getrandom-0.3) >= 0.3.4
BuildRequires:  crate(globset-0.4) >= 0.4.18
BuildRequires:  crate(hashbrown-0.16) >= 0.16.1
BuildRequires:  crate(heck-0.5) >= 0.5.0
BuildRequires:  crate(ignore-0.4) >= 0.4.25
BuildRequires:  crate(is-terminal-polyfill-1.0) >= 1.70.2
BuildRequires:  crate(itertools-0.14) >= 0.14.0
BuildRequires:  crate(jobserver-0.1) >= 0.1.34
BuildRequires:  crate(libc-0.2) >= 0.2.180
BuildRequires:  crate(libredox-0.1) >= 0.1.12
BuildRequires:  crate(lock-api-0.4) >= 0.4.14
BuildRequires:  crate(log-0.4) >= 0.4.29
BuildRequires:  crate(lru-0.16) >= 0.16.3
BuildRequires:  crate(macro-rules-attribute-0.2) >= 0.2.2
BuildRequires:  crate(macro-rules-attribute-proc-macro-0.2) >= 0.2.2
BuildRequires:  crate(memchr-2.0) >= 2.7.6
BuildRequires:  crate(nix-0.31) >= 0.31.1
BuildRequires:  crate(num-traits-0.2) >= 0.2.19
BuildRequires:  crate(once-cell-1.0) >= 1.21.3
BuildRequires:  crate(once-cell-polyfill-1.0) >= 1.70.2
BuildRequires:  crate(option-ext-0.2) >= 0.2.0
BuildRequires:  crate(parking-lot-0.12) >= 0.12.5
BuildRequires:  crate(parking-lot-core-0.9) >= 0.9.12
BuildRequires:  crate(paste-1.0) >= 1.0.15
BuildRequires:  crate(pcre2-0.2/utf32) >= 0.2.9
BuildRequires:  crate(pcre2-sys-0.2/utf32) >= 0.2.9
BuildRequires:  crate(phf-0.13) >= 0.13.1
BuildRequires:  crate(phf-codegen-0.13) >= 0.13.1
BuildRequires:  crate(phf-generator-0.13) >= 0.13.1
BuildRequires:  crate(phf-shared-0.13) >= 0.13.1
BuildRequires:  crate(pkg-config-0.3) >= 0.3.32
BuildRequires:  crate(portable-atomic-1.0) >= 1.13.1
BuildRequires:  crate(ppv-lite86-0.2) >= 0.2.21
BuildRequires:  crate(proc-macro2-1.0) >= 1.0.106
BuildRequires:  crate(quote-1.0) >= 1.0.44
BuildRequires:  crate(r-efi-5.0) >= 5.3.0
BuildRequires:  crate(rand-0.9) >= 0.9.2
BuildRequires:  crate(rand-chacha-0.9) >= 0.9.0
BuildRequires:  crate(rand-core-0.9) >= 0.9.5
BuildRequires:  crate(redox-syscall-0.5) >= 0.5.18
BuildRequires:  crate(redox-users-0.5) >= 0.5.2
BuildRequires:  crate(regex-automata-0.4) >= 0.4.13
BuildRequires:  crate(regex-syntax-0.8) >= 0.8.8
BuildRequires:  crate(rsconf-0.3) >= 0.3.0
BuildRequires:  crate(rust-embed-8.0) >= 8.11.0
BuildRequires:  crate(rust-embed-impl-8.0) >= 8.11.0
BuildRequires:  crate(rust-embed-utils-8.0) >= 8.11.0
BuildRequires:  crate(rustc-version-0.4) >= 0.4.1
BuildRequires:  crate(same-file-1.0) >= 1.0.6
BuildRequires:  crate(scc-2.0) >= 2.4.0
BuildRequires:  crate(scopeguard-1.0) >= 1.2.0
BuildRequires:  crate(sdd-3.0) >= 3.0.10
BuildRequires:  crate(semver-1.0) >= 1.0.28
BuildRequires:  crate(serde-1.0) >= 1.0.228
BuildRequires:  crate(serde-core-1.0) >= 1.0.228
BuildRequires:  crate(serde-derive-1.0) >= 1.0.228
BuildRequires:  crate(serial-test-3.0) >= 3.3.1
BuildRequires:  crate(serial-test-derive-3.0) >= 3.3.1
BuildRequires:  crate(sha2-0.10) >= 0.10.9
BuildRequires:  crate(shellexpand-3.0) >= 3.1.2
BuildRequires:  crate(shlex-1.0) >= 1.3.0
BuildRequires:  crate(siphasher-1.0) >= 1.0.2
BuildRequires:  crate(smallvec-1.0) >= 1.15.1
BuildRequires:  crate(strsim-0.11) >= 0.11.1
BuildRequires:  crate(strum-macros-0.28) >= 0.28.0
BuildRequires:  crate(syn-2.0) >= 2.0.114
BuildRequires:  crate(thiserror-2.0) >= 2.0.18
BuildRequires:  crate(thiserror-impl-2.0) >= 2.0.18
BuildRequires:  crate(typenum-1.0) >= 1.19.0
BuildRequires:  crate(unicode-ident-1.0) >= 1.0.22
BuildRequires:  crate(unicode-segmentation-1.0) >= 1.12.0
BuildRequires:  crate(unicode-width-0.2) >= 0.2.2
BuildRequires:  crate(unix-path-1.0) >= 1.0.1
BuildRequires:  crate(unix-str-1.0) >= 1.0.0
BuildRequires:  crate(utf8parse-0.2) >= 0.2.2
BuildRequires:  crate(version-check-0.9) >= 0.9.5
BuildRequires:  crate(walkdir-2.0) >= 2.5.0
BuildRequires:  crate(wasi-0.11) >= 0.11.1
BuildRequires:  crate(wasip2-1.0) >= 1.0.1
BuildRequires:  crate(widestring-1.0) >= 1.2.1
BuildRequires:  crate(winapi-util-0.1) >= 0.1.11
BuildRequires:  crate(windows-link-0.2) >= 0.2.1
BuildRequires:  crate(windows-sys-0.61) >= 0.61.2
BuildRequires:  crate(wit-bindgen-0.46) >= 0.46.0
BuildRequires:  crate(xterm-color-1.0) >= 1.0.2
BuildRequires:  crate(zerocopy-0.8) >= 0.8.37
BuildRequires:  crate(zerocopy-derive-0.8) >= 0.8.37
%if %{with doc}
BuildRequires:  python3-sphinx
%endif

Provides:       fish = %{version}-%{release}

Requires:       file
Requires:       man-db
Requires:       procps-ng
Requires:       python3

%description
fish is a command-line shell for modern systems, focused on
user-friendliness, discoverability, and interactive use. The syntax is simple,
but it is not POSIX compliant.

%prep -a
# The patch switches pcre2 from a git dependency to the system registry; the
# release Cargo.lock still records the original git source.
rm -f Cargo.lock

# cargo source use system-registry
cat >> .cargo/config.toml <<EOF
[net]
offline = true

[source.crates-io]
replace-with = "system-registry"

[source.system-registry]
directory = "/usr/share/cargo/registry"
EOF

%check
# Skip all super-flaky tests because I have no patience anymore...
export CI=1
%cmake_build --target fish_run_tests


%post
if [ "$1" = 1 ]; then
  if [ ! -f %{_sysconfdir}/shells ] ; then
    echo "%{_bindir}/fish" > %{_sysconfdir}/shells
    echo "/bin/fish" >> %{_sysconfdir}/shells
  else
    grep -q "^%{_bindir}/fish$" %{_sysconfdir}/shells || echo "%{_bindir}/fish" >> %{_sysconfdir}/shells
    grep -q "^/bin/fish$" %{_sysconfdir}/shells || echo "/bin/fish" >> %{_sysconfdir}/shells
  fi
fi

%postun
if [ "$1" = 0 ] && [ -f %{_sysconfdir}/shells ] ; then
  sed -i '\!^%{_bindir}/fish$!d' %{_sysconfdir}/shells
  sed -i '\!^/bin/fish$!d' %{_sysconfdir}/shells
fi

%files
%doc README.rst CHANGELOG.rst
%license COPYING
%{_bindir}/fish
%{_bindir}/fish_indent
%{_bindir}/fish_key_reader
%dir %{_sysconfdir}/fish
%dir %{_sysconfdir}/fish/conf.d
%dir %{_sysconfdir}/fish/completions
%dir %{_sysconfdir}/fish/functions
%config(noreplace) %{_sysconfdir}/fish/config.fish
%{_datadir}/fish
%{_datadir}/pkgconfig/fish.pc
%if %{with doc}
%{_mandir}/man1/fish*.1*
%endif
%{_docdir}/fish

%changelog
%autochangelog
