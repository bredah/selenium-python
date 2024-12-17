clean:
	rm -rf ./allure-results

test:
	poetry run pytest

report:
	poetry run allure serve ./allure-results
