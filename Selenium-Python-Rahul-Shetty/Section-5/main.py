import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

#Chrome drive service
driver = webdriver.Chrome()


driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

# ID, xpath, CSS Selector, Name, Class Name, Link Text, Partial Link Text, Tag Name

driver.find_element(By.NAME, "email").send_keys("email@email.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()










time.sleep(2)