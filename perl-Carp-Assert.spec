%define upstream_name    Carp-Assert
Name:		perl-%{upstream_name}
Version:	0.21
Release:	4

Summary:	Carp::Assert - executable comments
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Carp/%{upstream_name}-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Test::Inline)
BuildRequires:	perl(Test::More) >= 0.40
BuildArch:	noarch

%description
Carp::Assert is intended for a purpose like the ANSI C library assert.h.
If you're already familiar with assert.h, then you can probably skip
this and go straight to the FUNCTIONS section.

%prep
%setup -q -n %{upstream_name}-%{version}

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
