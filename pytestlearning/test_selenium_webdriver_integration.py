# To run tests in parallel mode pytest-xdist needs to be installed with pip
# To run tests in parallel, use the -n flag followed by the number of processes you want to use

# pytest test_selenium_webdriver_integration.py
# To generate reports pytest-html needs to be installed with pip then run the test with the flag: --html=testreports.html

# To use allure_reports install it with pip (pip install allure-pytest), run your test
# then generate the HTML version of the report with allure serve ./allure_reports

import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# Function to provide test data
def get_data():
    return [
        ("standard_user", "secret_sauce"),
        ("problem_user", "secret_sauce"),
        ("error_user", "secret_sauce"),
    ]

# Pytest fixture for setting up and tearing down the Selenium WebDriver
@pytest.fixture(scope="function")
def browser():
    # Configure WebDriver options
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Optional: Run in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Set up the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

# Test function using parameterized inputs
@pytest.mark.parametrize("username,password", get_data())
def test_login(browser, username, password):
    with allure.step("Input username and password"):
        # Locate username and password fields
        username_field = browser.find_element(By.ID, "user-name")
        password_field = browser.find_element(By.ID, "password")
        submit_button = browser.find_element(By.ID, "login-button")

        # Input username and password
        username_field.clear()
        username_field.send_keys(username)
        password_field.clear()
        password_field.send_keys(password)

        # Submit the form (simulating a login)
        submit_button.click()
        time.sleep(3)
    # In case of failure a screen-shot is generated
    try:
        with allure.step("Assert login failure"):
            assert "Fail" in browser.page_source
    except Exception as e:
        # Capture screenshot on failure
        allure.attach(
            browser.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG,
        )
        raise e
