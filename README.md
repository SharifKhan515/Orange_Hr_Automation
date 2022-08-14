

# Orange_Hr_Automation: Pytest-bdd with Page Object Model

OrangeHr Automation is a test automation project. Website is  in test is [OrangeHr](https://opensource-demo.orangehrmlive.com/index.php/dashboard).Login and Vacancy page filter test is automated as part of this project

This project provides an example for testing a UI with Selenium WebDriver, using the Page Object Model design pattern and driven via BDD feature files through Pytest BDD.

## Framework Overview
 As stated above, this project contains a Selenium Python test framework, implements the Page Object Model design pattern and utilizes Pytest BDD. As such, it follows test automation best practices. 

The Page Object Model means that each individual webpage has its own class, each containing the methods specific to controls on that page. Thus, each page is independent and separate from the tests, meaning any changes to the page are isolated to only the corresponding page class. This makes for code that is cleaner, easier to read and maintain, and contains less duplication.

The use of Gherkin-style BDD means the tests themselves are also clean and clear, written in plain English, so they can be understood by anyone working with the project, including non-technical roles. 

This project integrated Allure reporting which is neat and clear to understand and provide a nice and clean looking report after test execution 

## Technology
As this is a Python project, build and dependency management is handled by Pipenv, so there is a Pipfile (and associated .lock file) defining the versions of the dependencies:
1. Selenium [v4.4.0]
2. Webdriver manager [v3.8.3]
3. Pytest [v7.1.2]
4. Pytest-bdd [v6.0.1]
5. Assertpy [v1.1]
6. Allure-pytest [v2.9.45]

Selenium is used to automate the browser interaction to simulate the operations on page. Webdriver manager is used to manage the driver for browser interaction. Pytest is used as main validation framework where Pytest-bdd drive the test in bdd fashion.

Third party tool assertpy is used for assertion as its provide many assertion method out of the box.

Finally, Allure generate the report and attach the log and screenshot in report. Pytest-bdd hooks are utilize to  generate log and attach screenshot on test failure.

## Project Structure

The project uses a standard structure and naming convention (hopefully):
- **tests** : Standard tests folder which contains both **features** and **step_def** subdirectory.

- **features**  : this folder contains the Gherkin .feature files, one per website page. Each feature file is named after the page it test. e.g: login.feature, vacancy.feature

- **step_def**  : as name suggest it contains the step_def file for each feature file. each file contains step_def for a single feature file. pytest naming convention is followed for file name.

- **pages**  : the Page Object Model implementation of the individual website pages, one class file per page. Each class is named after the corresponding page e.g. LoginPage, HomePage etc.There is also a BasePage which the other page classes implement/extend through inheritance. BasePage contains all kind of shared methods implementation which other class used.

- **config**  : This directory contains config.json and environment class which set up the default environment of the project.

- **utility** : This directory contains the utility function needed throughout the test. right now, it has logger and screenshot method for framework.

- **pytest.ini**  : contains the pytest config
- **conftest.py**  :  contains necessary hooks, fixture and step_definition(given) which needed for more than one feature files. 

## Supported Browsers
The conftest.py module uses the Webdriver-Manager dependency to manage the various browser drivers. The browser Pytest fixture returns the relevant WebDriver instance for the chosen browser, with support for:

 - Chrome - the default option
 -  Firefox
 
The **browser** to be used can be passed in via a Pytest command line parameter with a key of `--browser`, defaulting to Chrome if no such property is specified. Alternatively, the browser parameter can be configured via the config.json file.

The **headless** property is used to determine whether the browser should run in headless mode it can be passed via a  Pytest command line parameter with a key of `--headless` . headless is `true` by default but default value can be changed in the config.json file.

The Webdriver-Manager plugin also has support for Edge, Opera and Internet Explorer but those options are not enabled yet.

##  Execute Test

To run the project first make sure you have python installed in your system if not please install python. this code is written using python 3.8.so you need python 3.8 to run this project. if you want to run the project with other version then edit the pipfile python version though it is not recommended because it may lead to some other version mismatch issue.

 As Pipenv is being used for dependency management. you can install the dependency by move to root directory of the project where pipfile is located and run using  command
 
    pipenv install

After dependency is install run below command to ruin the test with default options. 

    pipenv run pytest 
additionally you can provide `--browser` and `--headless` flag to run with different combinations. e.g:

    pipenv run pytest --browser Firefox --headless true

## Test Report
Allure is used for test reporting. so you need to install allure package in your system to generate the report in a human viewable state. Follow this page to install the [Allure](https://docs.qameta.io/allure/)

After tests execution completed test result with screenshot and log  will be store at **report** directory. Run below command in root directory to generate and view the report in browser

    allure serve report

## N.B. 
OrangeHr is an opensource project. Anyone can change the default credentials provided in their login page. In that case test will fail as credential is not valid to login and do further testing. OrangeHr credential is reset to its default after every 24 hours.
