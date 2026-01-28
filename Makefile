install:
	uv sync

dev:
	uv run python manage.py runserver

PORT ?= 8000
start:
	uv run python manage.py migrate
	uv run gunicorn --bind 0.0.0.0:$(PORT) task_manager.wsgi

shell:
	uv run python manage.py shell

makemig:
	uv run python manage.py makemigrations

migrate:
	uv run python manage.py migrate

collectstatic:
	uv run python manage.py collectstatic --noinput

lint:
	ruff check task_manager users tasks statuses labels

test:
	uv pip install -e .
	uv run pytest

.PHONY: install dev start shell makemig migrate collectstatic lint test
