# Generated by rust2rpm 13
%bcond_without check

%global crate starship

Name:           rust-%{crate}
Version:        0.32.1
Release:        2%{?dist}
Summary:        Cross-shell prompt for astronauts

# Upstream license specification: ISC
License:        ISC
URL:            https://crates.io/crates/starship
Source:         %{crates_source}
# Initial patched metadata
# * Use default features (OpenSSL) for reqwest, essentially revert of https://github.com/starship/starship/commit/d1b725a47cda1047546fb3998ff8f8a61ed4a48b
Patch0:         starship-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Cross-shell prompt for astronauts. ☄🌌️.}

%description %{_description}

%if ! %{__cargo_skip_build}
%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%doc README.md
%{_bindir}/starship
%endif

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md CONTRIBUTING.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+battery-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+battery-devel %{_description}

This package contains library source intended for building other packages
which use "battery" feature of "%{crate}" crate.

%files       -n %{name}+battery-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
# https://github.com/starship/starship/issues/755
sed -i -e '/EXE_PATH/s|/debug/|/release/|' tests/testsuite/common.rs
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
%if %{with check}
echo 'git-core'
%endif

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 26 08:19:53 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.32.1-1
- Update to 0.32.1

* Thu Dec 19 14:06:54 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.30.1-3
- Run tests

* Fri Dec 13 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.30.1-2
- Update to 0.30.1

* Fri Dec 13 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.29.0-1
- Update to 0.29.0

* Wed Dec 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.27.0-1
- Update to 0.27.0

* Thu Nov 28 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.26.5-1
- Update to 0.26.5

* Mon Nov 25 10:54:30 EET 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.26.4-1
- Initial package
