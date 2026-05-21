# SkryptOS-Pro RPM Sources

This directory contains RPM spec files and sources for building SkryptOS-Pro packages.

## Repository Structure

rpm-sources/ ├── *.spec # RPM spec files ├── *.tar.gz # Source tarballs (if needed) └── README.md # This file

## Building Locally

```bash
# Install build dependencies
sudo dnf install -y rpm-build fedora-packager rpmdevtools

# Setup build environment
rpmdev-setuptree

# Build a package
rpmbuild -ba rpm-sources/skryptos-welcome.spec
