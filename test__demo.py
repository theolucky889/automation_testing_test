from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

# set options for not prompting devtools info
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

print("testing started")
driver = webdriver.Chrome(options=options)

driver.get("https://wwww.saucedemo.com/")
sleep(3)

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, ("login-button").click())
sleep(5)

# test if login success
text = driver.find_element(By.CLASS_NAME, "title").text

assert "products" in text.lower()

print("TEST PASSED : LOGGIN SUCCESSFULL")

# close the driver
driver.quit()