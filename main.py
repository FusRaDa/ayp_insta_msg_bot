import random
import pyperclip
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


def get_list_of_full_names():
    wb = openpyxl.load_workbook(excel_file_path)
    sheet = wb.active

    username_column = sheet['C']

    fullname_list = []

    for x in range(1, len(username_column)):
        fullname_list.append(username_column[x].value)

    print(fullname_list)
    return fullname_list


def get_list_of_user_names():
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

    time.sleep(5)


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

    time.sleep(5)


def go_to_messages():
    chrome.get('https://www.instagram.com/direct/inbox/')

    time.sleep(5)


def dm_user(user_name, full_name, message):

    if full_name is None:
        full_name = "there"

    dm_button = chrome.find_element(By.XPATH,
                                    "//div[@class='x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x9f619 xe8uvvx xdj266r "
                                    "x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x6s0dn4 x78zum5 "
                                    "xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x1ypdohk xl56j7k x1y1aw1k x1sxyh0 "
                                    "xwib8y2 xurb0ha']")
    dm_button.click()

    time.sleep(10)

    search_box = chrome.find_element(By.CSS_SELECTOR, '[name="queryBox"]')
    search_box.send_keys(user_name)

    time.sleep(10)

    # select user
    user_results = chrome.find_elements(By.XPATH,
                                        "//span[@class='x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs xt0psk2 x1i0vuye "
                                        "xvs91rp xo1l8bm x1roi4f4 x10wh9bi x1wdrske x8viiok x18hxmgj']")

    for user in user_results:
        if user.text == user_name:
            user.click()
            break
        else:
            return

    time.sleep(10)

    chat_button = chrome.find_element(By.XPATH,
                                      "//div[@class='x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w x972fbf xcfux6l "
                                      "x1qhh985 xm0m39n xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r "
                                      "x2lwn1j xeuugli xexx8yu x18d9i69 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np "
                                      "x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1lq5wgf xgqcy7u x30kzoy x9jhf4c x1ejq31n "
                                      "xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x78zum5 x1i0vuye xwhw2v2 xl56j7k "
                                      "x17ydfre x1f6kntn x2b8uid xlyipyv x87ps6o x14atkfc x9bdzbf x1n2onr6 x1d5wrs8 "
                                      "xn3w4p2 x5ib6vp xc73u3c x1tu34mt xzloghq']")
    chat_button.click()

    time.sleep(10)

    full_message = "Hey " + full_name + message
    pyperclip.copy(full_message)
    message_box = chrome.find_element(By.XPATH, "//p[@class='xat24cr xdj266r']")
    message_box.send_keys(Keys.CONTROL, "v")

    time.sleep(10)

    send_button = chrome.find_element(By.XPATH,
                                      "//div[@class='x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w xdl72j9 x2lah0s xe8uvvx "
                                      "xdj266r xat24cr x1mh8g0r x2lwn1j xeuugli x1hl2dhg xggy1nq x1ja2u2z x1t137rt "
                                      "x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1ejq31n xd10rxx x1sy0etr x17r0tee "
                                      "x9f619 x1ypdohk x1i0vuye xwhw2v2 xl56j7k x17ydfre x1f6kntn x2b8uid xlyipyv "
                                      "x87ps6o x14atkfc x1d5wrs8 x972fbf xcfux6l x1qhh985 xm0m39n xm3z3ea x1x8b98j "
                                      "x131883w x16mih1h xt0psk2 xt7dq6l xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 "
                                      "xjbqb8w x1n5bzlp x173jzuc x1yc6y37 xfs2ol5']")
    send_button.click()

    time.sleep(10)

    time.sleep(random.randint(180, 300))


followers = get_list_of_user_names()
names = get_list_of_full_names()


initiate_chrome()
login()
go_to_messages()


message_var = {

    1: "! Have you secured your spot for the upcoming AYP Convention? Don’t miss out on this incredible "
       "opportunity because ticket prices will increase on July 1. 🔗 Visit AYP.me/Convention to discover why this "
       "event is a must-attend. If you have any questions or need support with scholarship funding to make attending "
       "possible, feel free to DM us. 🎁 As a special incentive, if you register within the next 24 hours & choose "
       "“Social Media Platform” as your referral source, we’ll gift you a FREE AYP hoodie! This exclusive offer "
       "cannot be combined with other referrals or discount codes. Don’t wait any longer – secure your spot now and "
       "join us at the AYP Convention! We look forward to seeing you there.",

    2: "! Have you heard about the amazing AYP Convention coming up in just over a month? 🎉 Time is running out, "
       "as ticket prices will increase on July 1st. To learn more about why the AYP Convention is an absolute "
       "must-attend, visit AYP.me/Convention. If you have any questions or need support with scholarship funding to "
       "make attending possible, please feel free to send us a DM. We’re here to help! But wait, there’s more! 🎁 If "
       "you register within the next 24 hours and choose “Social Media Platform” as your referral source, "
       "you’ll receive a FREE AYP hoodie as a token of our appreciation. This offer can’t be combined with other "
       "referrals or discount codes. Don’t wait any longer—secure your spot today and get ready for an unforgettable "
       "experience at the AYP Convention. See you there!",

    3: "Have you signed up for the AYP Convention happening next month? If not, don’t wait, because ticket prices go "
       "up on July 1. Visit AYP.me/Convention to learn more about why this is an event you do not want to miss, "
       "and DM us if you have questions or if you need scholarship funding support to make it possible for you to "
       "attend. As a special prize, if you register in the next 24 hours and select “Social Media Platform” when "
       "asked how you heard about the convention, we’ll give you a FREE AYP hoodie! This offer isn’t combinable with "
       "other referrals/discount codes.",
}

y = 1
for x in range(len(followers)):

    if y == 4:
        y = 1

    dm_user(followers[x], names[x], message_var.get(y))
    y += 1
