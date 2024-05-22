.DEFAULT_GOAL := help
.SILENT:
.PHONY: help

help:  ## Display this help
	awk 'BEGIN {FS = ":.*## "; printf "Usage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

##@ Format

format-black: ## run black (code formatter)
	poetry run black .

format-isort: ## run isort (imports formatter)
	poetry run isort .

format: format-black format-isort ## run all formatters

##@ Check

check-bandit: ## run bandit (check for common security issues)
	poetry run bandit -r ./src

check-black: ## run black in check mode
	poetry run black . --check

check-isort: ## run isort in check mode
	poetry run isort . --check

check-flake8: ## run flake8 (pep8 linter)
	poetry run flake8 ./src

check-mypy: ## run mypy (static-type checker)
	poetry run mypy ./src

check-mypy-report: ## run mypy & create report
	poetry run mypy ./src --html-report ./mypy_html

check: check-bandit check-black check-isort check-flake8 check-mypy ## run all checks

##@ Test

test: ## run tests
	poetry run pytest | tee tests.log

##@ Run Code

run: ## run
	cd ./src && poetry run uvicorn main:app --reload --host=0.0.0.0 --port=8000

##@ PostgreSQL

install_postgres: ## Install last postgres release version
	sudo sh -c 'echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
	wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
	sudo apt-get update
	sudo apt-get -y install postgresql

start_psql: ## Start postgres server
	systemctl start postgresql
	systemctl enable postgresql
	pg_lsclusters
	sudo -i -u postgres
	psql

generate_envrc:
	@if [ ! -f ./.envrc ]; then \
		current=$$(pwd); \
		echo 'export ENV_PATH="'"$$current"'/env.toml"' > ./.envrc; \
		echo 'export API_HOST="127.0.0.1"' >> ./.envrc; \
		echo 'export API_PORT="8000"' >> ./.envrc; \
		echo 'export DATABASE_URL="postgresql://<user>:<password>@<host_name>:5432/<db_name>"' >> ./.envrc; \
	fi

generate_env_toml:
	@if [ ! -f ./env.toml ]; then \
		current=$$(pwd); \
		echo '[injections]' > ./env.toml; \
		echo 'database_connection_factory = "database_connection_factory_prisma"' >> ./env.toml; \
	fi