import time
from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_driver = webdriver.Chrome()
chrome_driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(3)
chrome_driver.find_element(By.XPATH, value ="//input[@name='username']").send_keys("Admin")
password = "admin123"
chrome_driver.find_element(By.XPATH, value ="//input[@name='password']").send_keys(password)
login = chrome_driver.find_element(By.XPATH, value="//button[@type='submit']")
login.click()
time.sleep(15)
