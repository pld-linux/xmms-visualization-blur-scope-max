Summary:	Blur Scope MAX
Summary(pl):	Blur Scope MAX
Name:		xmms-visualization-blur-scope-max
Version:	1.3
Release:	4
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://home1.gte.net/mbardeen/blurscope/blur_scope_max-%{version}.tar.gz
# Source0-md5:	2ac23ec72d083ba81babc66f9f8301c9
Patch0:		blur_scope_max-no_asm.patch
Patch1:		blur_scope_max-no_dga.patch
Patch2:		%{name}-AM_PROG_AS.patch
Patch3:		%{name}-gcc33.patch
Patch4:		%{name}-xmms.patch
URL:		http://home1.gte.net/mbardeen/blurscope/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel >= 1.2.2
BuildRequires:	gtk+-devel >= 1.2.2
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel >= 1.2.3
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%patch2 -p1
%patch3 -p1
%patch4 -p1

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{xmms_visualization_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README ChangeLog
%attr(755,root,root) %{xmms_visualization_plugindir}/*.so
