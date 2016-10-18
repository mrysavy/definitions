Name:		habitus-bin
Version:	0.4.5
Release:	1%{?dist}
Summary:	Habitus is a standalone build flow tool for Docker

License:	MPL2
URL:		https://www.habitus.io/
Source0:	https://github.com/cloud66/habitus/releases/download/v%{version}/habitus_linux_amd64

ExclusiveArch:  x86_64

%define CHECKSUM 9578a0c95b02ec6fbaf1ff99e9d7378108eee5f91f63f3190365b9b85792247e

%description

%prep
echo %{CHECKSUM} %{SOURCE0} | sha256sum -c
%setup -c -T
cp %{SOURCE0} ./habitus

%install
install -D -m 755 habitus $RPM_BUILD_ROOT/usr/bin/habitus

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/bin/habitus
%doc



%changelog

