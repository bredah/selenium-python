import pytest

from pages.heroku.dropdown_page import DropdownPage


@pytest.fixture(name="dropdown_page")
def setup_page():
    return DropdownPage()


def test_dropdown_by_text(dropdown_page):
    dropdown_page.open()
    dropdown_page.select("Option 1")
    result = dropdown_page.get_value()
    assert result == "Option 1"


def test_dropdown_by_index(dropdown_page):
    dropdown_page.open()
    dropdown_page.select(1)
    result = dropdown_page.get_value()
    assert result == "Option 1"
