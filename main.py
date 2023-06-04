from selenium import webdriver
import configparser


# https://www.geeksforgeeks.org/send-direct-message-on-instagram-using-selenium-in-python/
# https://www.youtube.com/watch?v=Xjv1sY630Uc&list=PLzMcBGfZo4-n40rB1XaJ0ak1bemvlqumQ

parser = configparser.ConfigParser()
parser.read('credentials.txt')




def path():
    chrome = webdriver.Chrome()
    chrome.get('https://www.instagram.com/')


path()












