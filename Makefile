install:
	uv pip install -e .

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
	uv pip install -e .
	uv run pytest

.PHONY: install collectstatic migrate build render-start lint test
