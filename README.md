## Gunicorn FastApi Deamon
Демон для ubuntu, при переходе на корень сервера возвращает данные о погоде и местоположении исходя из ip адреса.
Запросы проксируются nginx

Стек:
 - gunicorn + uvicorn workers
 - FastApi
 - nginx

## Установка
Для работы надо создать переменное окружение:

```sh
python3 -m venv WeatherDeamon
source WeatherDeamon/bin/activate
```
Установить зависимости из requirements.txt

Затем из виртуального окружения:

```sh
deactivate
```

Скопировать файлы из /conf и создать ссылку:

```sh
cp conf/gunicorn.service /etc/systemd/system/
cp conf/w-nginx /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/w-nginx /etc/nginx/sites-enabled
```

Активировать демона и запустить его и nginx:
```sh
sudo systemctl enable gunicorn
sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl start nginx
```

Демон должен запуститься на 2000 порту, статус и логи можно посмотреть по команде:
```sh
sudo systemctl enable gunicorn
sudo journalctl -u gunicorn -e
```

Так же предусмотрен запуск через rpm пакет, но пока в разработке, так как некорректно работает)
