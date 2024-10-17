%define oname eyeD3

Summary: ID3 tag module
Name:    python-eyed3
Version: 0.7.4
Release: 3
Source0: http://eyed3.nicfit.net/releases/eyeD3-%{version}.tgz
License: GPL
Group: Development/Python
Url: https://eyed3.nicfit.net/
BuildRequires: python-devel
BuildRequires: python-magic
BuildRequires: python-distribute
BuildArch: noarch

# Maybe it would be better to python-magic package (built from 'file')
# to provides pythonegg?
# on the other hand, eyed3 seems to want magic from pypi.org...
%define __noautoreq 'pythonegg\\(python-magic\\)'
Requires: python-magic

%description
eyeD3 is a Python module and program for processing ID3
tags. Information about mp3 files (i.e bit rate, sample frequency,
play time, etc.) is also provided. The formats supported are ID3
v1.0/v1.1 and v2.3/v2.4.

%prep
%setup -q -n %oname-%version

%build
python setup.py build

%install
PYTHONDONTWRITEBYTECODE= python setup.py install --root=%{buildroot} --record=FILE_LIST
sed -i '/egg-info$/d' FILE_LIST

%files -f FILE_LIST
