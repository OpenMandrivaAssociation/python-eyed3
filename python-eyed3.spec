%define name python-eyed3
%define version 0.6.17
%define oname eyeD3
%define release %mkrel 4

Summary: ID3 tag module
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://eyed3.nicfit.net/releases/%{oname}-%{version}.tar.gz
License: GPL
Group: Development/Python
Url: http://eyed3.nicfit.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
%py_requires -d
BuildArch: noarch

%description
eyeD3 is a Python module and program for processing ID3
tags. Information about mp3 files (i.e bit rate, sample frequency,
play time, etc.) is also provided. The formats supported are ID3
v1.0/v1.1 and v2.3/v2.4.

%prep
%setup -q -n %oname-%version

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT installed-docs
%makeinstall
mv %buildroot%_datadir/doc/%oname-%version installed-docs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc installed-docs/*
%py_puresitedir/%oname
%py_puresitedir/*.egg-info
%_bindir/%oname
%_mandir/man1/%oname.1*


