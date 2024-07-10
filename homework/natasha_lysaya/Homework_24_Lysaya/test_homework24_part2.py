from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from time import sleep

TEST_URL = "https://magento.softwaretestingboard.com/gear/bags.html"


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_add_product_to_compare(driver):
    driver.get(TEST_URL)
    first_product = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".products-grid .product-item:first-child"))
    )
    first_product_name = first_product.find_element(By.CSS_SELECTOR, ".product-item-link").text
    actions = ActionChains(driver)
    actions.move_to_element(first_product).perform()
    add_to_compare_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".products-grid .product-item:first-child .actions-secondary .tocompare"))
    )
    add_to_compare_button.click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".block.block-compare")))
    compare_product = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".block.block-compare .product-item .product-item-name"))
    )
    compare_product_name = compare_product.text
    assert compare_product_name == first_product_name
