Summary:	MasqDialer console client
Summary(pl):	Konsolowy klient MasqDialera
Name:		mclient
Version:	2.8
Release:	3
License:	GPL
Group:		Networking/Utilities
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
%{__make} LIBS="%{rpmldflags}" CFLAGS="%{rpmcflags}"

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
