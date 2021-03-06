Summary:	sakura is a terminal emulator based on GTK and VTE
Summary(hu.UTF-8):	sakura egy GTK és VTE alapú terminál emulátor
Name:		sakura
Version:	2.4.0
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.pleyades.net/david/projects/sakura/%{name}-%{version}.tar.bz2
# Source0-md5:	ebc9ac2d0559c11863ed957557e95fef
URL:		http://www.pleyades.net/david/sakura.php
BuildRequires:	cmake
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	gettext-tools
BuildRequires:	gtk+2-devel
BuildRequires:	perl-tools-pod
BuildRequires:	pkgconfig
BuildRequires:	vte-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sakura is a terminal emulator based on GTK and VTE.

%description -l pl.UTF-8
sakura egy GTK és VTE alapú terminál emulátor.

%prep
%setup -q
%{__sed} -i 's@\(.*SET (CMAKE_C_FLAGS "\)-O2\(").\)*@\1%{rpmcflags}\2@' CMakeLists.txt

%build
%cmake .
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
%{_mandir}/man1/%{name}*
%{_pixmapsdir}/terminal-tango.svg
