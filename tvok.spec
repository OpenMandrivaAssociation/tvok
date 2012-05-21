%define		oversion	0.5.2
%define		mversion	36
%define		dversion	20110905

Name:		tvok
Version:	%{oversion}.%{mversion}
Release:	%mkrel 1
Summary:	A program for watching and recording TV
Group:		Video
License:	GPLv3+
URL:		http://www.kochkin.org/doku.php/tvok/010-index
Source:		http://tvok.kochkin.org/snapshots/%{name}-%{oversion}-%{mversion}-%{dversion}.tar.bz2
BuildRequires:	qt4-devel
BuildRequires:	imagemagick
Requires:	mplayer
Requires:	mencoder

%description
tvok is a mpalyer/mencoder-based program for watching and recording TV
using analog TV tuners.

%prep
%setup -q -n %{name}

%build
%qmake_qt4
%make

%install
%__rm -rf %{buildroot}
%__make install INSTALL_ROOT=%{buildroot}

for N in 16 32 48 64 128; do convert rc/tv.png -scale ${N}x${N} $N.png; done

%__install -D 16.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%__install -D 32.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%__install -D 48.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%__install -D 64.png %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
%__install -D 128.png %{buildroot}%{_iconsdir}/hicolor/128x128/apps/%{name}.png

# menu-entry
%__mkdir_p  %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=tvok
Comment=Watching and recording TV
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=AudioVideo;Video;Player;Recorder;TV;
EOF

%clean
%__rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc CHANGELOG README COPYRIGHT
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png

