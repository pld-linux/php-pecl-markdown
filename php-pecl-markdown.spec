%define		_modname	markdown
%define		_status		stable
Summary:	%{_modname} - a fast Markdown parser
Summary(pl.UTF-8):	%{_modname} - szybki parser Markdown
Name:		php-pecl-%{_modname}
Version:	1.0.0
Release:	2
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	cc8e4575f63c5809dcb62d146a9d04eb
URL:		http://pecl.php.net/package/markdown/
BuildRequires:	php-devel >= 4:5.2.0
BuildRequires:	rpmbuild(macros) >= 1.344
%{?requires_php_extension}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Markdown is an extension to parse a Markdown text, from a string or a
file. It is fast and has a simple API.

In PECL status of this extension is: %{_status}.

%description -l pl.UTF-8
Markdown to rozszerzenie umożliwiające parsowanie pochodzącego z
łańcucha znaków lub pliku tekstu Markdown. Rozszerzenie to jest
szybkie i posiada proste w użyciu API.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c
mv %{_modname}-%{version}/* .

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT \
	EXTENSION_DIR=%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=discount.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc CREDITS README
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{php_extensiondir}/discount.so
