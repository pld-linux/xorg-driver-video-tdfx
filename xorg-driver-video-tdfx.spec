Summary:	X.org video driver for 3Dfx video adapters
Summary(pl):	Sterownik obrazu X.org dla kart graficznych 3Dfx
Name:		xorg-driver-video-tdfx
Version:	1.1.0.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/driver/xf86-video-tdfx-%{version}.tar.bz2
# Source0-md5:	7b8f068e89337c24c81817a197e0f0bd
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xf86dgaproto-devel
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
BuildRequires:	xorg-xserver-server-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for 3Dfx video adapters. It supports Voodoo
Banshee, Voodoo3, Voodoo4 and Voodoo5 cards.

%description -l pl
Sterownik obrazu X.org dla kart graficznych 3Dfx. Obs³uguje karty
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
	DESTDIR=$RPM_BUILD_ROOT \
	drivermandir=%{_mandir}/man4

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/tdfx_drv.so
%{_mandir}/man4/tdfx.4x*
