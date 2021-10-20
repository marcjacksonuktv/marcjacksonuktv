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
testurl = 'https://uktv:wemakegreattv@uktvplay.uatuktv.co.uk/'
driver.get(testurl)

SignInToAccount = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]')
SignInToAccount.click()

driver.implicitly_wait(5)
Email = driver.find_element_by_id('email').send_keys('favourites@history.co.uk')
password = driver.find_element_by_id('password').send_keys('favhis123')
SignIn = driver.find_element_by_id('sign-in-btn').click()

driver.implicitly_wait(10)
CookieNotice = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/h2')
CookiePolicy = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/a').get_attribute('href')
print(CookiePolicy)
CookieYes = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/button').click()


FeaturedCarouselL1 = driver.find_element_by_xpath('//*[@id="featured-carousel"]/div/div/button[2]')
time.sleep(1)
FeaturedCarouselL1 .click()
time.sleep(1)
FeaturedCarouselL1.click()
time.sleep(1)
FeaturedCarouselR1 = driver.find_element_by_xpath('//*[@id="featured-carousel"]/div/div/button[1]')
FeaturedCarouselR1.click()
time.sleep(1)
FeaturedCarouselR1.click()
time.sleep(1)
CWCarouselL = driver.find_element_by_xpath('//*[@id="continue-watching-carousel"]/div/div/button[2]')
CWCarouselL.click()
time.sleep(1)
CWCarouselL.click()
time.sleep(1)
CWCarouselR = driver.find_element_by_xpath('//*[@id="continue-watching-carousel"]/div/div/button[1]')
CWCarouselR.click()
time.sleep(1)
CWCarouselR.click()
time.sleep(1)
Carousel1next = driver.find_element_by_xpath('//*[@id="series-highlights-carousel"]/div/div/button[2]')
Carousel1next.click()
time.sleep(1)
Carousel1previous = driver.find_element_by_xpath('//*[@id="series-highlights-carousel"]/div/div/button[1]')
Carousel1previous.click()
time.sleep(1)
Carousel2next = driver.find_element_by_xpath('//*[@id="subcategory-1-carousel"]/div/div/button[2]')
Carousel2next.click()
time.sleep(1)
Carousel2previous = driver.find_element_by_xpath('//*[@id="subcategory-1-carousel"]/div/div/button[1]')
Carousel2previous.click()
time.sleep(1)
Carousel3next = driver.find_element_by_xpath('//*[@id="subcategory-2-carousel"]/div/div/button[2]')
Carousel3next.click()
time.sleep(1)
Carousel3previous = driver.find_element_by_xpath('//*[@id="subcategory-2-carousel"]/div/div/button[1]')
Carousel3previous.click()
time.sleep(1)
SpotlightCarouselnext = driver.find_element_by_xpath('//*[@id="spotlight"]/section/div/div/div/div/button[2]')
SpotlightCarouselnext.click()
time.sleep(1)
SpotlightCarouselprevious = driver.find_element_by_xpath('//*[@id="spotlight"]/section/div/div/div/div/button[1]')
SpotlightCarouselprevious.click()
time.sleep(1)
MoreLike1Carouselnext = driver.find_element_by_xpath('//*[@id="morelike-1-carousel"]/div/div/button[2]')
MoreLike1Carouselnext.click()
time.sleep(1)
MoreLike1Carouselprevious= driver.find_element_by_xpath('//*[@id="morelike-1-carousel"]/div/div/button[1]')
MoreLike1Carouselprevious.click()
time.sleep(1)
MoreLike2Carouselnext= driver.find_element_by_xpath('//*[@id="morelike-2-carousel"]/div/div/button[2]')
MoreLike2Carouselnext.click()
time.sleep(1)
MoreLike2CarouselPrevious= driver.find_element_by_xpath('//*[@id="morelike-2-carousel"]/div/div/button[1]')
MoreLike2CarouselPrevious.click()
time.sleep(1)