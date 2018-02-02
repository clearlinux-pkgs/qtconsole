#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtconsole
Version  : 4.3.1
Release  : 11
URL      : http://pypi.debian.net/qtconsole/qtconsole-4.3.1.tar.gz
Source0  : http://pypi.debian.net/qtconsole/qtconsole-4.3.1.tar.gz
Summary  : Jupyter Qt console
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: qtconsole-bin
Requires: qtconsole-python3
Requires: qtconsole-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
# Jupyter Qt Console
[![Google Group](https://img.shields.io/badge/-Google%20Group-lightgrey.svg)](https://groups.google.com/forum/#!forum/jupyter)
[![Build Status](https://travis-ci.org/jupyter/qtconsole.svg?branch=master)](https://travis-ci.org/jupyter/qtconsole)
[![Documentation Status](https://readthedocs.org/projects/qtconsole/badge/?version=stable)](https://qtconsole.readthedocs.io/en/stable/)

%package bin
Summary: bin components for the qtconsole package.
Group: Binaries

%description bin
bin components for the qtconsole package.


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
%setup -q -n qtconsole-4.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507171199
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jupyter-qtconsole

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
