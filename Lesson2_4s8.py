import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()

browser.get("https://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price=WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID,"price"),"100"))
button =browser.find_element(By.ID,"book")
button.click()
value=browser.find_element(By.ID,"input_value")
x=value.text
y=calc(x)

input=browser.find_element(By.ID,"answer")
input.send_keys(y)

button2=browser.find_element(By.ID,"solve")
button2.click()
time.sleep(30)