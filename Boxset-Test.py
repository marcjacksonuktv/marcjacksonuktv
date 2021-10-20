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


#Cookie Notice
CookieNotice = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div')
CookiePolicy = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/a').get_attribute('href')
print(CookiePolicy)
time.sleep(2)
CookieYes = driver.find_element_by_css_selector('#app > div.cookie-consent > div > div > button').click()

#Collections Tab
CollectionsTab = driver.find_element_by_xpath('//*[@id="main"]/div/div/section/div/div[2]/a/span').click()
time.sleep(2)
CollectionHighlight= driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/section/div/div/div/div/button[2]').click()
CollectionHighlight2= driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/section/div/div/div/div/button[1]').click()
CollectionDave= driver.find_element_by_xpath('//*[@id="main"]/div/div[3]/div/div/section/div/div/div/div/button[2]').click()
CollectionDave2= driver.find_element_by_xpath('//*[@id="main"]/div/div[3]/div/div/section/div/div/div/div/button[1]').click()
CollectionEngineer = driver.find_element_by_xpath('//*[@id="main"]/div/div[4]/div/div/section/div/div/div/div/button[2]').click()
CollectionEngineer2= driver.find_element_by_xpath('//*[@id="main"]/div/div[4]/div/div/section/div/div/div/div/button[1]').click()
CollectionOriginal= driver.find_element_by_xpath('//*[@id="main"]/div/div[5]/div/div/section/div/div/div/div/button[2]').click()
CollectionOriginal2= driver.find_element_by_xpath('//*[@id="main"]/div/div[5]/div/div/section/div/div/div/div/button[1]').click()
CollectionNostal= driver.find_element_by_xpath('//*[@id="main"]/div/div[6]/div/div/section/div/div/div/div/button[2]').click()
CollectionNostal2= driver.find_element_by_xpath('//*[@id="main"]/div/div[6]/div/div/section/div/div/div/div/button[1]').click()
CollectionNazi= driver.find_element_by_xpath('//*[@id="main"]/div/div[7]/div/div/section/div/div/div/div/button[2]').click()
CollectionNazi2= driver.find_element_by_xpath('//*[@id="main"]/div/div[7]/div/div/section/div/div/div/div/button[1]').click()
CollectionShorts= driver.find_element_by_xpath('//*[@id="main"]/div/div[8]/div/div/section/div/div/div/div/button[2]').click()
CollectionShorts2= driver.find_element_by_xpath('//*[@id="main"]/div/div[8]/div/div/section/div/div/div/div/button[1]').click()
CollectionDavee= driver.find_element_by_xpath('//*[@id="main"]/div/div[9]/div/div/section/div/div/div/div/button[2]').click()
CollectionDavee2= driver.find_element_by_xpath('//*[@id="main"]/div/div[9]/div/div/section/div/div/div/div/button[1]').click()
CollectionYesterday= driver.find_element_by_xpath('//*[@id="main"]/div/div[10]/div/div/section/div/div/div/div/button[2]').click()
CollectionYesterday2= driver.find_element_by_xpath('//*[@id="main"]/div/div[10]/div/div/section/div/div/div/div/button[1]').click()
logofooter = driver.find_element_by_xpath('//*[@id="app"]/footer/div/a/img')
a.move_to_element(logofooter).perform()
OpenThumbnail =driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/section/div/div/div/div/div[1]/a/div/div[3]').click()
time.sleep(2)
#Boxsets
BoxsetTab = driver.find_element_by_xpath('//*[@id="app"]/div/div/nav/ul/li[3]/a').click()
time.sleep(2)
AtoZButton= driver.find_element_by_xpath('//*[@id="box-sets-sort-buttons"]/div[2]/button').click()
time.sleep(2)
MostPopular = driver.find_element_by_xpath('//*[@id="box-sets-sort-buttons"]/div[1]/button').click()
time.sleep(1)
Openboxset1 = driver.find_element_by_xpath('//*[@id="box-sets-grid"]/div/div/div[1]/a/div/div[2]').click()


