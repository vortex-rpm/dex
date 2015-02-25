Name:           dex
Version:        0.6.1
Release:        1.vortex%{?dist}
Summary:        MongoDB performance tuning tool
Group:          Applications/Databases
License:        MIT
URL:            https://github.com/mongolab/dex
Source0:        https://github.com/mongolab/dex/archive/%{name}-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel, python-setuptools, python-pymongo, python-dargparse, python-ordereddict
Requires:       python-pymongo, python-dargparse, python-ordereddict

%description
Dex is a MongoDB performance tuning tool that compares queries to the available
indexes in the queried collection(s) and generates index suggestions based on
simple heuristics. Currently you must provide a connection URI for your database.

%prep
%setup -q -n %{name}-%{version}

%install
rm -rf %{buildroot}
%{__python} setup.py install --root %{buildroot}
rm -rf %{buildroot}/%{python_sitelib}/Dex-%{version}-py2.6.egg-info

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python_sitelib}/%{name}*
%{_bindir}/%{name}
%doc docs/SCHEMA.md docs/release-notes.md README.md LICENSE.txt

%changelog
* Wed Feb 25 2015 Ilya Otyutskiy <ilya.otyutskiy@icloud.com> - 0.6.1-1.vortex
- Initial packaging.
