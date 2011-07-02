
%define		module	dns

%define snapshot 20110611

Summary:	dnspython - a DNS toolkit for Python
Summary(pl.UTF-8):	dnspython - zestaw narzędzi do DNS dla Pythona
Name:		python3-%{module}
Version:	1.9.5
Release:	0.%{snapshot}
License:	MIT
Group:		Development/Languages/Python
Source0:	dnspython3-%{version}-%{snapshot}.tar.gz
# Source0-md5:	74c6e72c6580a97a324f8f3cb894c83a
URL:		http://www.dnspython.org/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dnspython is a DNS toolkit for Python. It supports almost all record
types. It can be used for queries, zone transfers, and dynamic
updates. It supports TSIG authenticated messages and EDNS0.

dnspython provides both high and low level access to DNS. The high
level classes perform queries for data of a given name, type, and
class, and return an answer set. The low level classes allow direct
manipulation of DNS zones, messages, names, and records.

%description -l pl.UTF-8
dnspython to zestaw narzędzi do DNS dla Pythona. Obsługuje prawie
wszystkie rodzaje rekordów. Może być używany do zapytań, transferów
stref oraz dynamicznych uaktualnień. Obsługuje uwierzytelnione
komunikaty TSIG oraz EDNS0.

dnspython dostarcza zarówno wysoko- jak i niskopoziomowy dostęp do
DNS-a. Klasy wysokopoziomowe wykonują zapytania o dane dla podanej
nazwy, rodzaju i klasy, a zwracają zbiór odpowiedzi. Klasy
niskopoziomowe umożliwiają bezpośrednie manipulacje na strefach,
komunikatach, nazwach i rekordach w DNS-ie.

%prep
%setup -q -n dnspython3-%{version}

%build
%{__python3} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__python3} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README TODO
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/*.egg-info
%{_examplesdir}/%{name}-%{version}
