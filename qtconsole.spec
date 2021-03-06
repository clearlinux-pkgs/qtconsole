#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtconsole
Version  : 5.1.1
Release  : 61
URL      : https://files.pythonhosted.org/packages/f0/31/273a6c7c612186ddfaa19967466802938a0e350a51be399818100377b5ad/qtconsole-5.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/f0/31/273a6c7c612186ddfaa19967466802938a0e350a51be399818100377b5ad/qtconsole-5.1.1.tar.gz
Summary  : Jupyter Qt console
Group    : Development/Tools
License  : BSD-3-Clause
Requires: qtconsole-bin = %{version}-%{release}
Requires: qtconsole-license = %{version}-%{release}
Requires: qtconsole-python = %{version}-%{release}
Requires: qtconsole-python3 = %{version}-%{release}
Requires: Pygments
Requires: QtPy
Requires: ipykernel
Requires: ipython_genutils
Requires: jupyter_client
Requires: jupyter_core
Requires: pyzmq
Requires: traitlets
BuildRequires : Pygments
BuildRequires : QtPy
BuildRequires : buildreq-distutils3
BuildRequires : ipykernel
BuildRequires : ipython_genutils
BuildRequires : jupyter_client
BuildRequires : jupyter_core
BuildRequires : pyzmq
BuildRequires : traitlets

%description
# Jupyter QtConsole
![Windows tests](https://github.com/jupyter/qtconsole/workflows/Windows%20tests/badge.svg)
![Macos tests](https://github.com/jupyter/qtconsole/workflows/Macos%20tests/badge.svg)
![Linux tests](https://github.com/jupyter/qtconsole/workflows/Linux%20tests/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/jupyter/qtconsole/badge.svg?branch=master)](https://coveralls.io/github/jupyter/qtconsole?branch=master)
[![Documentation Status](https://readthedocs.org/projects/qtconsole/badge/?version=stable)](https://qtconsole.readthedocs.io/en/stable/)
[![Google Group](https://img.shields.io/badge/-Google%20Group-lightgrey.svg)](https://groups.google.com/forum/#!forum/jupyter)

%package bin
Summary: bin components for the qtconsole package.
Group: Binaries
Requires: qtconsole-license = %{version}-%{release}

%description bin
bin components for the qtconsole package.


%package license
Summary: license components for the qtconsole package.
Group: Default

%description license
license components for the qtconsole package.


%package python
Summary: python components for the qtconsole package.
Group: Default
Requires: qtconsole-python3 = %{version}-%{release}

%description python
python components for the qtconsole package.


%package python3
Summary: python3 components for the qtconsole package.
Group: Default
Requires: python3-core
Provides: pypi(qtconsole)
Requires: pypi(ipykernel)
Requires: pypi(ipython_genutils)
Requires: pypi(jupyter_client)
Requires: pypi(jupyter_core)
Requires: pypi(pygments)
Requires: pypi(pyzmq)
Requires: pypi(qtpy)
Requires: pypi(traitlets)

%description python3
python3 components for the qtconsole package.


%prep
%setup -q -n qtconsole-5.1.1
cd %{_builddir}/qtconsole-5.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1625065189
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qtconsole
cp %{_builddir}/qtconsole-5.1.1/LICENSE %{buildroot}/usr/share/package-licenses/qtconsole/6b85326e6a68c099bbfa0e2c7d5ca15aa9763753
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jupyter-qtconsole

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qtconsole/6b85326e6a68c099bbfa0e2c7d5ca15aa9763753

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
