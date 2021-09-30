from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Edge()
driver.get('https://passport.yandex.ru/auth/')
element = driver.find_element_by_name('login')
element.send_keys('')  # логин
element.send_keys(Keys.RETURN)
time.sleep(2)
element = driver.find_element_by_name('passwd')
element.send_keys('')  # пароль
element.send_keys(Keys.RETURN)
driver.close()
driver.quit()
