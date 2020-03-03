#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : padatious
Version  : 0.4.7
Release  : 9
URL      : https://files.pythonhosted.org/packages/33/c1/a54ac3f8fe5fac7fc9537beb90576673a660f3da9147e1317adf6e4c3cfb/padatious-0.4.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/33/c1/a54ac3f8fe5fac7fc9537beb90576673a660f3da9147e1317adf6e4c3cfb/padatious-0.4.7.tar.gz
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
# Padatious #
An efficient and agile neural network intent parser
### Features ###

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

%description python3
python3 components for the padatious package.


%prep
%setup -q -n padatious-0.4.7
cd %{_builddir}/padatious-0.4.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583196533
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
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
