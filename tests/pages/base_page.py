# pages/base_page.py
import logging
from typing import List
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException

from src.driver_manager import DriverManager

logger = logging.getLogger(__name__)


class LoggingWebElement:
    """TBD"""

    def __init__(self, element: WebElement, locator: tuple):
        """Wrapper para um WebElement com informações adicionais sobre o locator."""
        self.element = element
        self.locator = locator

    def click(self):
        """TBD"""
        logger.info("click on: [%s - %s]", self.locator[0], self.locator[1])
        self.element.click()

    def send_keys(self, value: str):
        """TBD"""
        logger.info("send keys '%s' on: [%s - %s]", value, self.locator[0], self.locator[1])
        self.element.send_keys(value)

    def __getattr__(self, item):
        """
        Encaminha outros métodos e atributos para o WebElement original.
        Isso permite que o LoggingWebElement seja tratado como um WebElement comum.
        """
        return getattr(self.element, item)


class BasePage:
    def __init__(self):
        self.driver = DriverManager.get_driver()
        self.timeout = 10

    def open(self, url):
        """Abre a URL no navegador"""
        logger.info("navigate to: %s", url)
        self.driver.get(url)

    def find_element(self, locator, timeout=0) -> LoggingWebElement:
        """Encontra um único elemento"""
        if timeout == 0:
            timeout = self.timeout
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return LoggingWebElement(element, locator)
        except TimeoutException:
            return None

    def find_elements(self, locator) -> List[LoggingWebElement]:
        """Encontra múltiplos elementos"""
        elements = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_all_elements_located(locator))
        return [LoggingWebElement(element, locator) for element in elements]

    def wait_for_element_to_be_clickable(self, locator) -> LoggingWebElement:
        """Espera até que o elemento seja clicável"""
        element = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))
        return LoggingWebElement(element, locator)
