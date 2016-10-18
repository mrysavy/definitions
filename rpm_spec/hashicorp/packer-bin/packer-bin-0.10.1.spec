Name:		packer-bin
Version:	0.10.1
Release:	1%{?dist}
Summary:	Packer is a tool for creating machine and container images for multiple platforms from a single source configuration.

License:	MPL2
URL:		https://www.packer.io/
Source0:	https://releases.hashicorp.com/packer/%{version}/packer_%{version}_linux_amd64.zip

ExclusiveArch:  x86_64

%define CHECKSUM 7d51fc5db19d02bbf32278a8116830fae33a3f9bd4440a58d23ad7c863e92e28

%description

%prep
echo %{CHECKSUM} %{SOURCE0} | sha256sum -c
# Copr tries to untar instead of unzip
%setup -c -T
/usr/bin/unzip %{SOURCE0}

%install
install -D -m 755 packer $RPM_BUILD_ROOT/usr/bin/packer

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/bin/packer
%doc



%changelog

