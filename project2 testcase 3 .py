import time
from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_driver = webdriver.Chrome()
chrome_driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(5)
chrome_driver.find_element(By.XPATH, value ="//input[@name='username']").send_keys("Admin")
password = "admin123"
chrome_driver.find_element(By.XPATH, value ="//input[@name='password']").send_keys(password)
login = chrome_driver.find_element(By.XPATH, value="//button[@type='submit']")
login.click()
time.sleep(5)
admin = chrome_driver.find_element(By.XPATH, value="//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a")
admin.click()
time.sleep(4)
pim = chrome_driver.find_element(By.XPATH, value="//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span")
pim.click()
time.sleep(4)
leave = chrome_driver.find_element(By.XPATH, value="//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a/span")
leave.click()
time.sleep(4)
second = chrome_driver.find_element(By.XPATH, value="//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a/span")
second.click()
time.sleep(4)
recruitment = chrome_driver.find_element(By.XPATH, value="//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span")
recruitment.click()
time.sleep(4)
myinfo = chrome_driver.find_element(By.XPATH, value="//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span")
myinfo.click()
time.sleep(4)
perform = chrome_driver.find_element(By.XPATH, value="//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span")
perform.click()
time.sleep(4)
dash = chrome_driver.find_element(By.XPATH, value="//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a/span")
dash.click()
time.sleep(4)
director = chrome_driver.find_element(By.XPATH, value="//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a/span")
director.click()
time.sleep(4)
maintenance = chrome_driver.find_element(By.XPATH, value="//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a/span")
maintenance.click()
time.sleep(4)
cancel = chrome_driver.find_element(By.XPATH, value="//*[@id='app']/div[1]/div[1]/form/div[4]/button[1]")
cancel.click()
time.sleep(4)
buzz = chrome_driver.find_element(By.XPATH, value="//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a/span")
buzz.click()
time.sleep(4)