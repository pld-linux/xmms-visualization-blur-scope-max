Summary:	Blur Scope MAX
Summary(pl):	Blur Scope MAX
Name:		xmms-visualization-blur-scope-max
Version:	1.3
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://home1.gte.net/mbardeen/blurscope/blur_scope_max-%{version}.tar.gz
Patch0:		blur_scope_max-no_asm.patch
Patch1:		blur_scope_max-no_dga.patch
URL:		http://home1.gte.net/mbardeen/blurscope/
Requires:	xmms
BuildRequires:	xmms-devel >= 1.2.3
BuildRequires:	glib-devel >= 1.2.2
BuildRequires:	gtk+-devel >= 1.2.2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Blur Scope MAX.

%description -l pl
Blur Scope MAX.

%prep
%setup -q -n blur_scope_max-%{version}
%ifnarch %{ix86}
%patch0
%endif
%patch1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS NEWS README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/xmms/*/*.so
