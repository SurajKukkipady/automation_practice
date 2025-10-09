import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service

#Chrome drive service
#driver = webdriver.Chrome()

##Service is used to specify the path of the driver
service = Service(r"C:\Users\suraj\Downloads\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=service)


driver.get("https://rahulshettyacademy.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)










time.sleep(2)