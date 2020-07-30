from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("/html/body/div/form/div/input[2]")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath("/html/body/div/form/div/input[3]")
    input3.send_keys("123@123.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element_by_name("file")
    element.send_keys(file_path)
    print(current_dir)
    print(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()