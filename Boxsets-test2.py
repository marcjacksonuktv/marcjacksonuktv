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
a = ActionChains(driver)
testurl = 'https://uktvplay.uktv.co.uk/box-sets/'
driver.get(testurl)

time.sleep(2)
CookieNotice = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/h2')
CookiePolicy = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/a').get_attribute('href')
print(CookiePolicy)
CookieYes = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/button').click()

# Collections Tab
CollectionsTab = driver.find_element_by_xpath('//*[@id="main"]/div/div/section/div/div[2]/a/span')
CollectionsTab.click()
time.sleep(2)
CollectionHighlight = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/section/div/div/div/div/button[2]')
CollectionHighlight2 = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/section/div/div/div/div/button[1]')
CollectionDave = driver.find_element_by_xpath('//*[@id="main"]/div/div[3]/div/div/section/div/div/div/div/button[2]')
CollectionDave2 = driver.find_element_by_xpath('//*[@id="main"]/div/div[3]/div/div/section/div/div/div/div/button[1]')
CollectionEngineer = driver.find_element_by_xpath('//*[@id="main"]/div/div[4]/div/div/section/div/div/div/div/button[2]')
CollectionEngineer2 = driver.find_element_by_xpath('//*[@id="main"]/div/div[4]/div/div/section/div/div/div/div/button[1]')
CollectionOriginal = driver.find_element_by_xpath('//*[@id="main"]/div/div[5]/div/div/section/div/div/div/div/button[2]')
CollectionOriginal2 = driver.find_element_by_xpath('//*[@id="main"]/div/div[5]/div/div/section/div/div/div/div/button[1]')
CollectionNostal = driver.find_element_by_xpath('//*[@id="main"]/div/div[6]/div/div/section/div/div/div/div/button[2]')
CollectionNostal2 = driver.find_element_by_xpath('//*[@id="main"]/div/div[6]/div/div/section/div/div/div/div/button[1]')
CollectionNazi = driver.find_element_by_xpath('//*[@id="main"]/div/div[7]/div/div/section/div/div/div/div/button[2]')
CollectionNazi2 = driver.find_element_by_xpath('//*[@id="main"]/div/div[7]/div/div/section/div/div/div/div/button[1]')
CollectionShorts = driver.find_element_by_xpath('//*[@id="main"]/div/div[8]/div/div/section/div/div/div/div/button[2]')
CollectionShorts2 = driver.find_element_by_xpath('//*[@id="main"]/div/div[8]/div/div/section/div/div/div/div/button[1]')
CollectionDavee = driver.find_element_by_xpath('//*[@id="main"]/div/div[9]/div/div/section/div/div/div/div/button[2]')
CollectionDavee2 = driver.find_element_by_xpath('//*[@id="main"]/div/div[9]/div/div/section/div/div/div/div/button[1]')
CollectionYesterday = driver.find_element_by_xpath('//*[@id="main"]/div/div[10]/div/div/section/div/div/div/div/button[2]')
CollectionYesterday2 = driver.find_element_by_xpath('//*[@id="main"]/div/div[10]/div/div/section/div/div/div/div/button[1]')
OpenThumbnail = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/section/div/div/div/div/div[1]/a/div/div[3]')
CollectionHighlight.click()
CollectionHighlight2.click()
CollectionDave.click()
CollectionDave2.click()
CollectionEngineer.click()
CollectionEngineer2.click()
CollectionOriginal.click()
CollectionOriginal2.click()
CollectionNostal.click()
CollectionNostal2.click()
CollectionNazi.click()
CollectionNazi2.click()
CollectionShorts.click()
CollectionShorts2.click()
CollectionDavee.click()
CollectionDavee2.click()
CollectionYesterday.click()
CollectionYesterday2.click()
logofooter = driver.find_element_by_xpath('//*[@id="app"]/footer/div/a/img')
a.move_to_element(logofooter).perform()
OpenThumbnail.click()
time.sleep(2)
driver.get('https://uktvplay.uktv.co.uk/box-sets/')
time.sleep(2)
# Boxsets
BoxsetTab = driver.find_element_by_xpath('//*[@id="app"]/div/div/nav/ul/li[3]/a')
AtoZButton = driver.find_element_by_xpath('//*[@id="box-sets-sort-buttons"]/div[2]/button')
MostPopular = driver.find_element_by_xpath('//*[@id="box-sets-sort-buttons"]/div[1]/button')
BoxsetTab.click()
time.sleep(2)
AtoZButton.click()
time.sleep(2)
MostPopular.click()
time.sleep(3)
Openboxset1 = driver.find_element_by_xpath('//*[@id="box-sets-grid"]/div/div/div[1]/a/div/div[2]')
Openboxset1.click()