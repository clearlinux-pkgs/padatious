#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : padatious
Version  : 0.4.8
Release  : 11
URL      : https://files.pythonhosted.org/packages/d0/e7/70a6eb34b7e67fef5b2645df2ee1f807db2b5a345e4e6adfb2660a56425b/padatious-0.4.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/d0/e7/70a6eb34b7e67fef5b2645df2ee1f807db2b5a345e4e6adfb2660a56425b/padatious-0.4.8.tar.gz
Summary  : A neural network intent parser
Group    : Development/Tools
License  : Apache-2.0
Requires: padatious-bin = %{version}-%{release}
Requires: padatious-python = %{version}-%{release}
Requires: padatious-python3 = %{version}-%{release}
Requires: fann2
Requires: padaos
BuildRequires : buildreq-distutils3
BuildRequires : fann2
BuildRequires : padaos

%description
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE.md) [![CLA](https://img.shields.io/badge/CLA%3F-Required-blue.svg)](https://mycroft.ai/cla) [![Team](https://img.shields.io/badge/Team-Mycroft_Core-violetblue.svg)](https://github.com/MycroftAI/contributors/blob/master/team/Mycroft%20Core.md) ![Status](https://img.shields.io/badge/-Production_ready-green.svg)

%package bin
Summary: bin components for the padatious package.
Group: Binaries

%description bin
bin components for the padatious package.


%package python
Summary: python components for the padatious package.
Group: Default
Requires: padatious-python3 = %{version}-%{release}

%description python
python components for the padatious package.


%package python3
Summary: python3 components for the padatious package.
Group: Default
Requires: python3-core
Provides: pypi(padatious)
Requires: pypi(fann2)
Requires: pypi(padaos)
Requires: pypi(xxhash)

%description python3
python3 components for the padatious package.


%prep
%setup -q -n padatious-0.4.8
cd %{_builddir}/padatious-0.4.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1590517146
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/padatious

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
