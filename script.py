from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(2)


driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)


sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
sort_dropdown.select_by_visible_text("Price (low to high)")
time.sleep(1)


first_add_button = driver.find_element(By.XPATH, "(//button[text()='Add to cart'])[1]")
first_add_button.click()
time.sleep(1)


driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(1)


driver.find_element(By.ID, "checkout").click()
time.sleep(1)


first_name = driver.find_element(By.ID, "first-name")
last_name = driver.find_element(By.ID, "last-name")
postal_code = driver.find_element(By.ID, "postal-code")

if first_name.is_displayed() and last_name.is_displayed() and postal_code.is_displayed():
    print("Checkout form is visible. Test passed!")
else:
    print(" Checkout form is not displayed. Test failed.")


first_name.send_keys("John")
last_name.send_keys("Doe")
postal_code.send_keys("12345")
time.sleep(1)


driver.find_element(By.ID, "cancel").click()
driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(1)
driver.find_element(By.ID, "logout_sidebar_link").click()

print("Logged out and test complete.")


driver.quit()