import pytest
from pytest_bdd import given
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from config.config import TestData
from pages.LoginPage import LoginPage


@pytest.fixture
def browser():
    # if request.param == "Chrome":
    #     web_driver = webdriver.Chrome(ChromeDriverManager().install())
    # elif request.param == "Firefox":
    #     web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    web_driver.maximize_window()
    web_driver.implicitly_wait(TestData.IMPLICIT_WAIT)
    yield web_driver
    web_driver.quit()


@given('I am at login page of OrangeHrm', target_fixture='login_page')
def navigate_to_login_page(browser):
    browser.get(TestData.BASE_URL)
    return LoginPage(browser)


@given('Login as admin')
def admin_login(login_page):
    login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
