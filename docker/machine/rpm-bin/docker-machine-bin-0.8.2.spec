Name:		docker-machine-bin
Version:	0.8.2
Release:	1%{?dist}
Summary:	Machine management for a container-centric world

License:	MPL2
URL:		https://docs.docker.com/machine/
Source0:	https://github.com/docker/machine/releases/download/v%{version}/docker-machine-linux-x86_64

ExclusiveArch:  x86_64

%define CHECKSUM e5c3e360b46a82d4bc5ff2efe357b15040cfc58d3d962f793fee6ee1e44e9b66

%description

%prep
echo %{CHECKSUM} %{SOURCE0} | sha256sum -c
%setup -c -T
cp %{SOURCE0} ./docker-machine

%install
install -D -m 755 docker-machine $RPM_BUILD_ROOT/usr/bin/docker-machine

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/bin/docker-machine
%doc



%changelog

