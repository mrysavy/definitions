Name:		packer-bin
Version:	0.10.2
Release:	1%{?dist}
Summary:	Packer is a tool for creating machine and container images for multiple platforms from a single source configuration.

License:	MPL2
URL:		https://www.packer.io/
Source0:	https://releases.hashicorp.com/packer/%{version}/packer_%{version}_linux_amd64.zip

ExclusiveArch:  x86_64

%define CHECKSUM 86c78bae6bd09afb4ddb86915cb71a22fb81ea79578bbf65de3ef48c842d9b2b

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

