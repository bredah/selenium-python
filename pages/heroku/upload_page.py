"""TBD"""

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.heroku import BASE_URL


class UploadPage(BasePage):
    """TBD"""

    def __init__(self):
        """TBD"""
        super().__init__()
        self.upload_input = (By.ID, "file-upload")
        self.upload_button = (By.ID, "file-submit")
        self.validation_message_label = (By.CSS_SELECTOR, "h3")
        self.validation_file_label = (By.ID, "uploaded-files")

    def open(self, url=None) -> None:
        """TBD"""
        super().open(url=f"{BASE_URL}/upload")

    @allure.step
    def upload(self, file: str) -> None:
        self.find_element(self.upload_input).send_keys(file)
        self.find_element(self.upload_button).click()

    @allure.step
    def get_info(self) -> tuple[str, str]:
        message = self.find_element(self.validation_message_label).text
        file = self.find_element(self.validation_file_label).text
        return (message, file)
