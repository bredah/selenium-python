"""TBD"""

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.heroku import BASE_URL


class DropdownPage(BasePage):
    """TBD"""

    def __init__(self):
        """TBD"""
        super().__init__()
        self.dropdown = (By.ID, "dropdown")

    def open(self, url=None) -> None:
        """TBD"""
        super().open(url=f"{BASE_URL}/dropdown")

    @allure.step
    def select(self, value) -> None:
        """TBD"""
        dropdown = self.find_element(self.dropdown)
        if isinstance(value, int):
            dropdown.select_by_index(value)
        if isinstance(value, str):
            dropdown.select_by_text(value)

    @allure.step
    def get_value(self) -> str:
        """TBD"""
        dropdown = self.find_element(self.dropdown)
        return dropdown.select_get_value()
