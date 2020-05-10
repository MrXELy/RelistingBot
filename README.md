# RelistingBot

Automatically relist your trade pile every hour when you're sleeping, at work, or far from your computer!

## Demo

https://puu.sh/FIFqk/6057634cc8.gif

## Disclaimer

This program does not handle EA bot verification.

# Running from source

## Clone

- Clone this repo to your local machine:
```
git clone https://github.com/MrXELy/RelistingBot.git
```

## Setup

- You need selenium:
```
pip install selenium
```
- Download chromedriver [here](https://chromedriver.chromium.org/getting-started) and put in your `PATH`.
- Change your FUT WebApp language to English, it's important!

## Usage

```
python main.py
python main.py -u your@mail
python main.py -u your@mail -p password
python main.py --help
```

## First use

```
[VERIFICATION] Looks like it is the first time you are using this.
[VERIFICATION] EA need to verify your identity
[VERIFICATION] You will receive a code: *****@gmail.com
[VERIFICATION] Please type in the code you received: 123456
```

You will probably be asked to verify your identity, because chromedriver creates a new session you've never been connencted to. Do it in the prompt. You will need to do this just once, as long as you don't delete `./CustomProfile/` folder.

# About

FUT player since 2012, FUT trader for a few years I used an autoclicker to relist my trade pile when I coundln't do it myself. Python beginner, I finally a fun project to make.