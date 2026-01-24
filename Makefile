install:
	uv pip install -r requirements.txt

collectstatic:
	python manage.py collectstatic --noinput

migrate:
	python manage.py migrate

build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi:application

lint:
	ruff check task_manager task_manager_app

test:
	PYTHONPATH=. pytest task_manager_app/tests

.PHONY: install collectstatic migrate build render-start lint test
