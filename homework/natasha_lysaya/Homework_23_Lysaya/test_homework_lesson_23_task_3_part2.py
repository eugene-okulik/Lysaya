from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TEST_URL = "https://the-internet.herokuapp.com/dynamic_loading/2"

driver = webdriver.Chrome()
driver.get(TEST_URL)

try:
    start_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Start')]"))
    )
    start_button.click()

    hello_world_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h4[text()='Hello World!']"))
    )

    assert hello_world_text.text == "Hello World!"
    print("Текст 'Hello World!' доступен на странице.")

finally:
    driver.quit()
