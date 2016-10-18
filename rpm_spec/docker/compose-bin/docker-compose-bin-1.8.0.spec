Name:		docker-compose-bin
Version:	1.8.0
Release:	1%{?dist}
Summary:	Define and run multi-container applications with Docker

License:	MPL2
URL:		https://docs.docker.com/compose/
Source0:	https://github.com/docker/compose/releases/download/%{version}/docker-compose-Linux-x86_64

ExclusiveArch:  x86_64

%global __strip /bin/true

%define CHECKSUM ebc6ab9ed9c971af7efec074cff7752593559496d0d5f7afb6bfd0e0310961ff

%description

%prep
echo %{CHECKSUM} %{SOURCE0} | sha256sum -c
%setup -c -T
cp %{SOURCE0} ./docker-compose

%install
install -D -m 755 docker-compose $RPM_BUILD_ROOT/usr/bin/docker-compose

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/bin/docker-compose
%doc



%changelog

