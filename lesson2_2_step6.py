from selenium import webdriver
import math
import time

driver = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://SunInJuly.github.io/execute_script.html"
    driver.get(link)
    driver.execute_script("window.scrollBy(0, 100);")
    x_element = driver.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    answerField = driver.find_element_by_id("answer")
    answerField.send_keys(y)
    checkbox1 = driver.find_element_by_xpath("//label[@for='robotCheckbox']")
    radiobutton1 = driver.find_element_by_xpath("//label[@for='robotsRule']")
    buttonSubmit = driver.find_element_by_xpath("//button[@type='submit']")
    checkbox1.click()
    radiobutton1.click()
    buttonSubmit.click()
finally:
    time.sleep(10)
    driver.quit()
