path := .
TORTOISE_ORM := db.base.TORTOISE_ORM

define Comment
	- Run `make help` to see all the available options.
	- Run `make lint` to run the linter.
	- Run `make lint-check` to check linter conformity.
	- Run `dep-lock` to lock the deps in 'requirements.txt' and 'requirements-dev.txt'.
	- Run `dep-sync` to sync current environment up to date with the locked deps.
	- Run `run-container` to run the container.
	- Run `kill-container` to kill the container.
	- Run `run-local` to run the local server.
endef


.PHONY: lint
lint: black isort flake mypy	## Apply all the linters.


.PHONY: lint-check
lint-check:  ## Check whether the codebase satisfies the linter rules.
	@echo
	@echo "Checking linter rules..."
	@echo "========================"
	@echo
	@black --check $(path)
	@isort --check $(path)
	@flake8 $(path)
	@mypy $(path)


.PHONY: black
black: ## Apply black.
	@echo
	@echo "Applying black..."
	@echo "================="
	@echo
	@black --fast $(path)
	@echo


.PHONY: isort
isort: ## Apply isort.
	@echo "Applying isort..."
	@echo "================="
	@echo
	@isort $(path)


.PHONY: flake
flake: ## Apply flake8.
	@echo
	@echo "Applying flake8..."
	@echo "================="
	@echo
	@flake8 $(path)


.PHONY: mypy
mypy: ## Apply mypy.
	@echo
	@echo "Applying mypy..."
	@echo "================="
	@echo
	@mypy $(path)


.PHONY: help
help: ## Show this help message.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'


.PHONY: test
test: ## Run the tests against the current version of Python.
	pytest


.PHONY: dep-lock
dep-lock: ## Freeze deps in 'requirements.txt' file.
	@pip-compile requirements.in -o requirements.txt
	@pip-compile requirements-dev.in -o requirements-dev.txt


.PHONY: dep-sync
dep-sync: ## Sync venv installation with 'requirements.txt' file.
	@chmod +x ./scripts/check-pip-tools.sh
	@./scripts/check-pip-tools.sh
	@pip-sync

.PHONY: dep-update
dep-update: ## Update all the deps.
	@chmod +x ./scripts/check-pip-tools.sh
	@./scripts/check-pip-tools.sh
	@chmod +x ./scripts/update-deps.sh
	@./scripts/update-deps.sh

.PHONY: db-config
db-config: ## Generate the database configuration file.
	aerich init -t $(TORTOISE_ORM)

.PHONY: db-init
db-init: ## Initialize the database.
	aerich init-db

.PHONY: db-migrate
db-migrate: ## Migrate the database.
	aerich migrate

.PHONY: db-upgrade
db-upgrade: ## Upgrade the database.
	aerich upgrade

.PHONY: create-volume
create-volume: ## Create the volume.
	docker volume create caddy_data
	docker volume create caddy_config
	docker volume create postgres

.PHONY: build-conntainer
build-container: ## Build the container.
	docker-compose up --build

.PHONY: run-container
run-container: ## Run the app in a docker container.
	docker-compose up -d

.PHONY: kill-container
kill-container: ## Stop the running docker container.
	docker-compose down


.PHONY: run-local
run-local: ## Run the app locally.
	uvicorn main:app --host=0.0.0.0 --port 5000 --reload