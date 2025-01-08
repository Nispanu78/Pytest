import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


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
    # Set up the WebDriver (Chrome in this example)
    driver = webdriver.Chrome()  # Ensure you have the ChromeDriver installed
    driver.get("https://www.saucedemo.com/")
    yield driver
    # Tear down the WebDriver
    driver.quit()


# Test function using parameterized inputs
@pytest.mark.parametrize("username,password", get_data())
def test_login(browser, username, password):
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

    # Assert that login is successful
    assert "Swag Labs" in browser.page_source
