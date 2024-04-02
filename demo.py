from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.get('http://192.168.1.149:5500/login')
driver.maximize_window()

username = '//*[@placeholder="请输入账号或邮箱"]'
pwd = '//*[@placeholder="请输入密码"]'
button = (By.XPATH, '//button')
wait = WebDriverWait(driver, 10, 0.3)
wait.until(ec.visibility_of_element_located((By.XPATH, '//button')))

driver.find_element(By.XPATH, username).send_keys('greatwall')

driver.find_element(By.XPATH, pwd).send_keys('Aa123456!')
time.sleep(5)
driver.find_element(By.XPATH, '//button').click()
try:
    wait.until(ec.presence_of_element_located((By.XPATH, "//*[text()='提示']")))
    print('弹窗出现')
except:
    print("未捕获弹窗")