Summary:	MasqDialer console client
Summary(pl):	Konsolowy klient MasqDialera
Name:		mclient
Version:	2.8
Release:	2
License:	GPL
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
Source0:	http://cpwright.villagenet.com/cli-mclient/cli-%{name}-%{version}.tar.gz
Patch0:		%{name}-rcfile.patch
URL:		http://cpwright.villagenet.com/cli-mclient
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Console MasqDialer client for use with Charles P. Wright MasqDialer
server (mserver).

%description -l pl
Konsolowy klient MasqDialera, przeznaczony do u¿ycia razem z serwerem
MasqDialera autorstwa Charlesa P. Wrighta (mserverem).

%prep
%setup  -q
%patch0 -p1

%build
make LIBS="-s" CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install mclient $RPM_BUILD_ROOT%{_bindir}

gzip -9nf CHANGES README.mclientrc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mclient
%doc *.gz
