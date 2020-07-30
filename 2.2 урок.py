from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/selects1.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get(link)
browser.find_element_by_css_selector("[value='" + z + "']").click()
try:

    option = browser.find_element_by_id("robotCheckbox")
    option.click()
    option1 = browser.find_element_by_id("robotsRule")
    option1.click()
    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(y)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
