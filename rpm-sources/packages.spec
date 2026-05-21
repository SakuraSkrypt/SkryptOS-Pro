# rpm-sources/example.spec
Name:           skryptos-welcome
Version:        1.0.0
Release:        1%{?dist}
Summary:        SkryptOS Welcome Package

License:        GPL2
BuildArch:      x86_64

%description
Welcome package for SkryptOS

%prep
%build
%install
mkdir -p %{buildroot}/usr/share/doc
echo "Welcome to SkryptOS" > %{buildroot}/usr/share/doc/WELCOME

%files
/usr/share/doc/WELCOME

%changelog
* Thu May 21 2025 SkryptOS <dev@skryptos.local> - 1.0.0-1
- Initial release
