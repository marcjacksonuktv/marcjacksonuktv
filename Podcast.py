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
testurl = 'https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy9mNTI5YzQ4L3BvZGNhc3QvcnNz'
driver.get(testurl)

driver.implicitly_wait(5)
PlayFirstEpisode= driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/c-wiz/div/c-wiz/div/div[2]/a[1]/div/div[4]/div/div')
PlayFirstEpisode.click()
time.sleep(5)
