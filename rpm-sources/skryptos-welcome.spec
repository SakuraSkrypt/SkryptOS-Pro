Name:           skryptos-welcome
Version:        1.0.0
Release:        1%{?dist}
Summary:        SkryptOS-Pro Welcome and System Information Package
License:        GPL-2.0-or-later
URL:            https://github.com/SakuraSkrypt/SkryptOS-Pro
BuildArch:      noarch

%description
Welcome package for SkryptOS-Pro providing system information and branding.
This package includes the SkryptOS-Pro welcome documentation and system identifiers.

%prep
%build

%install
mkdir -p %{buildroot}/usr/share/doc/skryptos
mkdir -p %{buildroot}/usr/share/pixmaps
mkdir -p %{buildroot}/etc

cat > %{buildroot}/usr/share/doc/skryptos/WELCOME << 'EOF'
╔═══════════════════════════════════════════════════════════════╗
║                 Welcome to SkryptOS-Pro!                      ║
║                                                               ║
║  SkryptOS-Pro is a custom Nobara-based Linux distribution     ║
║  optimized for gaming, development, and multimedia work.      ║
║                                                               ║
║  Repository: https://github.com/SakuraSkrypt/SkryptOS-Pro    ║
║  Documentation: https://github.com/SakuraSkrypt/SkryptOS-Pro ║
╚═══════════════════════════════════════════════════════════════╝

Getting Started:
- Check /usr/share/doc/skryptos/ for documentation
- Visit the GitHub repository for updates and support
- Report issues at: https://github.com/SakuraSkrypt/SkryptOS-Pro/issues

Thank you for using SkryptOS-Pro!
EOF

cat > %{buildroot}/etc/os-release.d/skryptos.conf << 'EOF'
# SkryptOS-Pro System Information
SKRYPTOS_VERSION=1.0.0
SKRYPTOS_RELEASE_DATE=2025-05-21
EOF

%files
/usr/share/doc/skryptos/WELCOME
/etc/os-release.d/skryptos.conf

%changelog
* Thu May 21 2025 SakuraSkrypt <dev@skryptos.local> - 1.0.0-1
- Initial SkryptOS-Pro welcome package
- Added system information files
- Added documentation

%post
echo "SkryptOS-Pro installed successfully!"
cat /usr/share/doc/skryptos/WELCOME

%preun
echo "Removing SkryptOS-Pro welcome package..."
