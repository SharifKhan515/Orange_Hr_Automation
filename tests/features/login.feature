Feature: Login feature
  As an admin
  I want to login to OrangeHrm Successfully
  with valid Credential

  Background:
     Given I am at login page of OrangeHrm

  Scenario Outline: Login with credential
    When I enter "<username>" in user field "<password>" in password field and click login
    Then I should see Welcome text
    Examples:
    | username | password     |
    | Admin    | @qPJ@X7@2gPp |
    | Admin    | admin123     |
