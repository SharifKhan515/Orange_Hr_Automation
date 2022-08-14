import json
import assertpy
import pytest
from pytest_bdd import given
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from config.environment import Environment
from pages.LoginPage import LoginPage
from utility.logger import *


def pytest_addoption(parser):
    """Capture command line arguments"""
    parser.addoption("--browser", action="store", default="", help="Provide browser. e.g: chrome or firefox")
    parser.addoption("--headless", action="store", default="", help="headless mode true or false")


def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    log_message(f'{step} executed successfully')


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    """Take screenshot after step failure and attach screenshot and log to report"""
    driver = step_func_args['browser']
    log_message(f'{step_func} is failed', "error")
    attach_screenshot(driver, step_func)


@pytest.fixture
def config(request, scope='session'):
    """Reading config file and command line input"""
    supported_browser = ['chrome', 'firefox']
    provided_browser = request.config.getoption("--browser")
    provided_headless = request.config.getoption("--headless")

    with open('config/config.json') as config_file:
        config = json.load(config_file)
        config["browser"] = config["browser"].lower()

    if len(provided_browser) > 1:
        config["browser"] = provided_browser.lower()
    if provided_headless.lower() == 'false':
        config["headless"] = False
    elif provided_headless.lower() == 'true':
        config["headless"] = True

    assertpy.assert_that(supported_browser, description=f'{config["browser"]} is not supported').contains(
        config["browser"])
    assertpy.assert_that(config["headless"], description=f'Provided value for headless is not boolean').is_type_of(bool)

    return config


@pytest.fixture
def browser(config):
    if config["browser"] == "chrome":
        opts = webdriver.ChromeOptions()
        if config['headless']:
            opts.add_argument('headless')
        web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
    elif config["browser"] == "firefox":
        opts = webdriver.FirefoxOptions()
        if config['headless']:
            opts.headless = True
        web_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=opts)
    else:
        raise Exception(f'Provide browser "{config["browser"]}" is not supported')

    web_driver.maximize_window()
    web_driver.implicitly_wait(Environment.IMPLICIT_WAIT)
    yield web_driver
    web_driver.quit()


@given('I am at login page of OrangeHrm', target_fixture='login_page')
def navigate_to_login_page(browser):
    browser.get(Environment.BASE_URL)
    return LoginPage(browser)


@given('Login as admin')
def admin_login(browser, login_page):
    login_page.do_login(Environment.USER_NAME, Environment.PASSWORD)
