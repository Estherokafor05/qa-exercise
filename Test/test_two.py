import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="Test\chromedriver.exe")
driver.maximize_window()

driver.get("https://risevest.com/build-wealth")
driver.implicitly_wait(30)

driver.find_element(By.XPATH, "//input[@value='35']").clear()
driver.find_element(By.XPATH, "//body/div[@id='__next']/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/label[1]/input[1]").send_keys('25')

driver.find_element(By.XPATH,
                    "//body/div[@id='__next']/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/label[1]/input[1]").clear()
driver.find_element(By.XPATH,
                    "//body/div[@id='__next']/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/label[1]/input[1]").send_keys(
    '350000')

driver.find_element(By.XPATH,
                    "//body/div[@id='__next']/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[3]/label[1]/input[1]").clear()
driver.find_element(By.XPATH,
                    "//body/div[@id='__next']/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[3]/label[1]/input[1]").send_keys(
    '20.00')

driver.find_element(By.XPATH,
                    "//body/div[@id='__next']/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[4]/label[1]/input[1]").clear()
driver.find_element(By.XPATH,
                    "//body/div[@id='__next']/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[4]/label[1]/input[1]").send_keys(
    '60')


select = Select(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@id='investmentPreference']"))))
select.select_by_visible_text("Stability")


driver.find_element(By.XPATH, "//button[contains(text(),'Calculate')]").click()  # calculate

driver.quit()

print('Test Passed')
