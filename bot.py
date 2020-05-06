from sys import exit
from os import system
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, InvalidArgumentException, WebDriverException, ElementNotInteractableException, ElementClickInterceptedException
from time import sleep
from getpass import getpass
import argparse

CHROME_PROFILE_PATH = './CustomProfile'
WEBAPP_URL = 'https://www.easports.com/fifa/ultimate-team/web-app/'

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username", help="FUT EA account email")
parser.add_argument("-p", "--password", help="FUT EA account password")
parser.add_argument("--init", help="Use init the first time you use this program", action="store_true")

args = parser.parse_args()

# TODO Use functions or classes for more readability

username = args.username

if args.username is None and args.init is not True:
    username = input("Email: ")
elif args.username is not None:
    username = args.username

if args.password is None and args.init is not True:
    pw = getpass()
elif args.password is not None:
    pw = args.password

# Chrome options
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--disable-extensions')
options.add_argument('--profile-directory=Profile 1')
options.add_argument('--user-data-dir=' + CHROME_PROFILE_PATH)
options.add_argument('--start-maximized')

# Open Chrome
print('[LOG] Opening Chrome...')
try:
    driver = webdriver.Chrome(options=options)
    print('[SUCCESS] Chrome opened')
# except WebDriverException: # ! Seems like I don't know how to handle exceptions
#     print('Can not load chromedriver, please see README.me')
#     exit()
# except InvalidArgumentException:
#     print('A Chrome session using the bot is already in use, please close it and try again...')
#     exit()
except:
    print('[FAIL] Error while using chromeloader: please make sure you have downloaded chromedriver and that no other session is already in use')
    exit()
sleep(1)

# Main loop
while True:
    print('\n[INFO] TO END PROGRAM, PRESS CTRL+C\n')

    # Open web app
    print('[LOG] Opening WebApp...')
    driver.get(WEBAPP_URL)
    print('[SUCCESS] WebApp opened')
    
    if args.init is True:
        print("Connect manually for the first time. When done, please use the program without '--init'")
        exit()

    sleep(10)

    # Log in
    print('[LOG] Logging in...')
    try:
        driver.find_element_by_xpath('//*[@id="Login"]/div/div/button[1]').click()

        # Log in with username and pw
        driver.find_element_by_xpath('//*[@id="email"]').clear()
        driver.find_element_by_xpath('//*[@id="email"]').send_keys(username)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(pw)
        driver.find_element_by_xpath('//*[@id="btnLogin"]/span/span').click()
        if driver.find_element_by_xpath('//*[@class="general-error"]') is not None:
            print("[FAIL] Login failed ! Wrong email or password")
            exit()
    except NoSuchElementException:
        print('[SUCCESS] Already logged in')
    sleep(10)

    try:
        print('[LOG] Clicking on Transfers')
        driver.find_element_by_xpath("//*[contains(text(), 'Transfers')]").click()
        print('[SUCCESS] Logged in')
        sleep(1)
    except ElementClickInterceptedException: # TODO handle daily gift popup
        print('[FAIL] Daily gift ?')
        exit()

    print('[LOG] Clicking on Transfer list')
    driver.find_element_by_xpath("//*[contains(text(), 'Transfer List')]").click()
    sleep(2)

    print('[LOG] Looking for players to relist...')
    try:
        driver.find_element_by_xpath("//*[contains(text(), 'Re-list All')]").click()
        sleep(3)
        driver.find_element_by_xpath("//*[contains(text(), 'Yes')]").click()
        print('[SUCCESS] Players relisted')
    except ElementNotInteractableException:
        print('[SUCCESS] No players to relist')

    print('[WAIT] Waiting for 1 hour...')
    sleep(3660)

system("pause")