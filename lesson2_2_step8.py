from selenium import webdriver
import time
import os

driver = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/file_input.html"
    driver.get(link)
    firstNameField = driver.find_element_by_xpath("//input[@name='firstname']")
    lastNameField = driver.find_element_by_xpath("//input[@name='lastname']")
    emailField = driver.find_element_by_xpath("//input[@name='email']")
    inputBtn = driver.find_element_by_xpath("//input[@name='file']")
    submitBtn = driver.find_element_by_xpath("//button[@type='submit']")
    currentDir = os.path.abspath(os.path.dirname(__file__))
    filePath = os.path.join(currentDir, 'client.txt')
    firstNameField.send_keys("Roman")
    lastNameField.send_keys("Miller")
    emailField.send_keys("adm.dx@outlook.com")
    inputBtn.send_keys(filePath)
    submitBtn.click()
finally:
    time.sleep(10)
    driver.quit()
