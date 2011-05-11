#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	CGI
%define		pnam	PSGI
%include	/usr/lib/rpm/macros.perl
Summary:	CGI::PSGI - Adapt CGI.pm to the PSGI protocol
#Summary(pl.UTF-8):	
Name:		perl-CGI-PSGI
Version:	0.14
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CGI/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	31d2bd2cd3b4d0ae196e93e11e7fd98f
# generic URL, check or change before uncommenting
#URL:		http://search.cpan.org/dist/CGI-PSGI/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is for web application framework developers who currently uses
CGI to handle query parameters, and would like for the frameworks to comply
with the PSGI protocol.

Only slight modifications should be required if the framework is already
collecting the body content to print to STDOUT at one place (rather using
the print-as-you-go approach).

On the other hand, if you are an "end user" of CGI.pm and have a CGI script
that you want to run under PSGI web servers, this module might not be what you
want.  Take a look at CGI::Emulate::PSGI instead.

Your application, typically the web application framework adapter
should update the code to do CGI::PSGI->new($env) instead of
CGI->new to create a new CGI object. (This is similar to how
CGI::Fast object is initialized in a FastCGI environment.)



# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/CGI/*.pm
%{_mandir}/man3/*
