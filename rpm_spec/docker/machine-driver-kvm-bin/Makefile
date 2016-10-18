PROJECT=devops
PACKAGE=docker-machine-driver-kvm-bin
VERSION=0.7.0
RELEASE=1
TARGET=fc24
SPECFILE=${PACKAGE}-${VERSION}.spec
SRPMFILE=${PACKAGE}-${VERSION}-${RELEASE}.${TARGET}.src.rpm

build:
	copr-cli build ${PROJECT} ~/rpmbuild/SRPMS/${SRPMFILE}

create:
	copr-cli create --chroot fedora-24-x86_64 --enable-net on ${PROJECT}

srpm:
	spectool -gf -R ${SPECFILE}
	rpmbuild -bs ${SPECFILE}

