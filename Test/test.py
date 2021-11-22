import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element

driver = webdriver.Chrome(executable_path="Test\chromedriver.exe")
driver.maximize_window()

driver.get('https://risevest.com')
driver.implicitly_wait(10)

"When I click on Products"
driver.find_element(By.XPATH, "//span[contains(text(),'Products')]").click()  # Product menu
driver.implicitly_wait(10)

s = driver.find_element(By.TAG_NAME, "h1")
# obtain text
t = s.text
print(t)

driver.find_element(By.LINK_TEXT, 'Build Wealth').click()  # build wealth
text_to_be_present_in_element(By.LINK_TEXT, "Build Wealth")




driver.quit()

print('test case completed')


