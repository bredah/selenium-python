-include .env

clean:
	rm -rf ./allure-results

setup:
	poetry shell && \
	poetry install --no-root

test:
	poetry run pytest

report:
	poetry run allure serve ./allure-results

docker-build:
	docker compose -f docker-compose.yaml build automation

docker-debug:
	docker compose run --entrypoint /bin/bash automation

docker-run:
	docker compose -f docker-compose.yaml run automation pytest

grid-up:
	docker compose -f docker-compose.yaml up -d selenium-hub chrome

grid-down:
	docker compose -f docker-compose.yaml down --remove-orphans
