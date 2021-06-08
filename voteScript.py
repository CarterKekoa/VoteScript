import time
# importing webdriver from selenium
from selenium import webdriver
import os
import subprocess
 
print("1")
# Here Chrome  will be used
PATH = "/usr/bin/chromedriver"
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")
print("2: ", PROJECT_ROOT)
print("3: ", DRIVER_BIN)
print("2")
driver = webdriver.Chrome(PATH)
print("4")
# URL of website
url = "https://www.heraldnet.com/sports/vote-for-the-heralds-prep-athlete-of-the-week-for-april-12-18/"
print("5")
# Opening the website
driver.get(url)
print(driver)
 
# getting the button by class name
button = driver.find_element_by_class_name("slide-out-btn")
 
# clicking on the button
button.click()