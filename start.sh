sudo apt update
sudo apt install python3-venv libpq-dev nginx curl
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
cp -f conf/w-nginx /etc/nginx/sites-available/
cp -f conf/gunicorn.service /etc/systemd/system/
sudo ln -sf /etc/nginx/sites-available/w-nginx /etc/nginx/sites-enabled
systemctl enable gunicorn.service
systemctl daemon-reload
systemctl start gunicorn.service
systemctl restart nginx