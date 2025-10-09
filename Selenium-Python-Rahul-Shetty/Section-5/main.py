import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service

#Chrome drive service
driver = webdriver.Chrome()


driver.get("https://rahulshettyacademy.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)










time.sleep(2)