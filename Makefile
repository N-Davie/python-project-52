install:
		uv sync

runserver:
		python manage.py runserver

build:
		./build.sh

render-start:
		gunicorn task_manager.wsgi

test:
		uv run pytest --ds=task_manager.settings --reuse-db

coverage:
		uv run coverage run --omit='*/migrations/*,*/settings.py,*/venv/*,*/.venv/*' -m pytest --ds=task_manager.settings
		uv run coverage report --show-missing --skip-covered
		uv run coverage xml -o coverage.xml


ci-install:
		uv sync --group dev


ci-migrate:
		uv run python manage.py makemigrations --noinput && \
		uv run python manage.py migrate --noinput


ci-test:
		uv run coverage run --omit='*/migrations/*,*/settings.py,*/venv/*,*/.venv/*' -m pytest --ds=task_manager.settings --reuse-db
		uv run coverage xml
		uv run coverage report --show-missing --skip-covered

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
