Name:		docker-compose-bin
Version:	1.8.1
Release:	1%{?dist}
Summary:	Define and run multi-container applications with Docker

License:	MPL2
URL:		https://docs.docker.com/compose/
Source0:	https://github.com/docker/compose/releases/download/%{version}/docker-compose-Linux-x86_64

ExclusiveArch:  x86_64

%global __strip /bin/true

%define CHECKSUM d9c19bfd39ccd8bf7168c2afefb6a2cbd77d299c4d61531a220f6803ec6b701a

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

