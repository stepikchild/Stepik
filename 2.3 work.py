from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get(link)
try:
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(y)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
    # изменил файл 2.3
