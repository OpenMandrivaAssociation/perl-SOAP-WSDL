%define module   SOAP-WSDL
%define version    2.00.05
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    SOAP with WSDL support
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/SOAP/%{module}-%{version}.tar.gz
BuildRequires: perl(Class::Std::Fast)
BuildRequires: perl(Cwd)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Date::Format)
BuildRequires: perl(Date::Parse)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(List::Util)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Storable)
BuildRequires: perl(Template)
BuildRequires: perl(Term::ReadKey)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI)
BuildRequires: perl(XML::Parser::Expat)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
SOAP::WSDL provides easy access to Web Services with WSDL descriptions.

The WSDL is parsed and stored in memory.

Your data is serialized according to the rules in the WSDL.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README LICENSE Changes README
%{_bindir}/wsdl2perl.pl
%{_mandir}/man3/*
%{_mandir}/man1/*
%{perl_vendorlib}/SOAP

