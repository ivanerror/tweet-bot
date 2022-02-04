from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
import random
from time import sleep

driver = webdriver.Chrome(executable_path="./chromedriver")
wait = WebDriverWait(driver, 10)

driver.get("https://shopee.co.id/buyer/login")
sleep(3)

username = driver.find_element_by_xpath('//input[@name="loginKey"]')
username.send_keys('ivanerror')

password = driver.find_element_by_xpath('//input[@name="password"]')
password.send_keys("Setanalas21")

loginBtn = driver.find_element_by_xpath('//button[contains(text(), "Log in")]')
loginBtn.click()
