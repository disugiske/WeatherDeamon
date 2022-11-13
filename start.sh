sudo apt update
sudo apt install python3-venv libpq-dev nginx curl
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
cp conf/w-nginx /etc/nginx/sites-available/
cp conf/gunicorn.service /etc/systemd/system/
sudo ln -s /etc/nginx/sites-available/w-nginx /etc/nginx/sites-enabled
systemctl enable unicorn.service
systemctl daemon-reload
systemctl start unicorn.service
systemctl restart nginx