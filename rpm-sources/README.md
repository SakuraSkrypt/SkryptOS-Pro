
## Building Locally

```bash
# Install build dependencies
sudo dnf install -y rpm-build fedora-packager rpmdevtools

# Setup build environment
rpmdev-setuptree

# Build a package
rpmbuild -ba rpm-sources/skryptos-welcome.spec
