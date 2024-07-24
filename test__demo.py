from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

# set options for not prompting devtools info
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

print("testing started")
driver = webdriver.Chrome(options=options)

driver.get("https://www.saucedemo.com/")
sleep(3)

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
sleep(5)

# test if login success
text = driver.find_element(By.CLASS_NAME, "title").text

assert "products" in text.lower()

print("TEST PASSED : LOGIN SUCCESSFULL", "\n")

# add to cart test
print("testing add to cart")
add_to_cart_btn = driver.find_elements(By.CLASS_NAME, "btn_inventory")

# click three buttons to make the cart_value 3
for btns in add_to_cart_btn[:3]:
    btns.click()

cart_value = driver.find_element(By.CLASS_NAME, "shopping_cart_container")
assert "3" in cart_value.text
print("TEST PASSED : ADD TO CART", "\n")

# test remove from cart
print("test remove from cart")
remove_btn = driver.find_elements(By.CLASS_NAME, "btn_inventory")
for btns in remove_btn[:2]:
    btns.click()
assert "1" in cart_value.text # there should be 1 item in the cart left
print("TEST PASSED : REMOVE FROM CART", "\n")

# Test search filter NAME Z to A
print("Test sorting Name Z to A")
active = driver.find_element(By.CLASS_NAME, "active_option")
driver.find_element(By.CLASS_NAME, "product_sort_container").click()
driver.find_element(By.XPATH, '//*[@value="az"]').click()

assert "Name (Z to A)" in active
print("TEST PASSED : SORTING FILTER")

# close the driver
driver.quit()