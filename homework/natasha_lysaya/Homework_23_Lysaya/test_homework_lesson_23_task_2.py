from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pytest

TEST_URL = "https://demoqa.com/automation-practice-form"
FIRST_NAME = "First"
SECOND_NAME = "Second"
EMAIL = "firstsecond@test.test"
USER_NUMBER = "1234567890"
MONTH = "June"
YEAR = "2012"
SUBJECT = "Computer Science"
ADDRESS = "Krasnaya 165, Minsk, Belarus"


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_form_filling(driver):
    driver.find_element_by_id("firstName").send_keys(FIRST_NAME)
    driver.find_element_by_id("lastName").send_keys(SECOND_NAME)
    driver.find_element_by_id("userEmail").send_keys(EMAIL)
    driver.find_element_by_id("gender-radio-1").click()
    driver.find_element_by_id("userNumber").send_keys(USER_NUMBER)
    driver.find_element_by_id("dateOfBirthInput").click()
    month_dropdown = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "react-datepicker__month-select"))
    )
    month_dropdown = Select(month_dropdown)
    month_dropdown.select_by_visible_text(MONTH)
    year_dropdown = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "react-datepicker__year-select"))
    )
    year_dropdown = Select(year_dropdown)
    year_dropdown.select_by_visible_text(YEAR)
    driver.find_element_by_xpath("//div[contains(@class, 'react-datepicker__day--0')]").click()

    driver.find_element_by_id("subjectsInput").send_keys(SUBJECT)
    driver.find_element_by_id("subjectsInput").send_keys(Keys.RETURN)
    driver.find_element_by_id("hobbies-checkbox-1").click()

    driver.find_element_by_id("currentAddress").send_keys(ADDRESS)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit"))
    )
    submit_button.click()

    result_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))
    ).text
    print("Текст после Submit:", result_text)
