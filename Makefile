install:
		uv sync

runserver:
		python manage.py runserver

build:
		./build.sh

render-start:
		gunicorn task_manager.wsgi

test:
	        uv run manage.py test

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml:coverage.xml

lint:
	        uv run ruff

migrate:
		uv run python manage.py makemigrations
		uv run python manage.py migrate

check:
		uv pip check

PORT ?= 8000
start:
		uv run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi

makemessages:
	 	django-admin makemessages

render-start:
		gunicorn task_manager.wsgi
		
