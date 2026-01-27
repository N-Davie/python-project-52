install:
	uv pip install .

collectstatic:
	python manage.py collectstatic --noinput

migrate:
	python manage.py migrate

build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi:application

lint:
	ruff check task_manager users tasks statuses labels

test:
	pytest

.PHONY: install collectstatic migrate build render-start lint test
