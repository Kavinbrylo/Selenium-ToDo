from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


driver = webdriver.Chrome()
file_path = os.path.abspath("crud_sample.html")
driver.get("file://" + file_path)
time.sleep(2)
driver.save_screenshot("1_loaded_page.png")


driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("admin")
driver.find_element(By.XPATH, "//button[text()='Login']").click()
time.sleep(2)
driver.save_screenshot("2_after_login.png")

for i, item in enumerate(["Apple", "Banana", "Cherry"], start=1):
    input_field = driver.find_element(By.ID, "new-item")
    input_field.clear()
    input_field.send_keys(item)
    driver.find_element(By.XPATH, "//button[text()='Add']").click()
    time.sleep(1)
    driver.save_screenshot(f"3_added_{item}.png")

delete_buttons = driver.find_elements(By.XPATH, "//ul[@id='item-list']//button[text()='Delete']")
if len(delete_buttons) > 1:
    delete_buttons[1].click()  
    time.sleep(2)
    driver.save_screenshot("4_after_deleting_banana.png")

driver.find_element(By.ID, "logout-btn").click()
time.sleep(2)
driver.save_screenshot("5_after_logout.png")

driver.quit()
