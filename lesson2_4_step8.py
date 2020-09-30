from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

driver = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    bookButton = driver.find_element_by_id("book")
    bookButton.click()
    driver.execute_script("window.scrollBy(0, 300);")
    xValue = int(driver.find_element_by_xpath("//span[@id='input_value']").text)
    resultField = driver.find_element_by_xpath("//input[@id='answer']")
    resultField.send_keys(calc(xValue))
    submitBtn1 = driver.find_element_by_xpath("//button[@type='submit']")
    submitBtn1.click()
finally:
    time.sleep(10)
    driver.quit()