from bot import *
from time import sleep
from getpass import getpass
import argparse

# TODO logging https://docs.python.org/3/howto/logging.html

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", help="FUT EA account email")
    parser.add_argument("-p", "--password", help="FUT EA account password")
    parser.add_argument("--headless", help="Run headless", action="store_true")

    args = parser.parse_args()

    if args.username is None:
        username = input("Email: ")
    elif args.username is not None:
        username = args.username

    if args.password is None:
        pw = getpass()
    elif args.password is not None:
        pw = args.password
        
    bot = WebAppBot(username, pw)
    bot.auto_relist()