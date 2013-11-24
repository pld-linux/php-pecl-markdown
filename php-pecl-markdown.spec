%define		php_name	php%{?php_suffix}
%define		modname	markdown
%define		status		stable
Summary:	%{modname} - a fast Markdown parser
Summary(pl.UTF-8):	%{modname} - szybki parser Markdown
Name:		%{php_name}-pecl-%{modname}
Version:	1.0.0
Release:	3
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	cc8e4575f63c5809dcb62d146a9d04eb
URL:		http://pecl.php.net/package/markdown/
BuildRequires:	%{php_name}-devel >= 4:5.2.0
BuildRequires:	rpmbuild(macros) >= 1.650
%{?requires_php_extension}
Provides:	php(%{modname}) = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Markdown is an extension to parse a Markdown text, from a string or a
file. It is fast and has a simple API.

In PECL status of this extension is: %{status}.

%description -l pl.UTF-8
Markdown to rozszerzenie umożliwiające parsowanie pochodzącego z
łańcucha znaków lub pliku tekstu Markdown. Rozszerzenie to jest
szybkie i posiada proste w użyciu API.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -q -c
mv %{modname}-%{version}/* .

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
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
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
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/discount.so
