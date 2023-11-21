import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver = webdriver.Chrome()
chrome_driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(5)
chrome_driver.find_element(By.XPATH, value="//input[@name='username']").send_keys("Admin")
time.sleep(5)
link = chrome_driver.find_element(By.XPATH, value="//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p")
link.click()
time.sleep(5)
chrome_driver.find_element(By.XPATH, value="//input[@name='username']").send_keys("Admin")
time.sleep(5)
retest = chrome_driver.find_element(By.XPATH, value="//*[@id='app']/div[1]/div[1]/div/form/div[2]/button[2]")
retest.click()
time.sleep(5)
