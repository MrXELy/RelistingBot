from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, InvalidArgumentException, WebDriverException, ElementNotInteractableException
from time import sleep
from password import pw

# TODO Use functions or classes for more readability
# TODO Use argparse to get user email
# TODO Get (hashed) password

username = 'druisr@gmail.com'
chrome_profile_path = './CustomProfile'
webapp_url = 'https://www.easports.com/fifa/ultimate-team/web-app/'

# Chrome options
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--disable-extensions')
options.add_argument('--profile-directory=Profile 1')
options.add_argument('--user-data-dir=' + chrome_profile_path)
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
while True: # TODO Handle daily gifts
    print('[INFO] TO END PROGRAM, PRESS CTRL+C')

    # Open web app
    print('[LOG] Opening WebApp...')
    driver.get(webapp_url)
    print('[SUCCESS] WebApp opened')
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
        print('[SUCCESS] Logged in')
    except NoSuchElementException:
        print('[SUCCESS] Already logged in')
    sleep(10)

    print('[LOG] Clicking on Transfers')
    driver.find_element_by_xpath('/html/body/main/section/nav/button[3]').click()
    sleep(1)

    print('[LOG] Clicking on Transfer list')
    driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/div[3]').click()
    sleep(2)

    print('[LOG] Looking for players to relist...')
    try:
        driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/div/section[2]/header/button').click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[4]/section/div/div/button[2]/span[1]').click()
        player('[SUCCESS] Players relisted')
    except ElementNotInteractableException:
        print('[SUCCESS] No players to relist')

    print('[WAIT] Waiting for 1 hour...')
    sleep(10)