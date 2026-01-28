install:
	uv sync

collectstatic:
	python manage.py collectstatic --noinput

migrate:
        python manage.py migrate
	

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
        pytest

.PHONY: install collectstatic migrate build render-start lint test package-install reinstall uninstall
