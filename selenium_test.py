from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

# set options for not prompting DevTools info
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

print("testing started")
driver = webdriver.Chrome(options=Options)
driver.get("https://www.saucedemo.com/")
sleep(3)

# get page title
title = driver.title

# test if title is correct
assert "Swag Labs" in title
print("TEST 0: 'title' test passed")


# close driver
driver.quit()