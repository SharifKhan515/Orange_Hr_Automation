from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from config.environment import Environment


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator, explicit_wait=Environment.EXPLICIT_WAIT):
        WebDriverWait(self.driver, explicit_wait).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text, explicit_wait=Environment.EXPLICIT_WAIT):
        element = WebDriverWait(self.driver, explicit_wait).until(EC.visibility_of_element_located(by_locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, by_locator, explicit_wait=Environment.EXPLICIT_WAIT):
        element = WebDriverWait(self.driver, explicit_wait).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def do_mouse_hover(self, by_locator, explicit_wait=Environment.EXPLICIT_WAIT):
        element = WebDriverWait(self.driver, explicit_wait).until(EC.visibility_of_element_located(by_locator))
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def do_select_from_dropdown(self, by_locator, option, explicit_wait=Environment.EXPLICIT_WAIT):
        element = WebDriverWait(self.driver, explicit_wait).until(EC.visibility_of_element_located(by_locator))
        element.click()
        select = Select(element)
        select.select_by_visible_text(option)

    def check_element_visibility(self, by_locator, explicit_wait=Environment.EXPLICIT_WAIT):
        WebDriverWait(self.driver, explicit_wait).until(EC.visibility_of_element_located(by_locator))

    def get_element_list(self, by_locator, explicit_wait=Environment.EXPLICIT_WAIT):
        return WebDriverWait(self.driver, explicit_wait).until(EC.visibility_of_all_elements_located(by_locator))
