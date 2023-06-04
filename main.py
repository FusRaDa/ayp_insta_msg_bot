from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
from selenium.webdriver.common.by import By
import configparser
import time
import openpyxl


# https://www.geeksforgeeks.org/send-direct-message-on-instagram-using-selenium-in-python/
# https://www.youtube.com/watch?v=Xjv1sY630Uc&list=PLzMcBGfZo4-n40rB1XaJ0ak1bemvlqumQ

excel_file_path = 'C:\\Users\\FusRada\\Desktop\\ftlwebdev-6-4-23.xlsx'

parser = configparser.ConfigParser()
parser.read('credentials.txt')

username = parser.get('creds', 'username')
password = parser.get('creds', 'password')


def get_list_of_users():
    wb = openpyxl.load_workbook(excel_file_path)
    sheet = wb.active

    username_column = sheet['B']

    username_list = []

    for x in range(1, len(username_column)):
        username_list.append(username_column[x].value)

    print(username_list)
    return username_list


# declare global webdriver variable
chrome = webdriver.Chrome()


# go to instagram - initiate browser
def initiate_chrome():

    chrome.get('https://www.instagram.com/')

    time.sleep(10)


def login():

    # finds the username box
    username_input = chrome.find_element("name", "username")
    # sends the entered username
    username_input.send_keys(username)

    # finds the password box
    password_input = chrome.find_element("name", "password")
    # sends the entered password
    password_input.send_keys(password)

    # press enter after sending password - login to account
    password_input.send_keys(Keys.RETURN)

    time.sleep(10)


def go_to_messages():
    chrome.get('https://www.instagram.com/direct/inbox/')

    time.sleep(5)

    not_now_button = chrome.find_element(By.CLASS_NAME, "_a9--")
    not_now_button.click()

    time.sleep(5)


def dm_user(user_name):
    dm_button = chrome.find_element(By.CLASS_NAME, "x78zum5 xdt5ytf x1n2onr6 x1ja2u2z")
    dm_button.click()

    search_box = chrome.find_element("name", "queryBox")
    search_box.send_keys(user_name)

    time.sleep(5)

    user_photo = chrome.find_element('alt', user_name)
    user_photo.click()

    time.sleep(5)


followers = get_list_of_users()

initiate_chrome()
login()
go_to_messages()
dm_user(followers[0])



























