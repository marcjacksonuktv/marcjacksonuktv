# driver = webdriver.Safari(executable_path = '/usr/bin/safaridriver')
# driver = webdriver.Firefox(executable_path='/Users/aaron.sudhera/PycharmProjects/venv/Selenium/Remote/geckodriver')
# driver = webdriver.Edge(executable_path='/Users/aaron.sudhera/PycharmProjects/venv/Selenium/Remote/msedgedriver')
# driver = webdriver.Opera(executable_path='/Users/aaron.sudhera/PycharmProjects/venv/Selenium/Remote/operadriver')
# -*- coding: utf-8 -*-
#import sys
#import time
#from time import gmtime, strftime
#import datetime
#import conf as conf
#now = datetime.datetime.now()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.opera.options import Options
from selenium.webdriver.safari.permissions import Permission
# Create a folder on your laptop
options = Options()
options.add_argument('--user-data-dir=/Users/james.stott/Desktop/SeleniumLogOn')
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1})
from selenium import webdriver
driver = webdriver.Chrome('/Users/marc.jackson/PycharmProjects/untitled/venv/Selenium/Remote/chromedriver')
testurl = 'https://uktvplay.uktv.co.uk/'
driver.get(testurl)
#time.sleep(2)

CookieYes = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/button')
CookieYes.click()

# My Account Register
MyAccount = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]')
MyAccount.click()
