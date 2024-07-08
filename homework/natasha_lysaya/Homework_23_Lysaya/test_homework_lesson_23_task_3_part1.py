from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TEST_URL = "https://www.qa-practice.com/elements/select/single_select"

driver = webdriver.Chrome()
driver.get(TEST_URL)

try:
    select_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "select_input"))
    )
    select_element.click()
    option_to_select = driver.find_element_by_xpath("//option[text()='Option 3']")
    option_to_select.click()

    submit_button = driver.find_element_by_id("submit_button")
    submit_button.click()

    result_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "select_result"))
    )

    result_text = result_element.text
    print("Текст после Submit:", result_text)

finally:
    driver.quit()
