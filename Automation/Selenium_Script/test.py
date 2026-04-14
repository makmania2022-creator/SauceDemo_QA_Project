from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Edge()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()


driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.save_screenshot("credentials_entered.png")
driver.find_element(By.ID, "login-button").click()

sleep(2)


driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
print("Product added to cart")
driver.save_screenshot("product_added.png")

sleep(2)

driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
print("Product removed from cart")
driver.save_screenshot("product_removed.png")

driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
print("Cart opened")

driver.find_element(By.XPATH, "//*[@id='react-burger-menu-btn']").click()
sleep(2)
driver.find_element(By.XPATH, "//*[@id='logout_sidebar_link']").click()
print("Logged out")

sleep(2)

driver.quit()
