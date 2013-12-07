%define _class	HTML
%define _subclass	Page
%define modname	%{_class}_%{_subclass}
%define pre	RC2

Summary:	Base class for XHTML page generation
Name:		php-pear-%{modname}
Version:	2.0.0
Release:	21
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/HTML_Page/
Source0:	http://download.pear.php.net/package/%{modname}-%{version}%{pre}.tar.bz2
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear

%description
The PEAR::HTML_Page package provides a simple interface for generating
an XHTML compliant page.
- supports virtually all HTML doctypes, from HTML 2.0 through XHTML 1.1
  and XHTML Basic 1.0
Plus preliminary support for XHTML 2.0
- namespace support
- global language declaration for the document
- line ending styles
- full META tag support
- support for stylesheet declaration in the head section
- support for linked stylesheets and scripts
- body can be a string, object with toHtml or toString methods or an
  array (can be combined)

%prep
%setup -qc
mv package.xml %{modname}-%{version}%{pre}/%{modname}.xml

%install
cd %{modname}-%{version}%{pre}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%doc %{modname}-%{version}%{pre}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{modname}.xml

