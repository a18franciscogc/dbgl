Name:			dbgl
Summary:	        DOSBox Game Launcher
URL:			http://home.quicknet.nl/qn/prive/blankendaalr/dbgl/
Version:		0.79
Release:		2%{?dist}
BuildArch:		noarch
License:		GPLv2
BuildRequires:	eclipse-swt
BuildRequires:	hsqldb
BuildRequires:	jpackage-utils
BuildRequires:	p7zip
BuildRequires:	unzip
BuildRequires:	xerces-j2
BuildRequires:	liboil
BuildRequires: desktop-file-utils
Requires:		dosbox >= 0.70
Requires:		eclipse-swt
Requires:		hsqldb
Requires:               java >= 1:1.7.0
Requires:               java-headless >= 1:1.7.0
Requires:		jpackage-utils
Requires:		SDL_net
Requires:		SDL_sound
Source0:		http://members.quicknet.nl/blankendaalr/dbgl/download/src079.zip
Source2:		%{name}.png
Source3:		%{name}

%description
DBGL is a Java front-end for DOSBox, based largely upon the proven
interface of D-Fend.
The front-end is by no means finished. It is a work in progress
and lacking many features, but the core is working, and I think
the product is somewhat usable as it is. Please bear in mind that
the interface is still quite rough around the edges.

%prep
%setup -c

%build
ant
tar -xf ./dist/dbgl079_generic.tar.gz

%install

# jars
install -dm 755 %{buildroot}%{_javadir}/%{name}/
copy_files="captures db  dbgl.jar  dosroot export lib profiles templates xsl"
for files in $copy_files
do 
cp -af $files %{buildroot}/%{_javadir}/%{name}/
done

# startscript
mkdir -p %{buildroot}%{_bindir}
install -m 775 %{SOURCE3} %{buildroot}%{_bindir}

# icons
mkdir %{buildroot}%{_datadir}/pixmaps
install -m 644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/

# menu
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Type=Application
Exec=dbgl
Icon=dbgl
Terminal=false
Name=DOSBox Game Launcher
Comment=%{summary}
Categories=Game;
EOF

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_javadir}/%{name}
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Fri Mar 20 2015 Oleg Kishinskiy <legunt@yandex.ru> - 0.79-2
- FIX change category

* Fri Mar 20 2015 Oleg Kishinskiy <legunt@yandex.ru> - 0.79-1
- update for new vertion
- change category

* Tue Dec 23 2014 Oleg Kishinskiy <legunt@yandex.ru> - 0.78-3
- fix spec to install from source

* Wed Dec 10 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.78-2
- spec cleanup

* Wed Dec 10 2014 Oleg Kishinskiy <legunt@yandex.ru> - 0.78-1
- Update for new vertion

* Mon Jul 29 2013 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.76-2
- Initial build rpm 
