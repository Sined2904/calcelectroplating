# calcelectroplating

### Описание
Бэкенд для сайта "Калькулятор гальваника". Выполнение рассчетов по заданным параметрам.

### Технологии
asgiref==3.7.2
attrs==23.2.0
Django==4.2.10
django-cors-headers==4.3.1
django-filter==23.5
djangorestframework==3.14.0
drf-spectacular==0.27.1
drf-spectacular-sidecar==2024.2.1
inflection==0.5.1
jsonschema==4.21.1
jsonschema-specifications==2023.12.1
python-dotenv==1.0.1
pytz==2024.1
PyYAML==6.0.1
referencing==0.33.0
rpds-py==0.18.0
sqlparse==0.4.4
typing_extensions==4.9.0
tzdata==2024.1
uritemplate==4.1.1
gunicorn==20.1.0
psycopg2-binary==2.9.3

### Запуск проекта в dev-режиме
- Установите и активируйте виртуальное окружение
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- Заполните файл .env
- В корневой папке проекта выполните команду:
```
docker compose up 
```

### Описание переменных окружения
POSTGRES_DB - название БД
POSTGRES_USER - имя пользователя БД
POSTGRES_PASSWORD - пароль пользователя БД
DB_NAME - название БД
DB_HOST - адрес БД
DB_PORT - порт БД
SECRET_KEY - криптографическая подпись Django
DEBUG - статус режима дебаг


### Авторы
Пиневич Денис

Github - Sined2904
Den2904@yandex.ru
TG - @PinevichD
