from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()

options.add.experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
