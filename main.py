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


def dm_follower(follower):
    url = 'https://www.instagram.com/' + follower
    chrome.get(url)

    time.sleep(5)

    try:
        message_button = chrome.find_element(By.XPATH, "//*[text()='Message']")
        message_button.click()

    except selenium.common.exceptions.NoSuchElementException:
        follow_button = chrome.find_element(By.XPATH, "//*[text()='Follow Back']")
        follow_button.click()

        time.sleep(5)

        message_button = chrome.find_element(By.XPATH, "//*[text()='Message']")
        message_button.click()

    time.sleep(5)


followers = get_list_of_users()

initiate_chrome()
login()
dm_follower(followers[0])



























