clean:
	rm -rf ./allure-results

allure-report:
	poetry run allure serve ./allure-results