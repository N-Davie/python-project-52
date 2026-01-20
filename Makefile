install:
	uv pip install -r requirements.txt

collectstatic:
	python manage.py collectstatic --noinput

migrate:
	python manage.py migrate

build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi

lint:
	ruff check task_manager task_manager_app

test:
	pytest

.PHONY: install collectstatic migrate build render-start lint test
