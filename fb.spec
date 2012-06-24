Summary:	Utility for viewing and editing binary files
Summary(pl.UTF-8):	Narzędzie do przeglądania i edycji plików binarnych
Name:		fb
Version:	1.5
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://home.mho.net/jswaby/%{name}_tar.gz
# Source0-md5:	9dd94106da20bc5a2929c5e95a729106
URL:		http://home.mho.net/jswaby/fb.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fb is a utility for the viewing and editing of binary files. Files can
be viewed in binary, decimal, hexadecimal, and octal, and/or
characters. In addition to simple overwriting, a binary file may be
dumped as binary, hexadecimal, decimal, or octal numbers; edited with
one's favorite text editor; and then translated back into a binary
file.

%description -l pl.UTF-8
fb jest narzędziem do oglądania i edycji plików binarnych. Pliki mogą
być oglądane w postaci liczb systemu dwójkowego, dziesiętnego,
szesnastkowego, ósemkowego, a także w postaci znaków ASCII. Oprócz
prostego nadpisywania, pliki binarne mogą być zapisane do pliku w
dowolnej postaci tekstowej, zmodyfikowane edytorem tekstu, a następnie
z powrotem przetłumaczone na plik binarny.

%prep
%setup -qc

%build
%{__make} %{name} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
