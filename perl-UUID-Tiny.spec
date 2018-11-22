#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-UUID-Tiny
Version  : 1.04
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/C/CA/CAUGUSTIN/UUID-Tiny-1.04.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CA/CAUGUSTIN/UUID-Tiny-1.04.tar.gz
Summary  : Pure Perl UUID Support With Functional Interface
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

%description
UUID-Tiny Version 1.04
This is a Pure Perl module for the creation of UUIDs:
- version 1 time based (with random multicast MAC address)
- version 3 MD5 based
- version 4 random number based
- version 5 SHA-1 based

%package dev
Summary: dev components for the perl-UUID-Tiny package.
Group: Development
Provides: perl-UUID-Tiny-devel = %{version}-%{release}

%description dev
dev components for the perl-UUID-Tiny package.


%prep
%setup -q -n UUID-Tiny-1.04

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/UUID/Tiny.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/UUID::Tiny.3
