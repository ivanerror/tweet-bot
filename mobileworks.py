from pydoc import cli
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
import random
from time import sleep
import itertools
import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
           "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ]

all_combos = list(itertools.combinations(letters, 7))
all_combos = [''.join(combo) for combo in all_combos]  # make them strings

accCount = int(input("How Many Accounts you want create :"))

options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)


def createAccount():
    randomname = email = random.sample(all_combos, 1)[0]
    driver = webdriver.Chrome(
        options=options, executable_path="./chromedriver")
    wait = WebDriverWait(driver, 10)

    driver.get("https://mobileworkslx.xyz/6308612916022")
    driver.minimize_window()

    daftarBtn = driver.find_element_by_xpath(
        '//*[@id="masthead"]/div/div/div/div[2]/div/div[1]/a')

    daftarBtn.click()

    driver.switch_to.window(driver.window_handles[1])

    sleep(1)

    fullname = driver.find_element_by_xpath('//*[@id="fullname"]')
    username = driver.find_element_by_xpath('//*[@id="username"]')
    email = driver.find_element_by_xpath('//*[@id="email"]')
    password = driver.find_element_by_xpath('//*[@id="password"]')
    passwordAgain = driver.find_element_by_xpath('//*[@id="passwordAgain"]')
    termsCB = driver.find_element_by_xpath('//*[@id="terms"]')
    signupBtn = driver.find_element_by_xpath(
        '/html/body/div/div/div/div[2]/div/div/div/div/div[8]/button')

    fullname.send_keys(randomname + ' fname')
    username.send_keys(randomname)
    email.send_keys(randomname + '@superx.xyz')
    password.send_keys('mypassword123')
    passwordAgain.send_keys('mypassword123')
    # terms = wait.until(ec.visibility_of_element_located(
    #     By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div/div[6]/div/label')).isSelected()
    # terms.click()

    termsCB.send_keys(Keys.SPACE)
    signupBtn.click()
    sleep(3)

    print(driver.current_url)

    if 'login' in driver.current_url:
        print('dipindahkan di login page, menunggu 15 detik')
        driver.quit()
        sleep(15)
        return createAccount()

    print('Success Register : ' + randomname)


    with open('accountList.txt', 'a') as f :
        f.write("\n" + randomname)
    driver.quit()
    return 0


for i in range(accCount):
    createAccount()
