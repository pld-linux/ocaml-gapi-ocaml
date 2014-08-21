#
# Conditional build:
%bcond_without	opt		# build opt

%define		pkgname	gapi-ocaml
%define		debug_package	%{nil}
Summary:	Google Data Protocol (GData) client library
Name:		ocaml-%{pkgname}
Version:	0.2.1
Release:	3
License:	MIT
Group:		Libraries
Source0:	https://forge.ocamlcore.org/frs/download.php/1274/%{pkgname}-%{version}.tar.gz
# Source0-md5:	c87aa3b2c9afef190307d8da51d65875
URL:		http://gapi-ocaml.forge.ocamlcore.org/
BuildRequires:	cppo >= 0.9.3
BuildRequires:	ocaml >= 3.04-7
BuildRequires:	ocaml-biniou-devel >= 1.0.6
BuildRequires:	ocaml-cryptokit-devel >= 1.9
BuildRequires:	ocaml-curl-devel >= 0.6.0
BuildRequires:	ocaml-easy-format-devel >= 1.0.1
BuildRequires:	ocaml-extlib-devel >= 1.5.4
BuildRequires:	ocaml-findlib >= 1.4
BuildRequires:	ocaml-net-netstring-devel >= 3.6
#BuildRequires:	ocaml-net-netstring-devel >= 3.7.3
BuildRequires:	ocaml-xmlm-devel >= 1.1.1
BuildRequires:	ocaml-yojson-devel >= 1.1.6
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gapi-ocaml is a simple, unofficial, OCaml client for Google Services.
The project is hosted on github, where you can find the latest
development version, and on the OCaml forge where you can find
releases. Reference documentation can be found here.

%description -l pl.UTF-8
Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających tej biblioteki.

%package devel
Summary:	Google Data Protocol (GData) client library - development part
Summary(pl.UTF-8):	Wiązania gapi dla OCamla - cześć programistyczna
Group:		Development/Libraries
%requires_eq	ocaml
Requires:	ocaml-biniou-devel >= 1.0.6
Requires:	ocaml-cryptokit-devel >= 1.9
Requires:	ocaml-curl-devel >= 0.6.0
Requires:	ocaml-easy-format-devel >= 1.0.1
Requires:	ocaml-extlib-devel >= 1.5.4
Requires:	ocaml-net-netstring-devel >= 3.6
#Requires:	ocaml-net-netstring-devel >= 3.7.3
Requires:	ocaml-xmlm-devel >= 1.1.1
Requires:	ocaml-yojson-devel >= 1.1.6

%description devel
This package contains files needed to develop OCaml programs using
this library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów używających
tej biblioteki.

%prep
%setup -q -n %{pkgname}-%{version}

%build
ocaml setup.ml -configure \
	--destdir $RPM_BUILD_ROOT
ocaml setup.ml -build

%install
rm -rf $RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
install -d $OCAMLFIND_DESTDIR
ocaml setup.ml -install

# move to dir pld ocamlfind looks
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/%{pkgname}
mv $OCAMLFIND_DESTDIR/%{pkgname}/META \
	$RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/%{pkgname}
cat <<EOF >> $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/%{pkgname}/META
directory="+%{pkgname}"
EOF

# no standard way of packaging .mli docs in pld. just drop
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/%{pkgname}/*.mli

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc LICENSE
%dir %{_libdir}/ocaml/%{pkgname}
%{_libdir}/ocaml/%{pkgname}/*.a
%{_libdir}/ocaml/%{pkgname}/*.cm[ixa]*
%dir %{_libdir}/ocaml/site-lib/%{pkgname}
%{_libdir}/ocaml/site-lib/%{pkgname}/META
