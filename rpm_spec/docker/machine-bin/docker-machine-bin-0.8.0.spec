Name:		docker-machine-bin
Version:	0.8.0
Release:	1%{?dist}
Summary:	Machine management for a container-centric world

License:	MPL2
URL:		https://docs.docker.com/machine/
Source0:	https://github.com/docker/machine/releases/download/v%{version}/docker-machine-linux-x86_64

ExclusiveArch:  x86_64

%define CHECKSUM 326ce856238b1f906278ee1a12409f9206a95f40e8c3a97adfc746006378f495

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

