from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, InvalidArgumentException
from time import sleep
from password import pw

username = 'druisr@gmail.com'
chrome_profile_path = './CustomProfile'

# Chrome options
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--disable-extensions')
options.add_argument('--profile-directory=Profile 1')
options.add_argument('--user-data-dir=' + chrome_profile_path)
options.add_argument('--start-maximized')

# Open Chrome
print('Opening Chrome...')
try:
    driver = webdriver.Chrome(options=options)
    print('Chrome opened')
except InvalidArgumentException:
    print('A Chrome session using the bot is already in use, please close it and try again...')
    exit()


# Open web app
print('Opening WebApp...')
driver.get('https://www.easports.com/fifa/ultimate-team/web-app/')
print('WebApp opened')
sleep(10)

# Log in
print('Logging in...')
try:
    driver.find_element_by_xpath('//*[@id="Login"]/div/div/button[1]').click()

    # Log in with username and pw
    driver.find_element_by_xpath('//*[@id="email"]').clear()
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(pw)
    # driver.find_element_by_xpath('//*[@id="remember-me-panel"]/li/div/div').click()
    driver.find_element_by_xpath('//*[@id="btnLogin"]/span/span').click()
except NoSuchElementException:
    print("Already logged in")

# TODO Main loop