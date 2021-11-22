from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="Test\chromedriver.exe")
driver.maximize_window()

driver.get("http://localhost:3000")
webdriver.wait(5)
print(driver.current_url)

driver.quit()

