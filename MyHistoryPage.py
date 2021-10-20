import time
from time import gmtime, strftime
import datetime
#import conf as conf
now = datetime.datetime.now()
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
options = Options()
options.add_argument('--user-data-dir=/Users/marc.jackson/Desktop/SeleniumLogOn')
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.g§ eolocation": 1,
    "profile.default_content_setting_values.notifications": 1})
from selenium import webdriver
driver = webdriver.Chrome('/Users/marc.jackson/PycharmProjects/untitled/venv/Selenium/Remote/chromedriver')
a = ActionChains(driver)
testurl = 'https://uktv:wemakegreattv@uktvplay.uatuktv.co.uk/'
driver.get(testurl)

driver.implicitly_wait(2)
CookieNotice = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/h2')
CookiePolicy = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/a').get_attribute('href')
print(CookiePolicy)
CookieYes = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/button').click()

SignInToAccount = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]')
SignInToAccount.click()

driver.implicitly_wait(5)
Email = driver.find_element_by_id('email').send_keys('favourites@history.co.uk')
password = driver.find_element_by_id('password').send_keys('favhis123')
SignIn = driver.find_element_by_id('sign-in-btn').click()

driver.implicitly_wait(10)
FirstThumbnail = driver.find_element_by_xpath('//*[@id="hero-block"]/div/section/div/div/div/div/div[1]/a/div')
FirstThumbnail.click()

driver.implicitly_wait(10)
ContinueWithoutButton = driver.find_element_by_xpath('//*[@id="watch-video-player"]/div/div/div[2]/div/section/div/div/button[2]')
ContinueWithoutButton.click()

driver.implicitly_wait(3)
AddToFavouritesButton = driver.find_element_by_xpath('//*[@id="add-to-favourites"]')
AddToFavouritesButton.click()

driver.implicitly_wait(3)
MylistButton = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/a/div/span')
MylistButton.click()

driver.implicitly_wait(3)
driver.refresh()
DeleteButton = driver.find_element_by_xpath('//*[@id="Close-X"]')
DeleteButton.click()

ChannelsPages = driver.find_element_by_xpath('//*[@id="app"]/div/div/nav/ul/li[2]/a')
ChannelsPages.click()

driver.implicitly_wait(3)
DaveChannelButton = driver.find_element_by_xpath('//*[@id="main-content"]/div[1]/div[1]/div/a/button')
DaveChannelButton.click()

driver.implicitly_wait(5)
UKComedyThumbnail = driver.find_element_by_xpath('//*[@id="hero-block"]/div/section/div/div/div/div/div[2]/a/div/div[2]')
UKComedyThumbnail.click()

driver.implicitly_wait(10)
ContinueWithoutButton = driver.find_element_by_xpath('//*[@id="watch-video-player"]/div/div/div[2]/div/section/div/div/button[2]')
ContinueWithoutButton.click()

driver.implicitly_wait(10)
PlayVideoButton = driver.find_element_by_xpath('//*[@id="watch-video-player"]/div[2]/a')
PlayVideoButton.click()

driver.implicitly_wait(10)
MylistButton = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/a/div/span')
MylistButton.click()

MyHistoryTab = driver.find_element_by_xpath('//*[@id="main-content"]/div/section/div/div[2]/a/span')
MyHistoryTab.click()
driver.refresh()

driver.implicitly_wait(4)
DeleteButton = driver.find_element_by_xpath('//*[@id="Close-X"]')
DeleteButton.click()