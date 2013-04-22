# vim:filetype=spec

# provided by wg_rpmbuild.py
%define _topdir $_topdir

# passed to wg_rpmbuild.py
%define checkoutroot $checkoutroot
%define lib_dir $lib_dir
%define rpm_version $rpm_version
%define buildnumber $buildnumber

# don't empty out jars
%define __jar_repack %{nil}

Summary: WGen db migrations framework
Name: tt-migrations-base
Version: %{rpm_version}
Release: %{buildnumber}
License: EULA
Group: TT
BuildArch: noarch
BuildRoot: %{_topdir}/ROOT/%{name}-%{version}

Requires: jdk = 2000:1.6.0_24-fcs

%description
The framework for running database migrations using LiquiBase and Postgres.

%prep
# nothing

%build
# nothing

%install
mkdir -p %{buildroot}/opt/tt/migrations/lib
mkdir -p %{buildroot}/opt/tt/migrations/migrations
mkdir -p %{buildroot}/opt/tt/migrations/bin
mkdir -p %{buildroot}/opt/tt/migrations/conf
mkdir -p %{buildroot}/opt/tt/migrations/log
mkdir -p %{buildroot}/usr/lib/python2.4/site-packages/func/minion/modules

cp %{checkoutroot}/scripts/migrations/liquibase.sh %{buildroot}/opt/tt/migrations/bin/liquibase.sh
cp %{lib_dir}/postgresql-8.3-603.jdbc4.jar %{buildroot}/opt/tt/migrations/lib/postgresql-8.3-603.jdbc4.jar
cp %{lib_dir}/liquibase-core-1.9.5.jar %{buildroot}/opt/tt/migrations/lib/liquibase-core-1.9.5.jar
cp %{checkoutroot}/scripts/migrations/wgmigration.py %{buildroot}/usr/lib/python2.4/site-packages/func/minion/modules/wgmigration.py

touch %{buildroot}/opt/tt/migrations/conf/migrations.env
touch %{buildroot}/usr/lib/python2.4/site-packages/func/minion/modules/wgmigration.pyc
touch %{buildroot}/usr/lib/python2.4/site-packages/func/minion/modules/wgmigration.pyo

find %{buildroot} -not -type d | sed 's#^%{buildroot}##g' >> INSTALLED_FILES

%files -f INSTALLED_FILES
%defattr(-,postgres,postgres)
%attr(0755,postgres,postgres) /opt/tt/migrations/bin/liquibase.sh
%ghost /opt/tt/migrations/conf/migrations.env
%dir /opt/tt/migrations
%dir /opt/tt/migrations/lib
%dir /opt/tt/migrations/migrations
%dir /opt/tt/migrations/bin
%dir /opt/tt/migrations/conf
%dir /opt/tt/migrations/log

%post
/sbin/service funcd restart || :
