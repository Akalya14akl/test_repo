import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver = webdriver.Chrome()
chrome_driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(3)
chrome_driver.find_element(By.XPATH, value="//input[@name='username']").send_keys("Admin")
password = "admin123"
chrome_driver.find_element(By.XPATH, value="//input[@name='password']").send_keys(password)
login = chrome_driver.find_element(By.XPATH, value="//button[@type='submit']")
login.click()
time.sleep(3)
pim = chrome_driver.find_element(By.XPATH,
                                 value=" (//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[2]")
pim.click()
time.sleep(3)
employee_list = chrome_driver.find_element(By.XPATH,
                                           value="//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div[4]/div/div/div[1]/div[1] ")
employee_list.click()
time.sleep(5)
employee_select = chrome_driver.find_element(By.XPATH, value="//div[@class='orangehrm-container']")
employee_select.click()
time.sleep(5)
chrome_driver.find_element(By.XPATH, value="(//input[@class='oxd-input oxd-input--active'])[2]").send_keys("AK")
time.sleep(5)
save = chrome_driver.find_element(By.XPATH, value="//button[@type='submit'] ")
save.click()
time.sleep(10)
