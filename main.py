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
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome = webdriver.Chrome(options=chrome_options)


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


def dm_user(user_name):
    dm_button = chrome.find_element(By.XPATH, "//div[@class='x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x9f619 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x6s0dn4 x78zum5 xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x1ypdohk xl56j7k x1y1aw1k x1sxyh0 xwib8y2 xurb0ha']")
    dm_button.click()

    time.sleep(5)

    search_box = chrome.find_element(By.CSS_SELECTOR, '[name="queryBox"]')
    search_box.send_keys(user_name)

    time.sleep(5)

    # start work here
    user_photo = chrome.find_element(By.XPATH, "//span[@class='x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xvs91rp x1s688f x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj']")
    user_photo.click()

    time.sleep(5)

    chat_button = chrome.find_element(By.XPATH, "//div[@class='x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w x972fbf xcfux6l x1qhh985 xm0m39n xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1lq5wgf xgqcy7u x30kzoy x9jhf4c x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x78zum5 x1i0vuye xwhw2v2 xl56j7k x17ydfre x1f6kntn x2b8uid xlyipyv x87ps6o x14atkfc x9bdzbf x1n2onr6 x1d5wrs8 xn3w4p2 x5ib6vp xc73u3c x1tu34mt xzloghq']")
    chat_button.click()

    time.sleep(5)

    message_box = chrome.find_element(By.XPATH, "//p[@class='xat24cr xdj266r']")
    message_box.send_keys("AYP Message")

    time.sleep(5)

    send_button = chrome.find_element(By.XPATH, "//div[@class='x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w xdl72j9 x2lah0s xe8uvvx xdj266r xat24cr x1mh8g0r x2lwn1j xeuugli x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x1i0vuye xwhw2v2 xl56j7k x17ydfre x1f6kntn x2b8uid xlyipyv x87ps6o x14atkfc x1d5wrs8 x972fbf xcfux6l x1qhh985 xm0m39n xm3z3ea x1x8b98j x131883w x16mih1h xt0psk2 xt7dq6l xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 xjbqb8w x1n5bzlp x173jzuc x1yc6y37 xfs2ol5']")
    send_button.click()

    time.sleep(5)


followers = get_list_of_users()

initiate_chrome()
login()
go_to_messages()

dm_user(followers[0])



























