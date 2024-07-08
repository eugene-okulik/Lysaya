from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

TEST_URL = "https://the-internet.herokuapp.com/dynamic_loading/2"


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_displaying_text(driver):
    driver.get(TEST_URL)
    start_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='start']/button"))
    )
    start_button.click()
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.ID, "loading"))
    )
    hello_world_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )
    assert hello_world_text.text == "Hello World!"
    print(hello_world_text.text, "is displayed on the page")
