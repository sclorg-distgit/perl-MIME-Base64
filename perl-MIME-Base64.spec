%{?scl:%scl_package perl-MIME-Base64}

Name:           %{?scl_prefix}perl-MIME-Base64
Version:        3.15
Release:        451%{?dist}
Summary:        Encoding and decoding of Base64 and quoted-printable strings
# Base.xs:      (GPL+ or Artistic) and MIT (Bellcore's part)
# Other files:  GPL+ or Artistic
License:        (GPL+ or Artistic) and MIT
URL:            https://metacpan.org/release/MIME-Base64
Source0:        https://cpan.metacpan.org/authors/id/G/GA/GAAS/MIME-Base64-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl-devel
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl-interpreter
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(vars)
BuildRequires:  %{?scl_prefix}perl(XSLoader)
# Tests:
BuildRequires:  %{?scl_prefix}perl(Encode)
BuildRequires:  %{?scl_prefix}perl(Test)
# Optional tests:
# Perl::API not yet packaged and does not work since perl 5.8.8
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Conflicts:      %{?scl_prefix}perl < 4:5.22.0-347

%description
This package contains a Base64 encoder/decoder and a quoted-printable
encoder/decoder. These encoding methods are specified in RFC 2045 - MIME
(Multipurpose Internet Mail Extensions).

%prep
%setup -q -n MIME-Base64-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE="$RPM_OPT_FLAGS" && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/MIME*
%{_mandir}/man3/*

%changelog
* Fri Dec 20 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.15-451
- SCL

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-439
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.15-438
- Increase release to favour standalone package

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-418
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-417
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.15-416
- Increase release to favour standalone package

* Wed Mar 07 2018 Petr Pisar <ppisar@redhat.com> - 3.15-397
- Modernize spec file

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-396
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-394
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.15-393
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-366
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.15-365
- Increase release to favour standalone package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-349
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 01 2015 Petr Pisar <ppisar@redhat.com> 3.15-348
- Specfile autogenerated by cpanspec 1.78.
