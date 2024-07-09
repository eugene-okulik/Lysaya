from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

TEST_URL = "https://www.qa-practice.com/elements/input/simple"
TEST_TEXT = "ABCD"


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_search_text(driver):
    driver.get(TEST_URL)
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "text_string"))
    )
    input_field.send_keys(TEST_TEXT)
    input_field.send_keys(Keys.ENTER)

    result_text = driver.find_element(By.ID, "result-text")
    assert result_text.text == TEST_TEXT
    print("Input text:", result_text.text)
