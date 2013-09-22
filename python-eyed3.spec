%define oname eyeD3

Summary: ID3 tag module
Name:    python-eyed3
Version: 0.7.3
Release: 1
Source0: http://eyed3.nicfit.net/releases/eyeD3-%{version}.tgz
License: GPL
Group: Development/Python
Url: http://eyed3.nicfit.net/
BuildRequires: python-devel
BuildArch: noarch

%description
eyeD3 is a Python module and program for processing ID3
tags. Information about mp3 files (i.e bit rate, sample frequency,
play time, etc.) is also provided. The formats supported are ID3
v1.0/v1.1 and v2.3/v2.4.

%prep
%setup -q -n %oname-%version

%build
%{__python} setup.py build

%install
PYTHONDONTWRITEBYTECODE= %{__python} setup.py install --root=%{buildroot} --record=FILE_LIST

%files -f FILE_LIST



%changelog
* Sun Nov 27 2011 Götz Waschk <waschk@mandriva.org> 0.6.18-1mdv2012.0
+ Revision: 733753
- new version

* Mon Oct 31 2011 Götz Waschk <waschk@mandriva.org> 0.6.17-4
+ Revision: 707978
- rebuild

* Sat Oct 30 2010 Michael Scherer <misc@mandriva.org> 0.6.17-3mdv2011.0
+ Revision: 590614
- rebuild for python 2.7

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.6.17-2mdv2011.0
+ Revision: 442104
- rebuild

* Tue Feb 03 2009 Götz Waschk <waschk@mandriva.org> 0.6.17-1mdv2009.1
+ Revision: 336812
- update to new version 0.6.17

* Fri Dec 26 2008 Funda Wang <fwang@mandriva.org> 0.6.16-3mdv2009.1
+ Revision: 319380
- rebuild for new python

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.6.16-2mdv2009.0
+ Revision: 265542
- rebuild early 2009.0 package (before pixel changes)

* Tue Jun 10 2008 Götz Waschk <waschk@mandriva.org> 0.6.16-1mdv2009.0
+ Revision: 217381
- new version

* Mon May 05 2008 Götz Waschk <waschk@mandriva.org> 0.6.15-1mdv2009.0
+ Revision: 201277
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed May 02 2007 Götz Waschk <waschk@mandriva.org> 0.6.13-1mdv2008.0
+ Revision: 20407
- new version


* Mon Feb 19 2007 Götz Waschk <waschk@mandriva.org> 0.6.12-1mdv2007.0
+ Revision: 122645
- new version

* Mon Dec 04 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.6.11-2mdv2007.1
+ Revision: 90583
- Rebuild against new python

* Mon Nov 06 2006 Götz Waschk <waschk@mandriva.org> 0.6.11-1mdv2007.1
+ Revision: 76840
- new version

* Thu Nov 02 2006 Götz Waschk <waschk@mandriva.org> 0.6.10-1mdv2007.1
+ Revision: 75191
- Import python-eyed3

* Thu Nov 02 2006 Götz Waschk <waschk@mandriva.org> 0.6.10-1mdv2007.1
- New version 0.6.10

* Tue Aug 01 2006 Götz Waschk <waschk@mandriva.org> 0.6.7-1mdv2007.0
- Rebuild

* Fri Apr 21 2006 Götz Waschk <waschk@mandriva.org> 0.6.7-2mdk
- use python macros
- use mkrel

* Mon Aug 29 2005 Götz Waschk <waschk@mandriva.org> 0.6.7-1mdk
- New release 0.6.7

* Fri Aug 12 2005 Götz Waschk <waschk@mandriva.org> 0.6.6-1mdk
- initial package


