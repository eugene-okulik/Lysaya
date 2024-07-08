from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pytest
import ipdb

TEST_URL = "https://demoqa.com/automation-practice-form"
FIRST_NAME = "First"
SECOND_NAME = "Second"
EMAIL = "firstsecond@test.test"
USER_NUMBER = "1234567890"
BIRTH_DATE = "01 Jun 2001"
MONTH = "June"
YEAR = "2012"
SUBJECT = "Computer Science"
ADDRESS = "Krasnaya 165, Minsk, Belarus"


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    # chrome_driver.maximize_window()
    yield chrome_driver


def test_form_filling(driver):
    driver.get(TEST_URL)
    driver.find_element(By.ID, "firstName").send_keys(FIRST_NAME)
    driver.find_element(By.ID, "lastName").send_keys(SECOND_NAME)
    driver.find_element(By.ID, "userEmail").send_keys(EMAIL)
    gender_radio_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='gender-radio-2']"))
    )
    gender_radio_button.click()
    driver.find_element(By.ID, "userNumber").send_keys(USER_NUMBER)
    # А после этого степа баг - при полном удалении даты появляется просто пустая страница.
    # driver.find_element(By.ID, "dateOfBirthInput").send_keys(BIRTH_DATE)
    driver.find_element(By.ID, "dateOfBirthInput").click()
    element = driver.find_element(By.TAG_NAME, "body")
    element.send_keys(Keys.END)
    month_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "react-datepicker__month-select"))
    )
    month_dropdown = Select(month_dropdown)
    month_dropdown.select_by_visible_text(MONTH)
    year_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "react-datepicker__year-select"))
    )
    year_dropdown = Select(year_dropdown)
    year_dropdown.select_by_visible_text(YEAR)
    driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day--0')]").click()
    driver.find_element(By.ID, "subjectsInput").send_keys(SUBJECT)
    driver.find_element(By.ID, "subjectsInput").send_keys(Keys.RETURN)
    hobbies_checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']"))
    )
    hobbies_checkbox.click()
    driver.find_element(By.ID, "currentAddress").send_keys(ADDRESS)

    state_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "state"))
    )
    state_dropdown.click()
    selected_state = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#state div.css-11unzgr"))
    )[-1]
    selected_state.click()
    city_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "city"))
    )
    city_dropdown.click()
    selected_city = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#city div.css-11unzgr"))
    )[0]
    selected_city.click()

    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit"))
    )
    submit_button.click()

    result_table = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='modal-content']//div[@class='table-responsive']//table"))
    )
    result_text = result_table.text
    print("Filled form data:\n", result_text)
