from assertpy import assertpy
from pytest_bdd import scenarios, when, then, parsers

from pages.HomePage import HomePage

scenarios('../features/login.feature')


@when(parsers.parse('I enter "{username}" in user field "{password}" in password field and click login'))
def login_with_credential(browser, login_page, username, password):
    login_page.do_login(username, password)


@then(parsers.parse('I should see Welcome text'))
def verify_login(browser):
    home_page = HomePage(browser)
    welcome_text = home_page.get_welcome_text()
    assertpy.assert_that(welcome_text, description="Login Failed").starts_with('Welcome')
