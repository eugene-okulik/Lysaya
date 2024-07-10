from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
import pytest

TEST_URL = "https://www.demoblaze.com/index.html"
PRODUCT = "Sony xperia z5"


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_shopping_cart(driver):
    driver.get(TEST_URL)
    selected_phone = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//a[contains(text(), '{PRODUCT}')]"))
    )
    selected_phone.send_keys(Keys.CONTROL + Keys.RETURN)
    driver.switch_to.window(driver.window_handles[1])
    product_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h2.name"))
    ).text
    assert PRODUCT == product_name, f"{PRODUCT} isn't the same as {product_name}"
    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn-success"))
    )
    add_button.click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = Alert(driver)
    alert.accept()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.ID, "cartur").click()
    added_product = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//td[contains(text(), 'Sony xperia z5')]"))
    ).text

    assert added_product == PRODUCT, f"'{added_product} has been added to the cart instead '{PRODUCT}'"
