# Python - Selenium

## Prerequisites

This repository provides a Python Selenium test automation setup with support for execution using Docker and Selenium Grid.

Make sure the following tools are installed:

- Docker
- Docker Compose
- Poetry (for dependency management): [Install Poetry](https://python-poetry.org/docs/)
- Pre-commit (for code validation): [Install Pre-commit](https://pre-commit.com/#install)
- Makefile: [Windows - Installation](https://community.chocolatey.org/packages/make)

## Environment Setup

1. Docker Image Configuration

Create a `.env` file with the following settings to define the default platform and Selenium version:

```sh
# .env file
DOCKER_DEFAULT_PLATFORM=linux/amd64
SELENIUM_VERSION=4.27.0
```

2. Test Environment Configuration

In the same `.env` file, specify the browser, version, and whether to run in headless mode:

```sh
# .env file
BROWSER_NAME=chrome
BROWSER_VERSION=latest
HEADLESS=true
```

3. Selenium Grid Configuration

Configure the Selenium Grid endpoint depending on your execution environment:

- Local Execution:

```sh
SELENIUM_GRID=http://localhost:4444/wd/hub
```

- Docker Compose Execution
```sh
SELENIUM_GRID=http://selenium-hub:4444/wd/hub
```

## Project Setup

1.	Install dependencies using Poetry:

```sh
poetry install
# or
make setup
```

2.	Initialize pre-commit in your development environment:

```sh
poetry run pre-commit install
```

## Execution

- Local

```sh
poetry run pytest
# or
make test
```

- With Docker Compose

```sh
docker compose -f docker-compose.yaml run automation pytest
# or
make docker-run
```

## Generate and View the Allure Report:

All test results and reports are saved in the allure-results directory.

The Allure Report provides the following insights:

- Test Status: Passed, Failed, and Skipped tests.
- Steps Execution: Detailed steps executed during the tests.
- Attachments: Screenshots, logs, or additional information on failure.

After the test execution, generate the Allure Report using the following command:

```sh
poetry run allure serve ./allure-results
# or
make report
```

> 	The report will automatically open in your default browser.

## Project Structure

The following is the clean directory structure of the project:

```plaintext
.
├── pages/                      # Page Object Model (POM) for different pages
│   ├── base_page.py            # Base class for all pages
│   ├── heroku/                 # Heroku-related page objects
│   ├── google/                 # Google-related page objects
├── src/                        # Core logic and helpers
│   ├── driver_factory.py       # WebDriver factory for Selenium
│   ├── driver_manager.py       # Manages WebDriver instances
│   ├── execution_manager.py    # Manages execution environment
│   ├── helpers/                # Helper utilities
└── .pytest.ini                 # Pytest configuration
```

## Best Practices

- Always use pre-commit to validate your code before each commit.
- Run tests locally and validate the environment before integrating with Selenium Grid.
- Use headless mode to optimize test execution in CI/CD environments.
