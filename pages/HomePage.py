from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class HomePage(BasePage):
    WELCOME_PANEL = (By.XPATH, "//a[@id='welcome']")
    RECRUITMENT_BUTTON = (By.XPATH, "//a[@id='menu_recruitment_viewRecruitmentModule']")
    JOB_VACANCY_BUTTON = (By.XPATH, "//a[@id='menu_recruitment_viewJobVacancy']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_welcome_text(self):
        return self.get_text(self.WELCOME_PANEL)

    def click_recruitment(self):
        self.do_click(self.RECRUITMENT_BUTTON)

    def click_job_vacancy_using_hover_over_recruitment(self):
        self.do_mouse_hover(self.RECRUITMENT_BUTTON)
        self.do_click(self.JOB_VACANCY_BUTTON)
