Summary:	X.org video driver for 3Dfx video adapters
Summary(pl):	Sterownik obrazu X.org dla kart graficznych 3Dfx
Name:		xorg-driver-video-tdfx
Version:	1.1.1.3
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/driver/xf86-video-tdfx-%{version}.tar.bz2
# Source0-md5:	e193816d45960d62937deb99d1b9986a
URL:		http://xorg.freedesktop.org/
BuildRequires:	Mesa-libGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xf86dgaproto-devel
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 0.99.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for 3Dfx video adapters. It supports Voodoo
Banshee, Voodoo3, Voodoo4 and Voodoo5 cards.

%description -l pl
Sterownik obrazu X.org dla kart graficznych 3Dfx. Obs�uguje karty
Voodoo Banshee, Voodoo3, Voodoo4 i Voodoo5.

%prep
%setup -q -n xf86-video-tdfx-%{version}

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
