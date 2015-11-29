
%define		module	dns

Summary:	dnspython3 - a DNS toolkit for Python 3
Summary(pl.UTF-8):	dnspython3 - zestaw narzędzi do DNS dla Pythona 3
Name:		python3-%{module}
Version:	1.11.1
Release:	4
License:	MIT
Group:		Development/Languages/Python
Source0:	http://www.dnspython.org/kits3/%{version}/dnspython3-%{version}.tar.gz
# Source0-md5:	c0203410e1405c3ee1d70dafa4ad6612
URL:		http://www.dnspython.org/
BuildRequires:	python3-devel >= 3.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dnspython3 is a DNS toolkit for Python 3. It supports almost all
record types. It can be used for queries, zone transfers, and dynamic
updates. It supports TSIG authenticated messages and EDNS0.

dnspython3 provides both high and low level access to DNS. The high
level classes perform queries for data of a given name, type, and
class, and return an answer set. The low level classes allow direct
manipulation of DNS zones, messages, names, and records.

%description -l pl.UTF-8
dnspython3 to zestaw narzędzi do DNS dla Pythona 3. Obsługuje prawie
wszystkie rodzaje rekordów. Może być używany do zapytań, transferów
stref oraz dynamicznych uaktualnień. Obsługuje uwierzytelnione
komunikaty TSIG oraz EDNS0.

dnspython3 dostarcza zarówno wysoko- jak i niskopoziomowy dostęp do
DNS-a. Klasy wysokopoziomowe wykonują zapytania o dane dla podanej
nazwy, rodzaju i klasy, a zwracają zbiór odpowiedzi. Klasy
niskopoziomowe umożliwiają bezpośrednie manipulacje na strefach,
komunikatach, nazwach i rekordach w DNS-ie.

%prep
%setup -q -n dnspython3-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/*.egg-info
%{_examplesdir}/%{name}-%{version}
