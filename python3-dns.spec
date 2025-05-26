#
# Conditional build:
%bcond_without	tests	# unit tests

%define		module	dns
Summary:	dnspython - a DNS toolkit for Python 3
Summary(pl.UTF-8):	dnspython - zestaw narzędzi do DNS dla Pythona 3
Name:		python3-%{module}
Version:	2.7.0
Release:	1
License:	MIT
Group:		Development/Languages/Python
Source0:	https://files.pythonhosted.org/packages/source/d/dnspython/dnspython-%{version}.tar.gz
# Source0-md5:	7a8f6f15038a116598744517931420d0
URL:		https://www.dnspython.org/
BuildRequires:	python3-build
BuildRequires:	python3-devel >= 1:3.9
BuildRequires:	python3-hatchling >= 1.21.0
BuildRequires:	python3-installer
%if %{with tests}
BuildRequires:	python3-cryptography >= 43
BuildRequires:	python3-idna >= 3.7
BuildRequires:	python3-pytest >= 7.4
# doh: httpcore >= 1.0.0, httpx >= 0.26.0, h2 >= 4.1.0
# doq: aioquic >= 1.0.0
# trio: trio >= 0.23
# wmi: wmi >= 1.5.1
%endif
BuildRequires:	rpmbuild(macros) >= 2.044
BuildRequires:	rpm-pythonprov
Requires:	python3-modules >= 1:3.9
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
%setup -q -n dnspython-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
cp -pr examples/* $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}

sed -E -i -e '1s,#!\s*/usr/bin/env\s+python(\s|$),#!%{__python3}\1,' \
	-e '1s,#!\s*/usr/bin/env\s+python3(\s|$),#!%{__python3}\1,' \
	-e '1s,#!\s*/usr/bin/python(\s|$),#!%{__python3}\1,' \
	$RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/dns
%{py3_sitescriptdir}/dnspython-%{version}.dist-info
%{_examplesdir}/python3-%{module}-%{version}
