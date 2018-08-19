#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtconsole
Version  : 4.4.1
Release  : 23
URL      : https://files.pythonhosted.org/packages/e4/6d/5af06751ece05ff0892dd02ce043062bc2d8f426f91894876f669a70ef1b/qtconsole-4.4.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/e4/6d/5af06751ece05ff0892dd02ce043062bc2d8f426f91894876f669a70ef1b/qtconsole-4.4.1.tar.gz
Summary  : Jupyter Qt console
Group    : Development/Tools
License  : BSD-3-Clause
Requires: qtconsole-bin
Requires: qtconsole-python3
Requires: qtconsole-license
Requires: qtconsole-python
BuildRequires : buildreq-distutils3

%description
# Jupyter Qt Console
[![Google Group](https://img.shields.io/badge/-Google%20Group-lightgrey.svg)](https://groups.google.com/forum/#!forum/jupyter)
[![Build Status](https://travis-ci.org/jupyter/qtconsole.svg?branch=master)](https://travis-ci.org/jupyter/qtconsole)
[![Coverage Status](https://coveralls.io/repos/github/jupyter/qtconsole/badge.svg?branch=master)](https://coveralls.io/github/jupyter/qtconsole?branch=master)
[![Documentation Status](https://readthedocs.org/projects/qtconsole/badge/?version=stable)](https://qtconsole.readthedocs.io/en/stable/)

%package bin
Summary: bin components for the qtconsole package.
Group: Binaries
Requires: qtconsole-license

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
Requires: qtconsole-python3

%description python
python components for the qtconsole package.


%package python3
Summary: python3 components for the qtconsole package.
Group: Default
Requires: python3-core

%description python3
python3 components for the qtconsole package.


%prep
%setup -q -n qtconsole-4.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534700218
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/qtconsole
cp LICENSE %{buildroot}/usr/share/doc/qtconsole/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jupyter-qtconsole

%files license
%defattr(-,root,root,-)
/usr/share/doc/qtconsole/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
