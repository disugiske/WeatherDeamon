License:        BSD
Vendor:         Otus
Group:          PD01
URL:            http://otus.ru/lessons/3/
Source0:        otus-%{current_datetime}.tar.gz
BuildRoot:      %{_tmppath}/otus-%{current_datetime}
Name:           ip2w
Version:        0.0.1
Release:        1
BuildArch:      noarch
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
BuildRequires: systemd
Requires: python-devel nginx gcc
Summary:  uvicorn daemon


%description
uvicorn daemon
Git version: %{git_version} (branch: %{git_branch})

%define __etcdir    /usr/local/etc
%define __logdir    /val/log/
%define __bindir    /usr/local/ip2w/
%define __systemddir	/usr/lib/systemd/system/
%define __nginxdir	/etc/nginx/
%define __sysconfigdir	/usr/local/

%prep
%setup -n otus-%{current_datetime}

%build
cd WeatherDeamon
python3 -m venv WeatherDeamon
source WeatherDeamon/bin/activate
pip3 install -r requirements.txt
deactivate
cp /conf/w-nginx /etc/nginx/sites-available/w-nginx

%install
[ "%{buildroot}" != "/" ] && rm -fr %{buildroot}
%{__mkdir} -p %{buildroot}/%{__systemddir}
%{__mkdir} -p %{buildroot}/%{__sysconfigdir}
%{__mkdir} -p %{buildroot}/%{__logdir}
%{__mkdir} -p %{buildroot}/%{__bindir}
%{__install} -pD -m 644 /conf/gunicorn.service %{buildroot}/%{__systemddir}/%{name}.service
%{__install} -pD -m 644 conf/w-nginx %{buildroot}/%{__nginxdir}/sites-available/

%post
%systemd_post %{name}.service
systemctl daemon-reload
systemctl restart nginx

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun %{name}.service

%clean
[ "%{buildroot}" != "/" ] && rm -fr %{buildroot}


%files
%{__logdir}
%{__bindir}
%{__systemddir}
%{__sysconfigdir}
%{__nginxdir}