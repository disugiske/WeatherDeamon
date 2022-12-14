

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
Requires: python3.9 nginx gcc
Summary:  uvicorn daemon


%description
uvicorn daemon
Git version: %{git_version} (branch: %{git_branch})

%define __etcdir    /usr/local/etc
%define __logdir    /val/log/
%define __bindir    /usr/local/ip2w/
%define __systemddir	/etc/systemd/system/
%define __nginxdir	/etc/nginx/
%define __sysconfigdir	/usr/local/

%prep
%setup -n otus-%{current_datetime}

%build
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
deactivate
cp conf/w-nginx /etc/nginx/sites-available/
cp conf/gunicorn.service %{__systemddir}
ln -s %{__nginxdir}sites-available/w-nginx/ %{__nginxdir}sites-enabled
%install
[ "%{buildroot}" != "/" ] && rm -fr %{buildroot}
%{__mkdir} -p %{buildroot}/%{__systemddir}
%{__mkdir} -p %{buildroot}/%{__sysconfigdir}
%{__mkdir} -p %{buildroot}/%{__logdir}
%{__mkdir} -p %{buildroot}/%{__bindir}
%{__install} -pD -m 644 conf/gunicorn.service %{buildroot}%{__systemddir}%{name}.service
%{__install} -pD -m 644 conf/w-nginx %{buildroot}%{__nginxdir}sites-available

%post
%systemd_post %{name}.service
systemctl enable unicorn.service
systemctl daemon-reload
systemctl start unicorn.service
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
