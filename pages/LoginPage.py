from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class LoginPage(BasePage):
    USER = (By.XPATH, "//input[@id='txtUsername']")
    PASSWORD = (By.XPATH, "//input[@id='txtPassword']")
    LOGIN_BUTTON = (By.XPATH, "//input[@id='btnLogin']")

    def __init__(self, driver):
        super().__init__(driver)

    def set_user(self, username):
        self.do_send_keys(self.USER, username)

    def set_password(self, password):
        self.do_send_keys(self.USER, password)

    def click_login(self):
        self.do_click(self.LOGIN_BUTTON)

    def do_login(self, username, password):
        self.do_send_keys(self.USER, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
