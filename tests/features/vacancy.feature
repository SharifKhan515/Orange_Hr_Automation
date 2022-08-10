Feature: Vacancy Feature
  As an admin
  I want to see and filter vacancies listed
  in Recruitment-Vacancies page

  Background:
    Given I am at login page of OrangeHrm
    And Login as admin

  Scenario: Job title filter is returning correct vacancy
    Given I hover over Recruitment button and click on Vacancy
    When  I applied filter "QA Lead" in Job Title field
    And  I click on search button
    Then I should see atleast one vacancy for Job title "QA Lead"

