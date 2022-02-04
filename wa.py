from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


driver = webdriver.Chrome(executable_path="./chromedriver")

driver.get("https://web.whatsapp.com")


print("Scan QR Code, And then Enter")
input()
print("Logged In")

newChat = driver.find_element_by_xpath('//span[@data-testid="chat"]')
newChat.click()

inputName = driver.find_element_by_xpath(
    '/html/body/div[1]/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div[1]/div/label/div/div[2]')
inputName.send_keys('Toni')