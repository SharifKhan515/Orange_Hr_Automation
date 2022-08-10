from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class VacancyPage(BasePage):
    JOB_TITLE_DROPDOWN = (By.XPATH, "//select[@id='vacancySearch_jobTitle']")
    SEARCH_BUTTON = (By.XPATH, "//input[@id='btnSrch']")
    RESULT_TABLE = (By.XPATH, "//table[@id='resultTable']")
    RESULT_TABLE_TOTAL_COLS = (By.XPATH, "//table[@id='resultTable']/tbody/tr/td")
    RESULT_TABLE_VACANCY = (By.XPATH, "//table[@id='resultTable']/tbody/tr/td[2]")
    RESULT_TABLE_JOB_TITLE = (By.XPATH, "//table[@id='resultTable']/tbody/tr/td[3]")

    # RESULT_TABLE_JOB_TITLE = (By.XPATH, "./tbody/tr/td[3]")
    # RESULT_TABLE_VACANCY = (By.XPATH, "./tbody/tr/td[2]")

    def __init__(self, driver):
        super().__init__(driver)
        # self.driver = driver

    def set_job_title_from_dropdown(self, title):
        self.do_select_from_dropdown(self.JOB_TITLE_DROPDOWN, title)

    def click_search(self):
        self.do_click(self.SEARCH_BUTTON)

    def result_table_has_entry(self):
        self.check_element_visibility(self.RESULT_TABLE)
        elements = self.driver.find_elements(*self.RESULT_TABLE_TOTAL_COLS)
        if len(elements) != 1:
            return True
        else:
            return False

    def get_job_title_list_from_result(self):
        self.check_element_visibility(self.RESULT_TABLE)
        elements = self.get_element_list(self.RESULT_TABLE_JOB_TITLE)
        job_title_list = []
        for element in elements:
            job_title_list.append(element.text)

        return job_title_list
