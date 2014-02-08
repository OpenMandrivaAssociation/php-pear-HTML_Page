%define     _class          HTML
%define     _subclass       Page
%define		upstream_name	%{_class}_%{_subclass}
%define		pre 		    RC2

Name:		php-pear-%{upstream_name}
Version:	2.0.0
Release:	18
Summary:	Base class for XHTML page generation
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/HTML_Page/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}%{pre}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

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
%setup -q -c
mv package.xml %{upstream_name}-%{version}%{pre}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}%{pre}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}%{pre}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-14mdv2011.0
+ Revision: 667502
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-13mdv2011.0
+ Revision: 607103
- rebuild

* Sat Dec 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.0-12mdv2010.1
+ Revision: 477867
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.0.0-11mdv2010.0
+ Revision: 426640
- rebuild

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-10mdv2009.1
+ Revision: 321821
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2.0.0-9mdv2009.0
+ Revision: 224738
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-8mdv2008.1
+ Revision: 178511
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-7mdv2007.0
+ Revision: 81097
- Import php-pear-HTML_Page

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-7mdk
- new group (Development/PHP)

* Thu Aug 25 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-6mdk
- rebuilt to fix auto deps

* Tue Aug 09 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sat Jul 30 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-4mdk
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-2mdk
- fix deps

* Mon Jul 18 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-1mdk
- initial Mandriva package (PLD import)

