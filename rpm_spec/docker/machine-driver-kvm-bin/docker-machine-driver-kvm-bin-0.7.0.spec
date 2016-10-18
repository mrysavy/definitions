Name:		docker-machine-driver-kvm-bin
Version:	0.7.0
Release:	1%{?dist}
Summary:	KVM driver for docker-machine

License:	MPL2
URL:		https://github.com/dhiltgen/docker-machine-kvm
Source0:	https://github.com/dhiltgen/docker-machine-kvm/releases/download/v%{version}/docker-machine-driver-kvm

ExclusiveArch:  x86_64

%define CHECKSUM 519d29300df740a73c90d048e5df43fb

%description

%prep
echo %{CHECKSUM} %{SOURCE0} | md5sum -c
%setup -c -T
cp %{SOURCE0} ./docker-machine-driver-kvm

%install
install -D -m 755 docker-machine-driver-kvm $RPM_BUILD_ROOT/usr/bin/docker-machine-driver-kvm

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/bin/docker-machine-driver-kvm
%doc



%changelog

