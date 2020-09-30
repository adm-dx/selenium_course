import math
import time

from selenium import webdriver

driver = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    driver.get(link)
    submitBtn = driver.find_element_by_xpath("//button[@type='submit']")
    submitBtn.click()
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    xValue = int(driver.find_element_by_xpath("//span[@id='input_value']").text)
    resultField = driver.find_element_by_xpath("//input[@id='answer']")
    resultField.send_keys(calc(xValue))
    submitBtn1 = driver.find_element_by_xpath("//button[@type='submit']")
    submitBtn1.click()
finally:
    time.sleep(10)
    driver.quit()
