### Hexlet tests and linter status:
[![Actions Status](https://github.com/N-Davie/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/N-Davie/python-project-52/actions)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=N-Davie_python-project-52&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=N-Davie_python-project-52)

[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=N-Davie_python-project-52&metric=coverage)](https://sonarcloud.io/summary/new_code?id=N-Davie_python-project-52)

https://task-mr.onrender.com


Task Manager

Task Manager — это веб-приложение для управления задачами.

Основные возможности:
Регистрация и управление пользователями.
Создание, редактирование и удаление статусов задач.
Создание, редактирование и удаление задач с возможностью фильтрации.

Требования
Python 3.12+
Django 6.0+
SQLite (по умолчанию)

Дополнительные зависимости: django-filter, rollbar

Установка
Клонируйте репозиторий:
git clone <URL_репозитория>
cd python-project-52

Создайте и активируйте виртуальное окружение:
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows

Установите зависимости:
pip install -r requirements.txt
Если файла requirements.txt нет, можно установить зависимости вручную:
pip install django==6.0
pip install django-filter
pip install rollbar

Примените миграции:
python manage.py makemigrations
python manage.py migrate

Запустите сервер разработки:
python manage.py runserver

Откройте в браузере:
http://127.0.0.1:8000/
