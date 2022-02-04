from selenium import webdriver
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
driver = webdriver.Chrome(executable_path="./chromedriver")
wait = WebDriverWait(driver, 10)
driver.get("https://twitter.com/login")
sleep(3)
driver.find_element_by_xpath(
    '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input').send_keys(input("Enter your username: "))
sleep(2)
driver.find_element_by_xpath(
    '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]').click()
sleep(2)
driver.find_element_by_xpath(
    '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(input("Enter your password: "))
sleep(2)
driver.find_element_by_xpath(
    '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div').click()


f = open('iron.txt', 'r')
sleep(3)

for word in f:
    if(word == "\n"):
        continue
    print("Tweet! : " + word)
    tweet_text_span = driver.find_element_by_xpath(
        "//div[@data-testid='tweetTextarea_0']/div/div/div/span")
    tweet_text_span.send_keys(word)
    tweet_button = wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@data-testid='tweetButtonInline']")))
    tweet_button.click()
# driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div').click()
# driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div').send_keys(word)
# driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]').click()
    sleep(random.randint(4,10))
