run-local:
	poetry run uvicorn outbound.app:app --reload

deps:
	poetry --version &> /dev/null || (echo -e "ERROR: please install poetry" && false)
	poetry config virtualenvs.in-project true
	poetry env list
	poetry env info
	poetry install

