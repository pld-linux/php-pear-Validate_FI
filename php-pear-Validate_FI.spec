%include	/usr/lib/rpm/macros.php
%define		_class		Validate
%define		_subclass	FI
%define		_status		beta
%define		_pearname	Validate_FI
Summary:	%{_pearname} - Validation class for Finland
Summary(pl.UTF-8):	%{_pearname} - klasa sprawdzająca poprawość dla Finlandii
Name:		php-pear-%{_pearname}
Version:	0.4.0
Release:	1
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	6de4fcaa54f47f364747ffa1e4c72694
URL:		http://pear.php.net/package/Validate_FI/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package containes locale validation for Finland such as:
 - Postal Code
 - Telephone Number
 - Car License Plate Number
 - Motorbike License Plate Number
 - Personal Identity Number (HETU)
 - Unique Identification Number (SATU)
 - Business ID Number (Y-tunnus)
 - Party Identification Number (OVT-tunnus)
 - Value Added Tax Number (ALV-numero)
 - Bank Account Number (tilinumero)
 - Bank Reference Number (viitenumero)
 - Credit Card Number

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet do sprawdzania poprawności dla Finlandii danych takich jak:
 - kod pocztowy,
 - numer telefoniczny,
 - numer rejestracyjny,
 - osobisty numer identyfikacyjny (HETU),
 - unikalny numer identyfikacyjny (SATU),
 - numer identyfikacji biznesowej (Y-tunnus),
 - numer identyfikacyjny produktu (OVT-tunnus),
 - numer podatku od wartości dodanej (ALV-numero),
 - numer konta bankowego (tilinumero),
 - numer referencyjny banku (viitenumero),
 - numer karty kredytowej.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Validate/FI.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Validate_FI/tests
