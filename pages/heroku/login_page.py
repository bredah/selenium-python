"""TBD"""

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.heroku import BASE_URL


class LoginPage(BasePage):
    """TBD"""

    def __init__(self):
        """TBD"""
        super().__init__()
        self.input_username = (By.ID, "username")
        self.input_password = (By.ID, "password")
        self.button_login = (By.XPATH, "//button")
        self.label_message = (By.ID, "flash")

    def open(self, url=None) -> None:
        """TBD"""
        super().open(url=f"{BASE_URL}/login")

    @allure.step
    def access_account(self, username: str, password: str) -> None:
        self.find_element(self.input_username).send_keys(username)
        self.find_element(self.input_password).send_keys(password)
        self.find_element(self.button_login).click()

    @allure.step
    def get_message(self) -> str:
        self.wait_presence_of_element(self.label_message)
        return self.find_element(self.label_message).text
