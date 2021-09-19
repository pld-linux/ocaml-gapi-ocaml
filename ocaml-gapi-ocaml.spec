#
# Conditional build:
%bcond_without	ocaml_opt	# skip building native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), remove when upstream will support it
%ifnarch %{ix86} %{x8664} arm aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

%define		pkgname	gapi-ocaml
%define		debug_package	%{nil}
Summary:	Google Data Protocol (GData) client library
Name:		ocaml-%{pkgname}
Version:	0.4.1
Release:	3
License:	MIT
Group:		Libraries
Source0:	https://github.com/astrada/gapi-ocaml/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	aeecae11fddf4511cea908808c73366a
URL:		http://gapi-ocaml.forge.ocamlcore.org/
BuildRequires:	cppo >= 0.9.3
BuildRequires:	ocaml >= 4.02.3
BuildRequires:	ocaml-biniou-devel >= 1.0.6
BuildRequires:	ocaml-cryptokit-devel >= 1.9
BuildRequires:	ocaml-curl-devel >= 0.6.0
BuildRequires:	ocaml-easy-format-devel >= 1.0.1
BuildRequires:	ocaml-findlib >= 1.4
BuildRequires:	ocaml-net-netstring-devel >= 4.1.4
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
%requires_eq ocaml
Requires:	ocaml-biniou-devel >= 1.0.6
Requires:	ocaml-cryptokit-devel >= 1.9
Requires:	ocaml-curl-devel >= 0.6.0
Requires:	ocaml-easy-format-devel >= 1.0.1
Requires:	ocaml-net-netstring-devel >= 3.7.3
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
dune build

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# no standard way of packaging .mli docs in pld. just drop
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/%{pkgname}/*.mli

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc LICENSE
%dir %{_libdir}/ocaml/%{pkgname}
%{_libdir}/ocaml/gapi-ocaml/META
%{_libdir}/ocaml/gapi-ocaml/dune-package
%{_libdir}/ocaml/gapi-ocaml/opam
%{_libdir}/ocaml/%{pkgname}/*.cma
%{_libdir}/ocaml/%{pkgname}/*.cmt*
%{_libdir}/ocaml/%{pkgname}/*.cm[ix]
%if %{with ocaml_opt}
%{_libdir}/ocaml/%{pkgname}/*.a
%{_libdir}/ocaml/%{pkgname}/*.cmx[as]
%endif
