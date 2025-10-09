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

#Creating xpath
# //tagname[@attribute='value']  -> //input[@type='submit']

driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

#Creating CSS Selector
# tagname[attribute='value']  -> input[type='submit']
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys('John')

assert 'Success' in message

# we can use #id and .class for CSS Selector
# #exampleInputPassword1  -> for id
# .form-control  -> for class

# (//input[@type='text'])[3] can be used to select the 3rd element of the same type

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("USA")
time.sleep(2)
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()










time.sleep(2)