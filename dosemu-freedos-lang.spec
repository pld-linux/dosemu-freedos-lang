Summary:	Various development tools for FreeDOS
Summary(pl):	Kompilatory i inne narzêdzia developerskie dzia³aj±ce pod DOS-em
Name:		dosemu-freedos-lang
Version:	beta7h01
Release:	3
Epoch:		1
License:	GPL
Group:		Applications/Emulators
Source0:	ftp://ftp.task.gda.pl/pub/dos/freedos/files/distributions/ripcord/beta7h01/EN/full/disksets/lang1.zip
# Source0-md5:	4812b5307cab44932a49d0c64d197ec8
URL:		http://www.freedos.org/
BuildRequires:	unzip
Requires:	dosemu
Requires:	dosemu-freedos-minimal
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Various development tools for FreeDOS.

%description -l pl
Ró¿ne narzêdzia developerskie dla DOS-a, takie jak kompilatory,
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
