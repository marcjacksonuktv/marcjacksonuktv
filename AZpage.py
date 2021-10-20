import time
from time import gmtime, strftime
import datetime

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
testurl = 'https://uktvplay.uktv.co.uk/shows/'
driver.get(testurl)
time.sleep(2)

CookieNotice = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/h2')
CookiePolicy = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/a').get_attribute('href')
print(CookiePolicy)
CookieYes = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/button').click()
logofooter = driver.find_element_by_xpath('//*[@id="app"]/footer/div/a/img')
AtoZNav = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]')
availableShowsToggle= driver.find_element_by_xpath('//*[@id="section-0"]/div[1]/div/div[2]')
availableShowsToggle.click()
time.sleep(2)
availableShowsToggle.click()

Letters = driver.find_element_by_css_selector('#section-0 > div.title-switch-wrap > h2')
print(Letters.is_displayed)
a.move_to_element(logofooter).perform()
time.sleep(2)
a.move_to_element(AtoZNav).perform()
TabB = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/span[2]')
TabB.click()
print(TabB.text)
a.move_to_element(logofooter).perform()
time.sleep(2)
a.move_to_element(AtoZNav).perform()
TabC = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/span[3]')
TabC.click()
print(TabC.text)
a.move_to_element(logofooter).perform()
time.sleep(2)
a.move_to_element(AtoZNav).perform()
TabD = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/span[4]')
TabD.click()
print(TabD.text)
a.move_to_element(logofooter).perform()
time.sleep(2)
a.move_to_element(AtoZNav).perform()
TabE = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/span[5]')
TabE.click()
print(TabE.text)
a.move_to_element(logofooter).perform()
time.sleep(2)
a.move_to_element(AtoZNav).perform()
TabF = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/span[6]')
TabF.click()
print(TabF.text)
a.move_to_element(logofooter).perform()
time.sleep(2)
a.move_to_element(AtoZNav).perform()
TabG = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/span[7]')
TabG.click()
print(TabG.text)
a.move_to_element(logofooter).perform()
time.sleep(2)
a.move_to_element(AtoZNav).perform()
TabH = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/span[8]')
TabH.click()
print(TabH.text)
a.move_to_element(logofooter).perform()
time.sleep(2)
a.move_to_element(AtoZNav).perform()
TabI = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/span[9]')
TabI.click()
print(TabI.text)
a.move_to_element(logofooter).perform()
time.sleep(2)
a.move_to_element(AtoZNav).perform()
TabJ = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/span[10]')
TabJ.click()
print(TabJ.text)
a.move_to_element(logofooter).perform()
time.sleep(2)
a.move_to_element(AtoZNav).perform()
TabK = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/span[11]')
TabK.click()
print(TabK.text)
a.move_to_element(logofooter).perform()
time.sleep(2)
a.move_to_element(AtoZNav).perform()
TabL = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/span[12]')
TabL.click()
print(TabL.text)
a.move_to_element(logofooter).perform()
time.sleep(2)
a.move_to_element(AtoZNav).perform()
#TabM = driver.find_elements_by_xpath('//*[@id="main"]/div/div[2]/div/div/span[13]')
#TabM.click()
#print(Letters.is_displayed)
TabN = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/span[14]')
TabN.click()
print(TabN.text)
a.move_to_element(logofooter).perform()
time.sleep(2)
a.move_to_element(AtoZNav).perform()
TabP = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/span[16]')
TabP.click()
print(TabP.text)
a.move_to_element(logofooter).perform()
time.sleep(2)
a.move_to_element(AtoZNav).perform()
TabQ = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/span[17]')
TabQ.click()
print(TabQ.text)
a.move_to_element(logofooter).perform()
time.sleep(2)
a.move_to_element(AtoZNav).perform()
TabR = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/span[18]')
TabR.click()
print(TabR.text)
a.move_to_element(logofooter).perform()
time.sleep(2)
a.move_to_element(AtoZNav).perform()
TabS = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/span[19]')
TabS.click()
print(TabS.text)
a.move_to_element(logofooter).perform()
time.sleep(2)
a.move_to_element(AtoZNav).perform()
TabT = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/span[20]')
TabT.click()
print(TabT.text)
a.move_to_element(logofooter).perform()
time.sleep(2)
a.move_to_element(AtoZNav).perform()
TabU = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/span[21]')
TabU.click()
print(TabU.text)
a.move_to_element(logofooter).perform()
time.sleep(2)
a.move_to_element(AtoZNav).perform()
time.sleep(2)
TabV = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/span[22]')
TabV.click()
print(TabV.text)
a.move_to_element(logofooter).perform()
time.sleep(2)
a.move_to_element(AtoZNav).perform()
TabW = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/span[23]')
TabW.click()
print(TabW.text)
a.move_to_element(logofooter).perform()
time.sleep(2)
a.move_to_element(AtoZNav).perform()
TabY = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/span[25]')
TabY.click()
print(TabY.text)
a.move_to_element(logofooter).perform()
time.sleep(2)
a.move_to_element(AtoZNav).perform()
TabZ = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/span[26]')
TabZ.click()
print(TabZ.text)
a.move_to_element(logofooter).perform()
time.sleep(2)
a.move_to_element(AtoZNav).perform()
TabNumbered= driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/span[27]')
TabNumbered.click()
print(TabNumbered.text)
a.move_to_element(logofooter).perform()
time.sleep(2)
a.move_to_element(AtoZNav).perform()