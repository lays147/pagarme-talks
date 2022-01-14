run_lint:
	poetry run tox -e lint

run_tests:
	poetry run pytest

run_compliance:
	poetry run tox -e compliance

setup_pre_commit:
	pre-commit install --hook-type pre-commit --hook-type pre-push --hook-type commit-msg
