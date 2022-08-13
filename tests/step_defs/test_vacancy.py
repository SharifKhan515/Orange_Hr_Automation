from assertpy import assertpy
from pytest_bdd import scenarios, when, then, parsers, given
from pages.HomePage import HomePage
from pages.VacancyPage import VacancyPage

scenarios('../features/vacancy.feature')


@given('I hover over Recruitment button and click on Vacancy', target_fixture="vacancy_page")
def click_vacancy_by_hovering_over_recruitment(browser):
    home_page = HomePage(browser)
    home_page.click_job_vacancy_using_hover_over_recruitment()
    return VacancyPage(browser)


@when(parsers.parse('I applied filter "{job_title}" in Job Title field'))
def apply_filter(browser, vacancy_page, job_title):
    vacancy_page.set_job_title_from_dropdown(job_title)


@when('I click on search button')
def click_search(browser, vacancy_page):
    vacancy_page.click_search()


@then(parsers.parse('I should see atleast one vacancy for Job title "{job_title}"'))
def click_search(browser, vacancy_page, job_title):
    assertpy.assert_that(vacancy_page.result_table_has_entry(),
                         description=f'Result Not Found in Result Table for {job_title}').is_true()
    vacancy_list = vacancy_page.get_job_title_list_from_result()
    assertpy.assert_that(vacancy_list, description=f'{job_title} Not Found in Search Result').contains(job_title)
