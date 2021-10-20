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
testurl = 'https://uktvplay.uktv.co.uk/shows/red-dwarf-the-promised-land/watch-online'
driver.get(testurl)
time.sleep(2)
CookieNotice = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/h2')
CookiePolicy = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/a').get_attribute('href')
print(CookiePolicy)
CookieYes = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/button').click()

#Episode Landing Page Elements
EpisodeThumbnail= driver.find_element_by_xpath('//*[@id="watch-video-player"]/div[1]/div/div[1]')
EpisodeThumbnail.click()
time.sleep(2)
SigninButton= driver.find_element_by_xpath('//*[@id="login-overlay"]/div/div/a[2]/button')
SigninButton.click()
time.sleep(2)

email = driver.find_element_by_id('email').send_keys('marc.jackson@uktv.co.uk')
password = driver.find_element_by_id('password').send_keys('Batman47')
signin = driver.find_element_by_id('sign-in-btn').click()
time.sleep(4)

Playbutton= driver.find_element_by_xpath('//*[@id="watch-video-player"]/div[2]/a')
Playbutton.click()
time.sleep(2)
AddFavourite= driver.find_element_by_xpath('//*[@id="add-to-favourites"]')
AddFavourite.click()
time.sleep(3)
RemoveFavourite= driver.find_element_by_xpath('//*[@id="add-to-favourites"]')
RemoveFavourite.click()
driver.implicitly_wait(10)
ShareButton= driver.find_element_by_xpath('//*[@id="episode-details"]/div/div[1]/div/div[2]/div/button')
ShareButton.click()
driver.implicitly_wait(10)
AutoPlaybutton= driver.find_element_by_xpath('//*[@id="episode-details"]/div/div[1]/div/button/span')
AutoPlaybutton.click()
#SubtitlesIcon= driver.find_element_by_xpath('//*[@id="episode-details"]/div/div[2]/div[1]/div/div[2]')
#print(SubtitlesIcon)
time.sleep(2)
EpisodeOnTv= driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/section/div/div[2]/button')
EpisodeOnTv.click()
time.sleep(1)
EpisodesOnDemand= driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/section/div/div[1]')
EpisodesOnDemand.click()
time.sleep(1)
SeriesDropdown= driver.find_element_by_xpath('//*[@id="main"]/div/div/div[2]/div/section/div/div[1]')
SeriesDropdown.click()
Carousel1Right= driver.find_element_by_xpath('//*[@id="collection"]/div/div/section/div/div/div/div/button[2]')
Carousel1Right.click()
time.sleep(1)
Carousel1Left= driver.find_element_by_xpath('//*[@id="collection"]/div/div/section/div/div/div/div/button[1]')
Carousel1Left.click()
time.sleep(1)
Carousel2Right= driver.find_element_by_xpath('//*[@id="watch-related-carousel"]/div/div/button[2]')
Carousel2Right.click()
time.sleep(1)
Carousel2Left = driver.find_element_by_xpath('//*[@id="watch-related-carousel"]/div/div/button[1]')
Carousel2Left.click()