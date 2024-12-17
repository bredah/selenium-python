"""pages/base_page.py"""

import logging
from typing import List

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

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
        logger.info("clicked on element: [%s = '%s']", self.locator[0], self.locator[1])
        self.element.click()

    def send_keys(self, value: str):
        """TBD"""
        logger.info("sent keys '%s' to element: [%s = '%s']", value, self.locator[0], self.locator[1])
        self.element.send_keys(value)

    def select_by_text(self, text: str) -> None:
        """TBD"""
        logger.info("selected option by visible text '%s' from element: [%s = '%s']", text, self.locator[0], self.locator[1])
        dropdown = Select(self.element)
        dropdown.select_by_visible_text(text)

    def select_by_index(self, index: int) -> None:
        """TBD"""
        logger.info("selected option by index '%d' from element: [%s = '%s']", index, self.locator[0], self.locator[1])
        dropdown = Select(self.element)
        dropdown.select_by_index(index)

    def select_get_value(self) -> str:
        """TBD"""
        logger.info("retrieved selected option from element: [%s = '%s']", self.locator[0], self.locator[1])
        dropdown = Select(self.element)
        return dropdown.first_selected_option.text

    def __getattr__(self, item):
        """
        Encaminha outros métodos e atributos para o WebElement original.
        Isso permite que o LoggingWebElement seja tratado como um WebElement comum.
        """
        return getattr(self.element, item)


class BasePage:
    """TBD"""

    def __init__(self):
        self.driver = DriverManager.get_driver()
        self.timeout = 10

    @allure.step
    def open(self, url) -> None:
        """Abre a URL no navegador"""
        logger.info("navigate to: %s", url)
        self.driver.get(url)

    def find_element(self, locator, timeout=10) -> LoggingWebElement:
        """Encontra um único elemento"""
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

    def wait_presence_of_element(self, locator) -> LoggingWebElement:
        """TBD"""
        element = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
        return LoggingWebElement(element, locator)

    def demo(self, var1, var2, var3, var4, var5, var6, var7):
        """tbd"""
