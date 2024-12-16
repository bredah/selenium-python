"""TBD"""

import logging
import os
import platform

import allure
import pytest

from src.driver_manager import DriverManager

logger = logging.getLogger(__name__)


@pytest.fixture(scope="session", autouse=True)
def fixture_session():
    """
    Fixture de sessão para inicializar e finalizar o driver Selenium.
    Essa fixture é executada automaticamente no início e no fim da sessão de testes.
    """
    logger.info("session - before")
    with DriverManager() as driver:
        yield driver  # Driver estará disponível para toda a sessão
    logger.info("session - after")


@pytest.fixture(scope="package", autouse=True)
def fixture_package():
    logger.info("package - before")
    yield
    logger.info("package - after")


@pytest.fixture(scope="module", autouse=True)
def fixture_module():
    logger.info("module - before")
    yield
    logger.info("module - after")


@pytest.fixture(scope="class", autouse=True)
def fixture_class():
    logger.info("class - before")
    yield
    logger.info("class - after")


@pytest.fixture(scope="function", autouse=True)
def fixture_test():
    logger.info("test - before")
    yield
    logger.info("test - after")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook do pytest para capturar o relatório do teste e anexar a screenshot em caso de falha.
    """
    outcome = yield
    report = outcome.get_result()

    # Captura a screenshot apenas se o teste falhar
    if report.when == "call" and report.failed:
        screenshot = DriverManager.get_driver().get_screenshot_as_png()
        allure.attach(screenshot, name=item.name, attachment_type=allure.attachment_type.PNG)


def pytest_sessionfinish(session):
    """
    Hook para configurar o pytest e gerar o arquivo environment.properties.
    """
    allure_results_dir = session.config.getoption("--alluredir") or "allure-results"
    environment_file = os.path.join(allure_results_dir, "environment.properties")

    os.makedirs(allure_results_dir, exist_ok=True)

    environment_data = {
        "BROWSER_NAME": os.getenv("BROWSER_NAME"),
        "BROWSER_VERSION": os.getenv("BROWSER_VERSION"),
        "HEADLESS": os.getenv("HEADLESS", "false"),
    }

    with open(environment_file, "w", encoding="utf-8") as file:
        for key, value in environment_data.items():
            file.write(f"{key}={value}\n")
