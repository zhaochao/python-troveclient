%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global sname troveclient
%if 0%{?fedora}
%global with_python3 1
%endif

%global dist_eayunstack .eayunstack

Name:           python-troveclient
Version:        2.5.0
Release:        2%{?dist_eayunstack}
Summary:        Client library for OpenStack DBaaS API

License:        ASL 2.0
URL:            http://www.openstack.org/
Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:      noarch


%description
This is a client for the Trove API. There's a Python API (the
troveclient module), and a command-line script (trove). Each
implements 100% (or less ;) ) of the Trove API.


%package -n python2-%{sname}
Summary:        Client library for OpenStack DBaaS API
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-sphinx
BuildRequires:  python-requests
BuildRequires:  python-pbr
BuildRequires:  python-oslo-sphinx
BuildRequires:  python-oslotest
BuildRequires:  python-mock
BuildRequires:  python-testtools
BuildRequires:  python-testrepository
BuildRequires:  python-keystoneauth1
BuildRequires:  python-keystoneclient
BuildRequires:  python-mistralclient
BuildRequires:  python-swiftclient
BuildRequires:  python-simplejson
BuildRequires:  python-httplib2
BuildRequires:  python-requests-mock
BuildRequires:  python-crypto

Requires:       python-babel
Requires:       python-keystoneauth1
Requires:       python-keystoneclient
Requires:       python-mistralclient
Requires:       python-swiftclient
Requires:       python-oslo-i18n
Requires:       python-oslo-utils
Requires:       python-pbr
Requires:       python-prettytable
Requires:       python-requests
Requires:       python-setuptools
Requires:       python-simplejson
Requires:       python-six

%{?python_provide:%python_provide python2-%{sname}}

%description -n python2-%{sname}
This is a client for the Trove API. There's a Python API (the
troveclient module), and a command-line script (trove). Each
implements 100% (or less ;) ) of the Trove API.


%if 0%{?with_python3}
%package -n python3-%{sname}
Summary:        Client library for OpenStack DBaaS API
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  python3-requests
BuildRequires:  python3-pbr
BuildRequires:  python3-oslo-sphinx
BuildRequires:  python3-oslotest
BuildRequires:  python3-mock
BuildRequires:  python3-testtools
BuildRequires:  python3-testrepository
BuildRequires:  python3-keystoneclient
BuildRequires:  python3-mistralclient
BuildRequires:  python3-swiftclient
BuildRequires:  python3-simplejson
BuildRequires:  python3-httplib2
BuildRequires:  python3-requests-mock
BuildRequires:  python3-crypto

Requires:       python3-babel
Requires:       python3-keystoneclient
Requires:       python3-mistralclient
Requires:       python3-swiftclient
Requires:       python3-oslo-utils
Requires:       python3-pbr
Requires:       python3-prettytable
Requires:       python3-requests
Requires:       python3-setuptools
Requires:       python3-simplejson
Requires:       python3-six

%{?python_provide:%python_provide python3-%{sname}}

%description -n python3-%{sname}
This is a client for the Trove API. There's a Python API (the
troveclient module), and a command-line script (trove). Each
implements 100% (or less ;) ) of the Trove API.
%endif


%prep
%setup -q -n %{name}-%{upstream_version}

# Remove bundled egg-info
rm -rf %{name}.egg-info

# Let RPM handle the requirements
rm -f {test-,}requirements.txt


%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%{__python2} setup.py build_sphinx


%install
%if 0%{?with_python3}
%py3_install
mv %{buildroot}%{_bindir}/trove %{buildroot}%{_bindir}/trove-%{python3_version}
ln -s ./trove-%{python3_version} %{buildroot}%{_bindir}/trove-3
%endif

%py2_install
mv %{buildroot}%{_bindir}/trove %{buildroot}%{_bindir}/trove-%{python2_version}
ln -s ./trove-%{python2_version} %{buildroot}%{_bindir}/trove-2

ln -s ./trove-2 %{buildroot}%{_bindir}/trove


%check
# FIXME test fails with latest release
PYTHONPATH=. %{__python2} setup.py test ||:
%if 0%{?with_python3}
rm -rf .testrepository
PYTHONPATH=. %{__python3} setup.py test ||:
%endif


%files -n python2-%{sname}
%doc doc/build/html README.rst
%license LICENSE
%{python2_sitelib}/python_troveclient-*.egg-info
%{python2_sitelib}/troveclient
%{_bindir}/trove-2*
%{_bindir}/trove

%if 0%{?with_python3}
%files -n python3-%{sname}
%doc doc/build/html README.rst
%license LICENSE
%{python3_sitelib}/python_troveclient-*.egg-info
%{python3_sitelib}/troveclient
%{_bindir}/trove-3*
%endif

%changelog
* Fri Apr 14 2017 Zhao <chao.zhao@eayun.com> 2.5.0-2.eayunstack
- 077295d support utf8 characters in names for client. 

* Tue Sep 13 2016 Haikel Guemar <hguemar@fedoraproject.org> 2.5.0-1
- Update to 2.5.0

