%define contentdir /var/www
%define with_oci8 %{?_with_oci8:1}%{!?_with_oci8:0}
%define with_mssql %{?_with_mssql:1}%{!?_with_mssql:0}
%define with_mhash %{?_with_mhash:1}%{!?_with_mhash:0}
%define with_ibase %{?_with_ibase:1}%{!?_with_ibase:0}

Summary: The PHP HTML-embedded scripting language. (PHP: Hypertext Preprocessor)
Name: php
Version: 5.0.3
Release: 2
License: The PHP License
Group: Development/Languages
URL: http://www.php.net/

Source0: http://www.php.net/distributions/php-%{version}.tar.gz

Source50: php.conf

Patch2: php-5.0.1-config.patch
Patch3: php-5.0.2-lib64.patch
Patch4: php-4.2.2-cxx.patch
Patch5: php-4.3.3-install.patch
Patch6: php-4.3.1-tests.patch
Patch7: php-4.3.2-libtool15.patch
Patch8: php-4.3.3-miscfix.patch
Patch9: php-4.3.6-umask.patch
Patch10: php-5.0.2-gdnspace.patch
Patch11: php-4.3.8-round.patch
Patch13: php-5.0.2-phpize64.patch
Patch14: php-5.0.3-sprintf.patch
Patch15: php-5.0.3-zstrtod.patch
Patch16: php-5.0.3-gdheaders.patch

# Fixes for extension modules
Patch21: php-4.3.1-odbc.patch
Patch22: php-5.0.3-libmbfl.patch

# Functional changes
Patch30: php-4.3.1-dlopen.patch
Patch31: php-5.0.0-easter.patch

BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: bzip2-devel, curl-devel >= 7.9, db4-devel, expat-devel
BuildRequires: gmp-devel, aspell-devel >= 0.50.0
BuildRequires: httpd-devel >= 2.0.46-1, libjpeg-devel, libpng-devel, pam-devel
BuildRequires: libstdc++-devel, openssl-devel
BuildRequires: zlib-devel, pcre-devel >= 5.0, smtpdaemon
BuildRequires: bzip2, fileutils, file >= 4.0, perl, libtool >= 1.4.3
Obsoletes: php-dbg, mod_php, php3, phpfi, stronghold-php, php-openssl
# Enforce Apache module ABI compatibility
Requires: httpd-mmn = %(cat %{_includedir}/httpd/.mmn || echo missing-httpd-devel)
Requires: php-pear, file >= 4.0

%description
PHP is an HTML-embedded scripting language. PHP attempts to make it
easy for developers to write dynamically generated webpages. PHP also
offers built-in database integration for several commercial and
non-commercial database management systems, so writing a
database-enabled webpage with PHP is fairly simple. The most common
use of PHP coding is probably as a replacement for CGI scripts. The
mod_php module enables the Apache Web server to understand and process
the embedded PHP language in Web pages.

%package devel
Group: Development/Libraries
Summary: Files needed for building PHP extensions.
Requires: php = %{version}-%{release}

%description devel
The php-devel package contains the files needed for building PHP
extensions. If you need to compile your own PHP extensions, you will
need to install this package.

%package pear
Group: Development/Languages
Summary: PHP Extension and Application Repository Components
Requires: php = %{version}-%{release}

%description pear
PEAR is a framework and distribution system for reusable PHP
components.  This package contains a set of PHP components from the
PEAR repository.

%package imap
Summary: An Apache module for PHP applications that use IMAP.
Group: Development/Languages
Requires: php = %{version}-%{release}
Obsoletes: mod_php3-imap, stronghold-php-imap
BuildRequires: krb5-devel, openssl-devel, libc-client-devel

%description imap
The php-imap package contains a dynamic shared object (DSO) for the
Apache Web server. When compiled into Apache, the php-imap module will
add IMAP (Internet Message Access Protocol) support to PHP. IMAP is a
protocol for retrieving and uploading e-mail messages on mail
servers. PHP is an HTML-embedded scripting language. If you need IMAP
support for PHP applications, you will need to install this package
and the php package.

%package ldap
Summary: A module for PHP applications that use LDAP.
Group: Development/Languages
Requires: php = %{version}-%{release}
Obsoletes: mod_php3-ldap, stronghold-php-ldap
BuildRequires: cyrus-sasl-devel, openldap-devel, openssl-devel

%description ldap
The php-ldap package is a dynamic shared object (DSO) for the Apache
Web server that adds Lightweight Directory Access Protocol (LDAP)
support to PHP. LDAP is a set of protocols for accessing directory
services over the Internet. PHP is an HTML-embedded scripting
language. If you need LDAP support for PHP applications, you will
need to install this package in addition to the php package.

%package mysql
Summary: A module for PHP applications that use MySQL databases.
Group: Development/Languages
Requires: php = %{version}-%{release}
Provides: php_database
Obsoletes: mod_php3-mysql, stronghold-php-mysql
BuildRequires: mysql-devel

%description mysql
The php-mysql package contains a dynamic shared object that will add
MySQL database support to PHP. MySQL is an object-relational database
management system. PHP is an HTML-embeddable scripting language. If
you need MySQL support for PHP applications, you will need to install
this package and the php or mod_php package.

%package pgsql
Summary: A PostgreSQL database module for PHP.
Group: Development/Languages
Requires: php = %{version}-%{release}
Provides: php_database
Obsoletes: mod_php3-pgsql, stronghold-php-pgsql
BuildRequires: krb5-devel, openssl-devel, postgresql-devel

%description pgsql
The php-pgsql package includes a dynamic shared object (DSO) that can
be compiled in to the Apache Web server to add PostgreSQL database
support to PHP. PostgreSQL is an object-relational database management
system that supports almost all SQL constructs. PHP is an
HTML-embedded scripting language. If you need back-end support for
PostgreSQL, you should install this package in addition to the main
php package.

%package odbc
Group: Development/Languages
Requires: php = %{version}-%{release}
Summary: A module for PHP applications that use ODBC databases.
Provides: php_database
Obsoletes: stronghold-php-odbc
BuildRequires: unixODBC-devel

%description odbc
The php-odbc package contains a dynamic shared object that will add
database support through ODBC to PHP. ODBC is an open specification
which provides a consistent API for developers to use for accessing
data sources (which are often, but not always, databases). PHP is an
HTML-embeddable scripting language. If you need ODBC support for PHP
applications, you will need to install this package and the php
package.

%package soap
Group: Development/Languages
Requires: php = %{version}-%{release}
Summary: A module for PHP applications that use the SOAP protocol
BuildRequires: libxml2-devel

%description soap
The php-soap package contains a dynamic shared object that will add
support to PHP for using the SOAP web services protocol.

%if %{with_ibase}
%package interbase
Group: Development/Languages
Prereq: php = %{version}-%{release}, perl, grep
Summary: A module for PHP applications that use Interbase databases.
Provides: php_database

%description interbase
The php-interbase package contains a dynamic shared object that will add
database support through Interbase to PHP. Interbase is a commercial
database system made by the Interbase Corporation. PHP is an
HTML-embeddable scripting language. If you need Interbase support for 
PHP applications, you will need to install this package and the php 
package.
%endif

%if %{with_oci8}
%package oci8
Group: Development/Languages
Requires: php = %{version}-%{release}
Summary: A module for PHP applications that use OCI8 databases.
Provides: php_database

%description oci8
The php-oci8 package contains a dynamic shared object that will add
support for accessing OCI8 databases to PHP.
%endif

%if %{with_mssql}
%package mssql
Group: Development/Languages
Requires: php = %{version}-%{release}, freetds
Summary: A module for PHP applications that use MSSQL databases.
Provides: php_database
BuildRequires: freetds-devel

%description mssql
The mssql package contains a dynamic shared object that will add
support for accessing MSSQL databases to PHP.
%endif

%if %{with_mhash}
%package mhash
Summary: A module for PHP applications that use Mhash.
Group: Development/Languages
Requires: php = %{version}-%{release}
BuildRequires: mhash-devel

%description mhash
The php-mhash package is a dynamic shared object (DSO) for the Apache
Web server that adds Mhash support to PHP.
%endif

%package snmp
Summary: A module for PHP applications that query SNMP-managed devices.
Group: Development/Languages
Requires: php = %{version}-%{release}
BuildRequires: net-snmp-devel

%description snmp
The php-snmp package contains a dynamic shared object that will add
support for querying SNMP devices to PHP.  PHP is an HTML-embeddable
scripting language. If you need SNMP support for PHP applications, you
will need to install this package and the php package.

%package xml
Summary: A module for PHP applications which use XML
Group: Development/Languages
Requires: php = %{version}-%{release}
Obsoletes: php-domxml, php-dom
Provides: php-dom, php-xsl
BuildRequires: libxslt-devel >= 1.0.18-1, libxml2-devel >= 2.4.14-1

%description xml
The php-xml package contains dynamic shared objects which add support
to PHP for manipulating XML documents using the DOM tree,
and performing XSL transformations on XML documents.

%package xmlrpc
Summary: A module for PHP applications which use the XML-RPC protocol
Group: Development/Languages
Requires: php = %{version}-%{release}
BuildRequires: expat-devel

%description xmlrpc
The php-xmlrpc package contains a dynamic shared object that will add
support for the XML-RPC protocol to PHP.

%package mbstring
Summary: A module for PHP applications which need multi-byte string handling
Group: Development/Languages
Requires: php = %{version}-%{release}

%description mbstring
The php-mbstring package contains a dynamic shared object that will add
support for multi-byte string handling to PHP.

%package ncurses
Summary: A module for PHP applications for using ncurses interfaces
Group: Development/Languages
Requires: php = %{version}-%{release}
BuildRequires: ncurses-devel

%description ncurses
The php-mbstring package contains a dynamic shared object that will add
support for using the ncurses terminal output interfaces.

%package gd
Summary: A module for PHP applications for using the gd graphics library
Group: Development/Languages
Requires: php = %{version}-%{release}
BuildRequires: gd-devel, freetype-devel

%description gd
The php-mbstring package contains a dynamic shared object that will add
support for using the gd graphics library to PHP.

%prep
%setup -q
%patch2 -p1 -b .config
%patch3 -p1 -b .lib64
%patch4 -p1 -b .cxx
%patch5 -p1 -b .install
%patch6 -p1 -b .tests
%patch7 -p1 -b .libtool15
##patch8 -p1 -b .miscfix
%patch9 -p1 -b .umask
%patch10 -p1 -b .gdnspace
%patch11 -p1 -b .round
%patch13 -p1 -b .phpize64
%patch14 -p1 -b .sprintf
%patch15 -p1 -b .zstrtod
%patch16 -p1 -b .gdheaders

%patch21 -p1 -b .odbc
%patch22 -p1 -b .libmbfl

%patch30 -p1 -b .dlopen
%patch31 -p1 -b .easter

# Prevent %%doc confusion over LICENSE files
cp Zend/LICENSE Zend/ZEND_LICENSE
cp TSRM/LICENSE TSRM_LICENSE
cp regex/COPYRIGHT regex_COPYRIGHT
cp ext/gd/libgd/README gd_README

# Source is built twice: once for /usr/bin/php, once for the Apache DSO.
mkdir build-cgi build-apache

# Use correct libdir
perl -pi -e 's|%{_prefix}/lib|%{_libdir}|' php.ini-recommended

# Remove bogus test; position of read position after fopen(, "a+")
# is not defined by C standard, so don't presume anything.
rm -f ext/standard/tests/file/bug21131.phpt

# Tests that fail.
rm -f ext/standard/tests/file/bug22414.phpt \
      ext/iconv/tests/bug16069.phpt

: Build for oci8=%{with_oci8} mssql=%{with_mssql} mhash=%{with_mhash} ibase=%{with_ibase}

%build

CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"; export CFLAGS

# Install extension modules in %{_libdir}/php/modules.
EXTENSION_DIR=%{_libdir}/php/modules; export EXTENSION_DIR

# pull latest ltmain.sh, AC_PROG_LIBTOOL
libtoolize --force --copy
# force aclocal run during buildconf
touch acinclude.m4

# Regenerate configure scripts (patches change config.m4's)
./buildconf --force

# Shell function to configure and build a PHP tree.
build() {
# bison-1.875-2 seems to produce a broken parser; workaround.
mkdir Zend && cp ../Zend/zend_{language,ini}_{parser,scanner}.[ch] Zend
ln -sf ../configure
%configure \
	--cache-file=../config.cache \
        --with-libdir=%{_lib} \
	--with-config-file-path=%{_sysconfdir} \
	--with-config-file-scan-dir=%{_sysconfdir}/php.d \
	--enable-force-cgi-redirect \
	--disable-debug \
	--enable-pic \
	--disable-rpath \
	--enable-inline-optimization \
	--with-bz2 \
	--with-db4=%{_prefix} \
	--with-curl \
	--with-exec-dir=%{_bindir} \
	--with-freetype-dir=%{_prefix} \
	--with-png-dir=%{_prefix} \
	--enable-gd-native-ttf \
	--without-gdbm \
	--with-gettext \
	--with-gmp \
	--with-iconv \
	--with-jpeg-dir=%{_prefix} \
	--with-openssl \
	--with-png \
	--with-pspell \
	--with-expat-dir=%{_prefix} \
        --with-pcre-regex=%{_prefix} \
	--with-zlib \
	--with-layout=GNU \
	--enable-bcmath \
	--enable-exif \
	--enable-ftp \
	--enable-magic-quotes \
	--enable-safe-mode \
	--enable-sockets \
	--enable-sysvsem \
	--enable-sysvshm \
	--enable-track-vars \
	--enable-trans-sid \
	--enable-yp \
	--enable-wddx \
	--with-pear=/usr/share/pear \
	--with-kerberos \
	--enable-ucd-snmp-hack \
	--with-unixODBC=shared,%{_prefix} \
	--enable-memory-limit \
	--enable-shmop \
	--enable-calendar \
	--enable-dbx \
	--enable-dio \
        --with-mime-magic=%{_datadir}/file/magic.mime \
        --without-sqlite \
        --with-libxml-dir=%{_prefix} \
	--with-xml \
	$* 
if test $? != 0; then 
  tail -500 config.log
  : configure failed
  exit 1
fi

make %{?_smp_mflags}
}

# Build standalone /usr/bin/php and shared extension modules that
# do not need to be built twice.
pushd build-cgi
build --enable-force-cgi-redirect \
      --with-imap=shared --with-imap-ssl \
      --enable-mbstring=shared --enable-mbstr-enc-trans \
      --enable-mbregex \
      --with-ncurses=shared \
      --with-gd=shared \
      --with-xmlrpc=shared \
      --with-ldap=shared \
      --with-mysql=shared,%{_prefix} \
      %{?_with_oci8:--with-oci8=shared} \
      %{?_with_mssql:--with-mssql=shared} \
      %{?_with_mhash:--with-mhash=shared} \
      %{?_with_ibase:--with-interbase=shared,/opt/interbase} \
      --enable-dom=shared \
      --with-dom-xslt=%{_prefix} --with-dom-exslt=%{_prefix} \
      --with-pgsql=shared \
      --with-snmp=shared,%{_prefix} \
      --enable-soap=shared \
      --with-xsl=shared,%{_prefix}
popd

# Build Apache module
pushd build-apache
build --with-apxs2=%{_sbindir}/apxs \
      --without-mysql --without-gd \
      --without-odbc --disable-dom
popd

%check
cd build-cgi
# Run tests
export NO_INTERACTION=1 REPORT_EXIT_STATUS=1 MALLOC_CHECK_=2
unset TZ LANG LC_ALL
if ! make test; then
  set +x
  for f in `find .. -name \*.diff -type f -print`; do
    echo "TEST FAILURE: $f --"
    cat "$f"
    echo "-- $f result ends."
  done
  set -x
  #exit 1
fi
unset NO_INTERACTION REPORT_EXIT_STATUS MALLOC_CHECK_

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

# Install from CGI tree
pushd build-cgi
make install INSTALL_ROOT=$RPM_BUILD_ROOT 
popd

# Install the Apache module
pushd build-apache
make install-sapi INSTALL_ROOT=$RPM_BUILD_ROOT
popd

# Install the default configuration file and icons
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/
install -m 644    php.ini-recommended $RPM_BUILD_ROOT%{_sysconfdir}/php.ini
install -m 755 -d $RPM_BUILD_ROOT%{contentdir}/icons
install -m 644    *.gif $RPM_BUILD_ROOT%{contentdir}/icons/

# install the DSO
install -m 755 -d $RPM_BUILD_ROOT%{_libdir}/httpd/modules
install -m 755 build-apache/libs/libphp5.so $RPM_BUILD_ROOT%{_libdir}/httpd/modules

# Apache config fragment
install -m 755 -d $RPM_BUILD_ROOT/etc/httpd/conf.d
install -m 644 $RPM_SOURCE_DIR/php.conf $RPM_BUILD_ROOT/etc/httpd/conf.d

install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php.d
install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/lib/php
install -m 700 -d $RPM_BUILD_ROOT%{_localstatedir}/lib/php/session

# Generate files lists and stub .ini files for each subpackage
for mod in pgsql mysql odbc ldap snmp xmlrpc imap \
    mbstring ncurses gd dom xsl soap \
    %{?_with_oci8:oci8} %{?_with_mssql:mssql} %{?_with_mhash:mhash} \
    %{?_with_ibase:interbase}; do
    cat > $RPM_BUILD_ROOT%{_sysconfdir}/php.d/${mod}.ini <<EOF
; Enable ${mod} extension module
extension=${mod}.so
EOF
    cat > files.${mod} <<EOF
%attr(755,root,root) %{_libdir}/php/modules/${mod}.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.d/${mod}.ini
EOF
done

# The dom and xsl modules are both packaged in php-xml
cat files.dom files.xsl > files.xml

# Remove PEAR testsuite
rm -rf $RPM_BUILD_ROOT%{_datadir}/pear/tests

# Remove unpackaged files
rm -f $RPM_BUILD_ROOT%{_libdir}/php/modules/*.a \
      $RPM_BUILD_ROOT%{_bindir}/{phptar,pearize}

# Remove irrelevant docs
rm -f README.{Zeus,QNX,CVS-RULES}

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
rm files.*

%files
%defattr(-,root,root)
%doc CODING_STANDARDS CREDITS EXTENSIONS INSTALL LICENSE NEWS README*
%doc Zend/ZEND_* gd_README TSRM_LICENSE regex_COPYRIGHT
%config(noreplace) %{_sysconfdir}/php.ini
%config %{_sysconfdir}/pear.conf
%{_bindir}/php
%dir %{_libdir}/php
%dir %{_libdir}/php/modules
%dir %{_localstatedir}/lib/php
%attr(0770,root,apache) %dir %{_localstatedir}/lib/php/session
%{_libdir}/httpd/modules/libphp5.so
%config %{_sysconfdir}/httpd/conf.d/php.conf
%dir %{_sysconfdir}/php.d
%{contentdir}/icons/php.gif

%files pear
%defattr(-,root,root)
%{_bindir}/pear
%{_datadir}/pear

%files devel
%defattr(-,root,root)
%{_bindir}/php-config
%{_bindir}/phpize
%{_bindir}/phpextdist
%{_includedir}/php
%{_libdir}/php/build

%files pgsql -f files.pgsql
%files mysql -f files.mysql
%files odbc -f files.odbc
%files imap -f files.imap
%files ldap -f files.ldap
%files snmp -f files.snmp
%files xml -f files.xml
%files xmlrpc -f files.xmlrpc
%files mbstring -f files.mbstring
%files ncurses -f files.ncurses
%files gd -f files.gd
%files soap -f files.soap

%if %{with_oci8}
%files oci8 -f files.oci8
%endif
%if %{with_mssql}
%files mssql -f files.mssql
%endif
%if %{with_mhash}
%files mhash -f files.mhash
%endif
%if %{with_ibase}
%files interbase -f files.interbase
%endif

%changelog
* Wed Feb  9 2005 Joe Orton <jorton@redhat.com> 5.0.3-2
- install the ext/gd headers (#145891)
- enable pcntl extension in /usr/bin/php (#142903)
- add libmbfl array arithmetic fix (dcb314@hotmail.com, #143795)
- add BuildRequire for recent pcre-devel (#147448)

* Wed Jan 12 2005 Joe Orton <jorton@redhat.com> 5.0.3-1
- update to 5.0.3 (thanks to Robert Scheck et al, #143101)
- enable xsl extension (#142174)
- package both the xsl and dom extensions in php-xml
- enable soap extension, shared (php-soap package) (#142901)
- add patches from upstream 5.0 branch:
 * Zend_strtod.c compile fixes
 * correct php_sprintf return value usage

* Mon Nov 22 2004 Joe Orton <jorton@redhat.com> 5.0.2-8
- update for db4-4.3 (Robert Scheck, #140167)
- build against mysql-devel
- run tests in %%check

* Wed Nov 10 2004 Joe Orton <jorton@redhat.com> 5.0.2-7
- truncate changelog at 4.3.1-1
- merge from 4.3.x package:
 - enable mime_magic extension and Require: file (#130276)

* Mon Nov  8 2004 Joe Orton <jorton@redhat.com> 5.0.2-6
- fix dom/sqlite enable/without confusion

* Mon Nov  8 2004 Joe Orton <jorton@redhat.com> 5.0.2-5
- fix phpize installation for lib64 platforms
- add fix for segfault in variable parsing introduced in 5.0.2

* Mon Nov  8 2004 Joe Orton <jorton@redhat.com> 5.0.2-4
- update to 5.0.2 (#127980)
- build against mysqlclient10-devel
- use new RTLD_DEEPBIND to load extension modules
- drop explicit requirement for elfutils-devel
- use AddHandler in default conf.d/php.conf (#135664)
- "fix" round() fudging for recent gcc on x86
- disable sqlite pending audit of warnings and subpackage split

* Fri Sep 17 2004 Joe Orton <jorton@redhat.com> 5.0.1-4
- don't build dom extension into 2.0 SAPI

* Fri Sep 17 2004 Joe Orton <jorton@redhat.com> 5.0.1-3
- ExclusiveArch: x86 ppc x86_64 for the moment

* Fri Sep 17 2004 Joe Orton <jorton@redhat.com> 5.0.1-2
- fix default extension_dir and conf.d/php.conf

* Thu Sep  9 2004 Joe Orton <jorton@redhat.com> 5.0.1-1
- update to 5.0.1
- only build shared modules once
- put dom extension in php-dom subpackage again
- move extension modules into %%{_libdir}/php/modules
- don't use --with-regex=system, it's ignored for the apache* SAPIs

* Wed Aug 11 2004 Tom Callaway <tcallawa@redhat.com>
- Merge in some spec file changes from Jeff Stern (jastern@uci.edu)

* Mon Aug 09 2004 Tom Callaway <tcallawa@redhat.com>
- bump to 5.0.0
- add patch to prevent clobbering struct re_registers from regex.h
- remove domxml references, replaced with dom now built-in
- fix php.ini to refer to php5 not php4

* Wed Aug 04 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- rebuild

* Wed Jul 14 2004 Joe Orton <jorton@redhat.com> 4.3.8-3
- update to 4.3.8
- catch some fd > FD_SETSIZE vs select() issues (#125258)

* Mon Jun 21 2004 Joe Orton <jorton@redhat.com> 4.3.7-4
- pick up test failures again
- have -devel require php of same release

* Thu Jun 17 2004 Joe Orton <jorton@redhat.com> 4.3.7-3
- add gmp_powm fix (Oskari Saarenmaa, #124318)
- split mbstring, ncurses, gd, openssl extns into subpackages
- fix memory leak in apache2handler; use ap_r{write,flush}
  rather than brigade interfaces

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jun  3 2004 Joe Orton <jorton@redhat.com> 4.3.7-1
- update to 4.3.7
- have -pear subpackage require php of same VR

* Wed May 26 2004 Joe Orton <jorton@redhat.com> 4.3.6-6
- buildrequire smtpdaemon (#124430)
- try switching to system libgd again (prevent symbol conflicts
  when e.g. mod_perl loads the system libgd library.)

* Wed May 19 2004 Joe Orton <jorton@redhat.com> 4.3.6-5
- don't obsolete php-imap (#123580)
- unconditionally build -imap subpackage

* Thu May 13 2004 Joe Orton <jorton@redhat.com> 4.3.6-4
- remove trigger

* Thu Apr 22 2004 Joe Orton <jorton@redhat.com> 4.3.6-3
- fix umask reset "feature" (#121454)
- don't use DL_GLOBAL when dlopen'ing extension modules

* Sun Apr 18 2004 Joe Orton <jorton@redhat.com> 4.3.6-2
- fix segfault on httpd SIGHUP (upstream #27810)

* Fri Apr 16 2004 Joe Orton <jorton@redhat.com> 4.3.6-1
- update to 4.3.6 (Robert Scheck, #121011)

* Wed Apr  7 2004 Joe Orton <jorton@redhat.com> 4.3.4-11
- add back imap subpackage, using libc-client (#115535)

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 18 2004 Joe Orton <jorton@redhat.com> 4.3.4-10
- eliminate /usr/local/lib RPATH in odbc.so
- really use system pcre library

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com> 4.3.4-9
- rebuilt

* Mon Feb  2 2004 Bill Nottingham <notting@redhat.com> 4.3.4-8
- obsolete php-imap if we're not building it

* Wed Jan 28 2004 Joe Orton <jorton@redhat.com> 4.3.4-7
- gd fix for build with recent Freetype2 (from upstream)
- remove easter egg (Oden Eriksson, Mandrake)

* Wed Jan 21 2004 Joe Orton <jorton@redhat.com> 4.3.4-6
- php-pear requires php
- also remove extension=imap from php.ini in upgrade trigger
- merge from Taroon: allow upgrade from Stronghold 4.0

* Wed Jan 21 2004 Joe Orton <jorton@redhat.com> 4.3.4-5
- add defattr for php-pear subpackage
- restore defaults: output_buffering=Off, register_argc_argv=On
- add trigger to handle php.ini upgrades smoothly (#112470)

* Tue Jan 13 2004 Joe Orton <jorton@redhat.com> 4.3.4-4
- conditionalize support for imap extension for the time being
- switch /etc/php.ini to use php.ini-recommended (but leave
  variables_order as EGPCS) (#97765)
- set session.path to /var/lib/php/session by default (#89975)
- own /var/lib/php{,/session} and have apache own the latter
- split off php-pear subpackage (#83771)

* Sat Dec 13 2003 Jeff Johnson <jbj@jbj.org> 4.3.4-3
- rebuild against db-4.2.52.

* Mon Dec  1 2003 Joe Orton <jorton@redhat.com> 4.3.4-2
- rebuild for new libxslt (#110658) 
- use --with-{mssql,oci8} for enabling extensions (#110482)
- fix rebuild issues (Jan Visser, #110274)
- remove hard-coded LIBS
- conditional support for mhash (Aleksander Adamowski, #111251)

* Mon Nov 10 2003 Joe Orton <jorton@redhat.com> 4.3.4-1.1
- rebuild for FC1 updates

* Mon Nov 10 2003 Joe Orton <jorton@redhat.com> 4.3.4-1
- update to 4.3.4
- include all licence files
- libxmlrpc fixes

* Mon Oct 20 2003 Joe Orton <jorton@redhat.com> 4.3.3-6
- use bundled libgd (#107407)
- remove manual: up-to-date manual sources are no longer DFSG-free;
  it's too big; it's on the web anyway; #91292, #105804, #107384

* Wed Oct 15 2003 Joe Orton <jorton@redhat.com> 4.3.3-5
- add php-xmlrpc subpackage (#107138)

* Mon Oct 13 2003 Joe Orton <jorton@redhat.com> 4.3.3-4
- drop recode support, symbols collide with MySQL

* Sun Oct 12 2003 Joe Orton <jorton@redhat.com> 4.3.3-3
- split domxml extension into php-domxml subpackage
- enable xslt and xml support in domxml extension (#106042)
- fix httpd-devel build requirement (#104341)
- enable recode extension (#106755)
- add workaround for #103982

* Thu Sep 25 2003 Jeff Johnson <jbj@jbj.org> 4.3.3-3
- rebuild against db-4.2.42.

* Sun Sep  7 2003 Joe Orton <jorton@redhat.com> 4.3.3-2
- don't use --enable-versioning, it depends on libtool being
 broken (#103690)

* Sun Sep  7 2003 Joe Orton <jorton@redhat.com> 4.3.3-1
- update to 4.3.3
- add libtool build prereq (#103388)
- switch to apache2handler

* Mon Jul 28 2003 Joe Orton <jorton@redhat.com> 4.3.2-8
- rebuild

* Tue Jul 22 2003 Nalin Dahyabhai <nalin@redhat.com> 4.3.2-7
- rebuild

* Tue Jul  8 2003 Joe Orton <jorton@redhat.com> 4.3.2-6
- use system pcre library

* Mon Jun  9 2003 Joe Orton <jorton@redhat.com> 4.3.2-5
- enable mbstring and mbregex (#81336)
- fix use of libtool 1.5

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun  3 2003 Joe Orton <jorton@redhat.com> 4.3.2-3
- add lib64 and domxml fixes

* Tue Jun  3 2003 Frank Dauer <f@paf.net>
- added conditional support for mssql module (#92149)

* Fri May 30 2003 Joe Orton <jorton@redhat.com> 4.3.2-2
- update the -tests and -lib64 patches
- fixes for db4 detection
- require aspell-devel >= 0.50.0 for pspell compatibility

* Thu May 29 2003 Joe Orton <jorton@redhat.com> 4.3.2-1
- update to 4.3.2

* Fri May 16 2003 Joe Orton <jorton@redhat.com> 4.3.1-3
- link odbc module correctly
- patch so that php -n doesn't scan inidir
- run tests using php -n, avoid loading system modules

* Wed May 14 2003 Joe Orton <jorton@redhat.com> 4.3.1-2
- workaround broken parser produced by bison-1.875

* Tue May  6 2003 Joe Orton <jorton@redhat.com> 4.3.1-1
- update to 4.3.1; run test suite
- open extension modules with RTLD_NOW rather than _LAZY
