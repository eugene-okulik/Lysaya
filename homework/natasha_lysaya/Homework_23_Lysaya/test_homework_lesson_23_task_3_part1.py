from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

TEST_URL = "https://www.qa-practice.com/elements/select/single_select"
LANGUAGE = "Ruby"


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_select_language(driver):
    driver.get(TEST_URL)
    select_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "id_choose_language"))
    )
    select_element.click()
    driver.find_element(By.XPATH, f"//option[text()='{LANGUAGE}']").click()
    driver.find_element(By.TAG_NAME, "body").click()

    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit-id-submit"))
    )
    submit_button.click()

    selected_language = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "result-text"))
    )
    result_text = selected_language.text
    assert LANGUAGE in result_text
    print("Selected language:", result_text)
