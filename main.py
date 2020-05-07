from chrome import *
from time import sleep
from getpass import getpass
import argparse

# TODO learn classes
# TODO logging https://docs.python.org/3/howto/logging.html

if __name__ = '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", help="FUT EA account email")
    parser.add_argument("-p", "--password", help="FUT EA account password")
    parser.add_argument("--headless", help="Run headless", action="store_true")

    args = parser.parse_args()

    if args.username is None and args.init is not True:
        username = input("Email: ")
    elif args.username is not None:
        username = args.username

    if args.password is None and args.init is not True:
        pw = getpass()
    elif args.password is not None:
        pw = args.password
        
    # Open Chrome
    driver = open_chrome(set_options())

    # Main loop
    while True:
        open_webapp(driver)
        log_in(driver, username, pw)
        wait_webapp_loaded(driver)
        click_transfers(driver)
        click_transfer_list(driver)
        click_relist_all(driver)
        
        print('[WAIT] Waiting for 1 hour...')
        
        input()
        driver.quit()
        exit()