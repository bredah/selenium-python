import pytest

from pages.heroku.login_page import LoginPage


@pytest.fixture(name="login_page")
def setup_page():
    return LoginPage()


def test_should_login_successfully(login_page):
    login_page.open()
    login_page.access_account("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area!" in login_page.get_message()


@pytest.mark.parametrize(
    "username,password,expected_message",
    [
        ("tomsmit", "SuperSecretPassword!", "Your username is invalid!"),
        ("", "SuperSecretPassword!", "Your username is invalid!"),
        ("tomsmith", "SuperSecretPassword", "Your password is invalid!"),
        ("tomsmith", "", "Your password is invalid!"),
        ("", "", "Your username is invalid!"),
    ],
)
def test_should_login_unsuccessfully(login_page, username, password, expected_message):
    login_page.open()
    login_page.access_account(username, password)
    assert expected_message in login_page.get_message()
