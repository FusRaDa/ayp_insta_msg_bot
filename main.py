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

test_file = "ftlwebdev-6-4-23.xlsx"
ayp_file = "ayp-6-4-23.xlsx"

excel_file_path = 'C:\\Users\\FusRada\\Desktop\\' + test_file

parser = configparser.ConfigParser()
parser.read('credentials.txt')

username = parser.get('creds', 'username')
password = parser.get('creds', 'password')


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


def dm_user(user_name, message):
    try:

        dm_button = chrome.find_element(By.XPATH,
                                        "//div[@class='x78zum5']")
        dm_button.click()

        time.sleep(10)

        search_box = chrome.find_element(By.CSS_SELECTOR, '[name="queryBox"]')
        search_box.send_keys(user_name)

        time.sleep(10)

        # select user
        user_results = chrome.find_elements(By.XPATH,
                                            "//span[@class='x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xvs91rp xo1l8bm x1roi4f4 x10wh9bi x1wdrske x8viiok x18hxmgj']")

        for user in user_results:
            if user.text == user_name:
                print(user.text)
                user.click()
                break

        time.sleep(10)

        chat_button = chrome.find_element(By.XPATH,
                                          "//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh "
                                          "xw7yly9 xktsk01 x1yztbdb x1d52u69 x1uhb9sk x1plvlek xryxfnj x1c4vz4f "
                                          "x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1']")
        chat_button.click()

        time.sleep(10)

        accept_button = chrome.find_element(By.XPATH, "//div[@class='x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w xdl72j9 "
                                                      "x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j "
                                                      "xeuugli x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv "
                                                      "x1a2a7pz x6s0dn4 xjyslct x1ejq31n xd10rxx x1sy0etr x17r0tee "
                                                      "x9f619 x1ypdohk x1i0vuye x1f6kntn xwhw2v2 xl56j7k x17ydfre "
                                                      "x2b8uid xlyipyv x87ps6o x14atkfc x1d5wrs8 xjbqb8w xm3z3ea "
                                                      "x1x8b98j x131883w x16mih1h x972fbf xcfux6l x1qhh985 xm0m39n "
                                                      "xt0psk2 xt7dq6l xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 "
                                                      "x1n5bzlp xqnirrm xj34u2y']")

        if accept_button.is_displayed():
            print("message request accepted from " + user_name)
            accept_button.click()

            time.sleep(5)

            general_button = chrome.find_element(By.XPATH, "//button[@class='xjbqb8w xaqea5y x1b1mbwd xav7gou xtuw4uo "
                                                           "x1ypdohk xvs91rp x1evy7pa xdj266r x11i5rnm xat24cr "
                                                           "x1mh8g0r x1wxaq2x x1iorvi4 x1sxyh0 xjkvuk6 xurb0ha "
                                                           "x2b8uid x87ps6o xxymvpz xh8yej3 x52vrxo x4gyw5p x5n08af']")
            general_button.click()

            time.sleep(5)
        else:
            time.sleep(10)

        pyperclip.copy(message)
        message_box = chrome.find_element(By.XPATH, "//p[@class='xat24cr xdj266r']")
        message_box.send_keys(Keys.CONTROL, "v")

        time.sleep(10)

        message_box.send_keys(Keys.ENTER)

        print(user_name + " has been messaged.")

        time.sleep(20)

        time.sleep(random.randint(180, 300))

    except selenium.common.exceptions.NoSuchElementException:

        print("User not found - go to next user")

        exit_button = chrome.find_element(By.XPATH,
                                          "//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh "
                                          "xyamay9 x1pi30zi x1l90r2v x1swvt13 x1uhb9sk x1plvlek xryxfnj x1c4vz4f "
                                          "x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1']")
        exit_button.click()

        time.sleep(10)


followers = get_list_of_user_names()

initiate_chrome()
login()
go_to_messages()

message_var = {

    1: "Hey! Have you secured your spot for the upcoming AYP Convention? Don’t miss out on this incredible opportunity because ticket prices will increase on July 1. \n\n"
       "🔗 Visit AYP.me/Convention to discover why this event is a must-attend. If you have any questions or need support with scholarship funding to make attending possible, feel free to DM us. \n\n"
       "🎁 As a special incentive, if you register within the next 24 hours & choose “Social Media Platform” as your referral source, we’ll gift you a FREE AYP hoodie! This exclusive offer cannot be combined with other referrals or discount codes. \n\n"
       "Don’t wait any longer – secure your spot now and join us at the AYP Convention! We look forward to seeing you there.",

    2: "Hey! Have you heard about the amazing AYP Convention coming up in just over a month? 🎉 Time is running out, as ticket prices will increase on July 1st. \n\n"
       "To learn more about why the AYP Convention is an absolute must-attend, visit AYP.me/Convention. If you have any questions or need support with scholarship funding to make attending possible, please feel free to send us a DM. We’re here to help! \n\n"
       "But wait, there’s more! 🎁 If you register within the next 24 hours and choose “Social Media Platform” as your referral source, you’ll receive a FREE AYP hoodie as a token of our appreciation. This offer can’t be combined with other referrals or discount codes. \n\n"
       "Don’t wait any longer—secure your spot today and get ready for an unforgettable experience at the AYP Convention. See you there!",

    3: "Have you signed up for the AYP Convention happening next month? If not, don’t wait, because ticket prices go up on July 1. \n\n"
       "Visit AYP.me/Convention to learn more about why this is an event you do not want to miss, and DM us if you have questions or if you need scholarship funding support to make it possible for you to attend. \n\n"
       "As a special prize, if you register in the next 24 hours and select “Social Media Platform” when asked how you heard about the convention, we’ll give you a FREE AYP hoodie! This offer isn’t combinable with other referrals/discount codes."

}

y = 1
for x in range(len(followers)):

    if y == 4:
        y = 1

    dm_user(followers[x], message_var.get(y))
    y += 1
