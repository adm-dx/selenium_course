from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/math.html"
    browser.get(link)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    answerField = browser.find_element_by_id("answer")
    answerField.send_keys(y)
    checkbox1 = browser.find_element_by_xpath("//label[@for='robotCheckbox']")
    radiobutton1 = browser.find_element_by_xpath("//label[@for='robotsRule']")
    buttonSubmit = browser.find_element_by_xpath("//button[@type='submit']")
    checkbox1.click()
    radiobutton1.click()
    buttonSubmit.click()

finally:
    time.sleep(10)
    browser.quit()
