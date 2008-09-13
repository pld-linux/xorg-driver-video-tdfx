Summary:	X.org video driver for 3Dfx video adapters
Summary(pl.UTF-8):	Sterownik obrazu X.org dla kart graficznych 3Dfx
Name:		xorg-driver-video-tdfx
Version:	1.4.0
Release:	4
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-tdfx-%{version}.tar.bz2
# Source0-md5:	b13132f24683ef759bfb0c1db5096496
Patch0:		%{name}-chiptype.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	Mesa-libGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.8.0
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xf86dgaproto-devel
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
BuildRequires:  rpmbuild(macros) >= 1.389
%requires_xorg_xserver_videodrv
Requires:	xorg-xserver-server >= 1.0.99.901
Obsoletes:	X11-driver-tdfx < 1:7.0.0
Obsoletes:	XFree86-3dfx
Obsoletes:	XFree86-driver-tdfx < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for 3Dfx video adapters. It supports Voodoo
Banshee, Voodoo3, Voodoo4 and Voodoo5 cards.

%description -l pl.UTF-8
Sterownik obrazu X.org dla kart graficznych 3Dfx. Obsługuje karty
Voodoo Banshee, Voodoo3, Voodoo4 i Voodoo5.

%prep
%setup -q -n xf86-video-tdfx-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/tdfx_drv.so
%{_mandir}/man4/tdfx.4*
