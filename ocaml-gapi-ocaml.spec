#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

%define		module	gapi-ocaml
%define		debug_package	%{nil}
Summary:	Google Data Protocol (GData) client library
Summary(pl.UTF-8):	Biblioteka kliencka protokołu GData (Google Data Protocol)
Name:		ocaml-%{module}
Version:	0.4.2
Release:	2
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/astrada/gapi-ocaml/releases
Source0:	https://github.com/astrada/gapi-ocaml/archive/v%{version}/%{module}-%{version}.tar.gz
# Source0-md5:	d8f549e73826599a5ae94a3633aa7356
URL:		http://gapi-ocaml.forge.ocamlcore.org/
BuildRequires:	cppo >= 0.9.3
BuildRequires:	ocaml >= 1:4.02.3
BuildRequires:	ocaml-cryptokit-devel >= 1.9
BuildRequires:	ocaml-curl-devel >= 0.6.0
BuildRequires:	ocaml-dune
BuildRequires:	ocaml-findlib >= 1.4
BuildRequires:	ocaml-net-netstring-devel >= 4.1.4
BuildRequires:	ocaml-net-netsys-devel >= 4.1.4
BuildRequires:	ocaml-xmlm-devel >= 1.0.2
BuildRequires:	ocaml-yojson-devel >= 1.1.6
%requires_eq	ocaml-runtime
Conflicts:	ocaml-gapi-ocaml < 0.4.1-4
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
Summary(pl.UTF-8):	Biblioteka kliencka protokołu GData (Google Data Protocol) - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-cryptokit-devel >= 1.9
Requires:	ocaml-curl-devel >= 0.6.0
Requires:	ocaml-net-netstring-devel >= 4.1.1
Requires:	ocaml-net-netsys-devel >= 4.1.4
Requires:	ocaml-xmlm-devel >= 1.0.2
Requires:	ocaml-yojson-devel >= 1.1.6

%description devel
This package contains files needed to develop OCaml programs using
this library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki gapi-ocaml.

%prep
%setup -q -n %{module}-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/%{module}/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/%{module}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%dir %{_libdir}/ocaml/gapi-ocaml
%{_libdir}/ocaml/gapi-ocaml/META
%{_libdir}/ocaml/gapi-ocaml/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/gapi-ocaml/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/gapi-ocaml/dune-package
%{_libdir}/ocaml/gapi-ocaml/opam
%{_libdir}/ocaml/gapi-ocaml/*.cmi
%{_libdir}/ocaml/gapi-ocaml/*.cmt
%{_libdir}/ocaml/gapi-ocaml/*.cmti
%{_libdir}/ocaml/gapi-ocaml/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/gapi-ocaml/*.a
%{_libdir}/ocaml/gapi-ocaml/*.cmx
%{_libdir}/ocaml/gapi-ocaml/*.cmxa
%endif
