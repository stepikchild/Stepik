from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import vareables
from help import calc

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 12)
browser.get(vareables.link1)
wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
browser.find_element_by_id("book").click()
y = calc(browser.find_element_by_id("input_value").text)
print(y)
browser.find_element_by_id("answer").send_keys(y)
browser.find_element_by_id("solve").click()