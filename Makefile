run-local:
	poetry run python athenas_test/manage.py runserver

deps:
	poetry --version &> /dev/null || (echo -e "ERROR: please install poetry" && false)
	poetry config virtualenvs.in-project true
	poetry env list
	poetry env info
	poetry install
