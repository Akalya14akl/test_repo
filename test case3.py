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
time.sleep(5)
pim = chrome_driver.find_element(By.XPATH, value =" (//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[2]")
pim.click()
time.sleep(5)
add = chrome_driver.find_element(By.XPATH, value="//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
add.click()
time.sleep(5)
chrome_driver.find_element(By.XPATH, value ="//input[@name='firstName']").send_keys("Akalya")
chrome_driver.find_element(By.XPATH, value ="//input[@name='middleName']").send_keys("surendhar")
chrome_driver.find_element(By.XPATH, value ="//input[@name='lastName']" ).send_keys("S")
time.sleep(5)
chrome_driver.find_element(By.XPATH, value = "(//input[@class='oxd-input oxd-input--active'])[2] ")
time.sleep(5)
create = chrome_driver.find_element(By.XPATH, value = "//span[@class='oxd-switch-input oxd-switch-input--active "
                                                      "--label-right']"
)
create.click()
time.sleep(5)
chrome_driver.find_element(By.XPATH, value = "(//input[@class='oxd-input oxd-input--active'])[3]").send_keys("Suren")
password = "Akalya@123"
chrome_driver.find_element(By.XPATH, value = "(//input[@type='password'])[1]").send_keys(password)
chrome_driver.find_element(By.XPATH, value = "(//input[@type='password'])[2]").send_keys(password)
time.sleep(5)
disable = chrome_driver.find_element(By.XPATH, value = "(//span[@class='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input'])[2]")
disable.click()
time.sleep(5)
save = chrome_driver.find_element(By.XPATH, value = "//button[@type='submit'] ")
save.click()
time.sleep(5)