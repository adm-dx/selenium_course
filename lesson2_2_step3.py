from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/selects2.html"
    driver.get(link)
    numElement1 = driver.find_element_by_xpath("//span[@id='num1']")
    numElement2 = driver.find_element_by_xpath("//span[@id='num2']")
    result = str(int(numElement1.text) + int(numElement2.text))
    select = Select(driver.find_element_by_xpath("//select[@id='dropdown']"))
    select.select_by_value(result)
    submitButton = driver.find_element_by_xpath("//button[@type='submit']")
    submitButton.click()
finally:
    time.sleep(10)
    driver.quit()
