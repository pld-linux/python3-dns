#
# Conditional build:
%bcond_without	tests	# unit tests

%define		module	dns
Summary:	dnspython - a DNS toolkit for Python 3
Summary(pl.UTF-8):	dnspython - zestaw narzędzi do DNS dla Pythona 3
Name:		python3-%{module}
Version:	2.9.2
Release:	3
License:	ISC
Group:		Development/Languages/Python
Source0:	https://files.pythonhosted.org/packages/source/d/dnspython/dnspython-%{version}.tar.gz
# Source0-md5:	7b46ef88a095ea615709c6bbb62c34e3
Patch0:		dnspython-tests-feature-gates.patch
Patch1:		dnspython-sigtime-32bit-time_t.patch
URL:		https://www.dnspython.org/
BuildRequires:	python3-build
BuildRequires:	python3-devel >= 1:3.11
BuildRequires:	python3-installer
BuildRequires:	python3-uv-build >= 0.9.21
BuildRequires:	python3-uv-build < 0.14
%if %{with tests}
BuildRequires:	python3-aioquic >= 1.3.0
BuildRequires:	python3-cryptography >= 50
BuildRequires:	python3-h2 >= 4.4
BuildRequires:	python3-httpcore2 >= 2.13
BuildRequires:	python3-httpx2 >= 2.13
BuildRequires:	python3-hypercorn >= 0.18.0
BuildRequires:	python3-idna >= 3.20
BuildRequires:	python3-pytest >= 7.4
BuildRequires:	python3-quart-trio >= 0.12.0
BuildRequires:	python3-sniffio
BuildRequires:	python3-trio >= 0.34
# wmi: wmi >= 1.5.1
%endif
BuildRequires:	rpmbuild(macros) >= 2.044
BuildRequires:	rpm-pythonprov
Requires:	python3-modules >= 1:3.11
# upstream optional extras: rpm generates no deps for them, dnspython enables
# each one at runtime only when installed in at least this version
# (dns/_features.py)
# dnssec: DNSSEC signing and validation
Requires:	python3-cryptography >= 50
# idna: IDNA 2008 (falls back to IDNA 2003 otherwise)
Requires:	python3-idna >= 3.20
# doq: DNS over QUIC and DNS over HTTP/3
Suggests:	python3-aioquic >= 1.3.0
# doh: DNS over HTTPS
Suggests:	python3-h2 >= 4.4
Suggests:	python3-httpcore2 >= 2.13
Suggests:	python3-httpx2 >= 2.13
# trio: trio async backend
Suggests:	python3-trio >= 0.34
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
%patch -P0 -p1
%patch -P1 -p1

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
