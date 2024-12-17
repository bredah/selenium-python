"""pages/google_page.py"""

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.google import BASE_URL


class GooglePage(BasePage):
    """TBD"""

    # def __init__(self):
    #     super().__init__()

    def open(self, url=None) -> None:
        """TBD"""
        super().open(url=f"{BASE_URL}/")

    def _accept_terms(self):
        button_accept_all = self.find_element((By.CSS_SELECTOR, "div > button:nth-of-type(2)"), 1)
        if button_accept_all:
            button_accept_all.click()

    def search(self, query):
        """Realiza uma pesquisa no Google"""
        self._accept_terms()
        search_box = self.find_element((By.NAME, "q"))
        search_box.send_keys(query)
        search_button = self.wait_for_element_to_be_clickable((By.NAME, "btnK"))
        search_button.click()

    def get_results(self):
        """Retorna os títulos dos resultados de pesquisa"""
        result_elements = self.find_elements((By.CSS_SELECTOR, "a h3"))
        return [element.text for element in result_elements]
