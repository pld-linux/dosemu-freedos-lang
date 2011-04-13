Summary:	Various development tools for FreeDOS
Summary(pl.UTF-8):	Kompilatory i inne narzędzia developerskie działające pod DOS-em
Name:		dosemu-freedos-lang
Version:	beta7h03
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/Emulators
Source0:	ftp://ftp.task.gda.pl/pub/dos/freedos/files/distributions/ripcord/%{version}/EN/disksets/lang1.zip
# Source0-md5:	47c516daad419e599b872631b20f86df
URL:		http://www.freedos.org/
BuildRequires:	unzip
Requires:	dosemu
Requires:	dosemu-freedos-minimal
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Various development tools for FreeDOS.

%description -l pl.UTF-8
Różne narzędzia developerskie dla DOS-a, takie jak kompilatory,
interpretery, linker, itp.

%prep
%setup -q -c

rm -rf freedos
mkdir freedos
for i in *.ZIP ; do
	unzip -L -o $i -d freedos
done
rm -f freedos/copying freedos/bin/cwsdpmi.exe

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/lib/dosemu/bootdir

cp -Rf freedos $RPM_BUILD_ROOT/var/lib/dosemu/bootdir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/var/lib/dosemu/bootdir/freedos/bin/*
/var/lib/dosemu/bootdir/freedos/doc/*
/var/lib/dosemu/bootdir/freedos/help/*
