install:
	uv sync

collectstatic:
	python manage.py collectstatic --noinput

migrate:
	python3 manage.py migrate
	python3 manage.py makemigrations

build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi:application

package-install:
	uv tool install dist/*.whl

reinstall:
	uv tool install --force dist/*.whl

uninstall:
	uv tool uninstall hexlet-code

lint:
	ruff check task_manager users tasks statuses labels

test:
	uv pip install -e .
	uv run python manage.py migrate --settings=task_manager.settings --noinput
	uv run pytest

.PHONY: install collectstatic migrate build render-start lint test package-install reinstall uninstall
