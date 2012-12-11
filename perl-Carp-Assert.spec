%define upstream_name    Carp-Assert
%define	upstream_version 0.20

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Carp::Assert - executable comments
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Carp/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Test::Inline)
BuildRequires:	perl(Test::More) >= 0.40
BuildArch:	noarch

%description
Carp::Assert is intended for a purpose like the ANSI C library assert.h.
If you're already familiar with assert.h, then you can probably skip
this and go straight to the FUNCTIONS section.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Carp
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.200.0-2mdv2011.0
+ Revision: 680714
- mass rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.200.0-1mdv2011.0
+ Revision: 406257
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.20-3mdv2009.0
+ Revision: 255477
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.20-1mdv2008.1
+ Revision: 136666
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Apr 30 2007 Olivier Thauvin <nanardon@mandriva.org> 0.20-1mdv2008.0
+ Revision: 19682
- fix build

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    -New version


* Fri Aug 04 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-04 18:26:41 (52733)
- import perl-Carp-Assert-0.18-2mdv2007.0

* Fri Aug 04 2006 Scott Karns <scottk@mandriva.org> 0.18-2mdv2007.0
- Rebuild
- Updated to comply with Mandriva perl packaging policies

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.18-1mdk
- initial Mandriva package

