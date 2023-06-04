from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import configparser
import time


# https://www.geeksforgeeks.org/send-direct-message-on-instagram-using-selenium-in-python/
# https://www.youtube.com/watch?v=Xjv1sY630Uc&list=PLzMcBGfZo4-n40rB1XaJ0ak1bemvlqumQ

parser = configparser.ConfigParser()
parser.read('credentials.txt')

username = parser.get('creds', 'username')
password = parser.get('creds', 'password')

# go to instagram
chrome = webdriver.Chrome()
chrome.get('https://www.instagram.com/')


def login():

    time.sleep(5)

    # finds the username box
    username_input = chrome.find_element("name", "username")
    # sends the entered username
    username_input.send_keys(username)

    # finds the password box
    password_input = chrome.find_element("name", "password")
    # sends the entered password
    password_input.send_keys(password)

    # press enter after sending password
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)




















