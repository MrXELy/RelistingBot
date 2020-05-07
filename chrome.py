from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, InvalidArgumentException, \
    WebDriverException, ElementNotInteractableException, ElementClickInterceptedException, \
    TimeoutException
from time import sleep


CHROME_PROFILE_PATH = './CustomProfile'
WEBAPP_URL = 'https://www.easports.com/fifa/ultimate-team/web-app/'


def set_options():
    """Return chrome options

    :return: Chrome options
    :rtype: ChromeOptions
    """
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging']) # comment this line to see driver logs

    options.add_argument('--disable-extensions')
    options.add_argument('--profile-directory=Profile 1')
    options.add_argument('--user-data-dir=' + CHROME_PROFILE_PATH)
    
    return options


def open_chrome(options):
    """Open a Google Chrome session, using options

    :param options: Chrome options
    :type options: ChromeOptions
    :return: Driver
    :rtype: webdriver
    """
    try:
        print('[LOG] Opening Chrome...')
        driver = webdriver.Chrome(options=options)
        print('[SUCCESS] Chrome opened')
    except Exception as e:
        print('[FAIL]', e)
        exit()

    return driver


def open_webapp(driver):
    print('[LOG] Opening WebApp...')
    driver.get(WEBAPP_URL)
    try:
        element_tmp = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="Login"]/div/div/header')))
        print('[SUCCESS] WebApp opened')
    except TimeoutException:
        print('[FAIL] Timeout')
        driver.quit()
        exit()


def log_in(driver, username, pw):
    print('[LOG] Logging in...')
    sleep(1)
    
    try:
        element_tmp = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Login"]/div/div/button[1]')))
        driver.find_element_by_xpath('//*[@id="Login"]/div/div/button[1]').click()
        
        print('[LOG] Trying to log in...')
        try:
            element_tmp = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="email"]')))
            driver.find_element_by_xpath('//*[@id="email"]').clear()
            driver.find_element_by_xpath('//*[@id="email"]').send_keys(username)
            driver.find_element_by_xpath('//*[@id="password"]').send_keys(pw)
            driver.find_element_by_xpath('//*[@id="btnLogin"]/span/span').click()
            
            print('[LOG] Is there an error ?')
            try:
                driver.find_element_by_xpath('//*[@class="general-error"]')
                print("[FAIL] Login failed ! Wrong email or password")
                driver.quit()
                exit()
            except NoSuchElementException:
                print("[SUCCESS] Logged in!")
        except TimeoutException:
            print('[FAIL] Timeout')
    except TimeoutException:
        print('[SUCCESS] Already logged in')


def wait_webapp_loaded(driver):
    print('[LOG] Loading WebApp...')
    try: # ? Sometimes "click-shield" intercepts the click
        element_tmp = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Transfers')]")))
        sleep(1)
        element_tmp = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Transfers')]")))
        print('[SUCCESS] WebApp loaded')
    except Exception as e:
        print('[FAIL]', e)
        driver.quit()
        exit()
        

def click_transfers(driver):
    print('[LOG] Clicking on Transfers')
    try:
        driver.find_element_by_xpath("//*[contains(text(), 'Transfers')]").click()
    except Exception as e:
        print('[FAIL]', e)
        driver.quit()
        exit()
        
        
def click_transfer_list(driver):
    print('[LOG] Clicking on Transfer List')
    try:
        element_tmp = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Transfer List')]")))
        sleep(0.5)
        driver.find_element_by_xpath("//*[contains(text(), 'Transfer List')]").click()
    except TimeoutException:
        print('[FAIL] Timeout')
        driver.quit()
        exit()
        

def click_relist_all(driver):
    print('[LOG] Looking for players to relist...')
    try:
        driver.find_element_by_xpath("//*[contains(text(), 'Re-list All')]").click()
        
        try:
            element_tmp = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Yes')]")))
            sleep(0.5)
            driver.find_element_by_xpath("//*[contains(text(), 'Yes')]").click()
            print('[SUCCESS] Players relisted')
        except TimeoutException:
            print('[FAIL] Timeout')
    except ElementNotInteractableException:
        print('[SUCCESS] No players to relist')