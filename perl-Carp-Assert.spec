%define upstream_name    Carp-Assert
%define upstream_version 0.21

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Carp::Assert - executable comments
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Carp/%{upstream_name}-%{upstream_version}.tar.gz

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
