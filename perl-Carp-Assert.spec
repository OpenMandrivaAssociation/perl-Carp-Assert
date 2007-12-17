%define realname Carp-Assert
%define	name	perl-%{realname}
%define modprefix Carp

%define	version	0.20
%define	release	%mkrel 1

Summary:	Carp::Assert - executable comments
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{realname}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Test::Inline)
BuildRequires:	perl(Test::More) >= 0.40
BuildArch:	noarch

%description
Carp::Assert is intended for a purpose like the ANSI C library assert.h.
If you're already familiar with assert.h, then you can probably skip
this and go straight to the FUNCTIONS section.

%prep
%setup -q -n %{realname}-%{version} 

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%__make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/%{modprefix}
%{_mandir}/*/*

