import time
from time import gmtime, strftime
import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.ui as ui
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
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1})
from selenium import webdriver
driver = webdriver.Chrome('/Users/marc.jackson/PycharmProjects/untitled/venv/Selenium/Remote/chromedriver')
a = ActionChains(driver)
testurl = 'https://alibi.uktv.co.uk/'
driver.get(testurl)
HomeIconFT = driver.find_element_by_xpath('//*[@id="footer-nav"]/li[1]/a')
TVGuideFT = driver.find_element_by_xpath('//*[@id="footer-nav"]/li[2]/a')
print(TVGuideFT.get_attribute('href'))
OnDemandFT = driver.find_element_by_xpath('//*[@id="footer-nav"]/li[3]/a')
print(OnDemandFT.get_attribute('href'))
ShowsFT = driver.find_element_by_xpath('//*[@id="footer-nav"]/li[4]/a')
print(ShowsFT.get_attribute('href'))
# Footer (Mid)
PrivacyPolicy = driver.find_element_by_xpath('//*[@id="static-footer"]/div[2]/nav/ul/li[1]/a')
print(PrivacyPolicy.get_attribute('href'))
TandC = driver.find_element_by_xpath('//*[@id="static-footer"]/div[2]/nav/ul/li[2]/a')
print(TandC.get_attribute('href'))
CookieFooter = driver.find_element_by_xpath('//*[@id="static-footer"]/div[2]/nav/ul/li[3]/a')
print(CookieFooter.get_attribute('href'))
Slavery = driver.find_element_by_xpath('//*[@id="static-footer"]/div[2]/nav/ul/li[4]/a')
print(Slavery.get_attribute('href'))
ContactUs = driver.find_element_by_xpath('//*[@id="static-footer"]/div[2]/nav/ul/li[5]/a')
print(ContactUs.get_attribute('href'))
Help = driver.find_element_by_xpath('//*[@id="static-footer"]/div[2]/nav/ul/li[6]/a')
print(Help.get_attribute('href'))
Corp = driver.find_element_by_xpath('//*[@id="static-footer"]/div[2]/nav/ul/li[7]/a')
print(Corp.get_attribute('href'))
PG = driver.find_element_by_xpath('//*[@id="static-footer"]/div[2]/nav/ul/li[8]/a')
print(PG.get_attribute('href'))
HowTo = driver.find_element_by_xpath('//*[@id="static-footer"]/div[2]/nav/ul/li[9]/a')
print(HowTo.get_attribute('href'))
# Footer (Bottom)
UKTVCorpLogo = driver.find_element_by_xpath('//*[@id="footer-site-links"]/nav/h4/a')
print(UKTVCorpLogo.get_attribute('href'))
WChannel = driver.find_element_by_xpath('//*[@id="footer-site-links"]/nav/ul[1]/li[1]/a')
print(WChannel.get_attribute('href'))
Dave = driver.find_element_by_xpath('//*[@id="footer-site-links"]/nav/ul[1]/li[2]/a')
print(Dave.get_attribute('href'))
Alibi = driver.find_element_by_xpath('//*[@id="footer-site-links"]/nav/ul[1]/li[3]/a')
print(Alibi.get_attribute('href'))
Gold = driver.find_element_by_xpath('//*[@id="footer-site-links"]/nav/ul[1]/li[4]/a')
print(Gold.get_attribute('href'))
Eden = driver.find_element_by_xpath('//*[@id="footer-site-links"]/nav/ul[2]/li[1]/a')
print(Eden.get_attribute('href'))
Drama = driver.find_element_by_xpath('//*[@id="footer-site-links"]/nav/ul[2]/li[2]/a')
print(Drama.get_attribute('href'))
Yesterday = driver.find_element_by_xpath('//*[@id="footer-site-links"]/nav/ul[2]/li[3]/a')
print(Yesterday.get_attribute('href'))
UKTVPlay = driver.find_element_by_xpath('//*[@id="footer-site-links"]/nav/ul[2]/li[4]/a')
print(UKTVPlay.get_attribute('href'))
# Social Media Links
facebookfooter = driver.find_element_by_xpath('//*[@id="site-footer"]/section/div/ul/li[1]/a')
print(facebookfooter.get_attribute('href'))
twitterfooter = driver.find_element_by_xpath('//*[@id="site-footer"]/section/div/ul/li[2]/a')
print(twitterfooter.get_attribute('href'))
youtubefooter = driver.find_element_by_xpath('//*[@id="site-footer"]/section/div/ul/li[3]/a')
print(youtubefooter.get_attribute('href'))
newsletterfooter = driver.find_element_by_xpath('//*[@id="site-footer"]/section/div/ul/li[4]/a')
print(facebookfooter.get_attribute('href'))
print('Footer Passed')
driver.execute_script("window.open('about:blank', 'tab2');")
driver.switch_to.window("tab2")
driver.get('https://alibi.uktv.co.uk/tv-guide/')
time.sleep(2)
driver.execute_script("window.open('about:blank', 'tab3');")
driver.switch_to.window("tab3")
driver.get('https://alibi.uktv.co.uk/shows/')
time.sleep(2)
driver.execute_script("window.open('about:blank', 'tab4');")
driver.switch_to.window("tab4")
driver.get('https://alibi.uktv.co.uk/videos/')
time.sleep(2)
driver.execute_script("window.open('about:blank', 'tab5');")
driver.switch_to.window("tab5")
driver.get('https://www.facebook.com/alibichannel')
time.sleep(2)
driver.execute_script("window.open('about:blank', 'tab6');")
driver.switch_to.window("tab6")
driver.get('https://twitter.com/Alibi_Channel')
time.sleep(2)
driver.execute_script("window.open('about:blank', 'tab7');")
driver.switch_to.window("tab7")
driver.get('https://www.youtube.com/c/uktv')
time.sleep(2)
driver.execute_script("window.open('about:blank', 'tab8');")
driver.switch_to.window("tab8")
driver.get('https://alibi.uktv.co.uk/myuktv/newsletter-signup')
time.sleep(2)

Email = driver.find_element_by_id('nl_email').send_keys('marc.jackson@uktv.co.uk')
SignUpButtonElement = driver.find_element_by_xpath('//*[@id="nl-signup-btn"]')
SignUpButtonElement.click()

driver.close()
driver.switch_to.window("tab7")
driver.close()
driver.switch_to.window("tab6")
driver.close()
driver.switch_to.window("tab5")
driver.close()
driver.switch_to.window("tab4")

driver.implicitly_wait(1)
PlayVideoClipElement = driver.find_element_by_xpath('//*[@id="main-content"]/div[1]/div/div/div[1]/div[1]/a/i')
PlayVideoClipElement.click()
driver.implicitly_wait(1)
#PlayVideoClip2Element = driver.find_element_by_css_selector('//*[@id="short-form-player"]/button')
#PlayVideoClip2Element.click()
Search = driver.find_element_by_id('site-search-input').send_keys('Quantico')
SearchButtonElement= driver.find_element_by_xpath('//*[@id="site-search-btn"]')
SearchButtonElement.click()
driver.close()
driver.switch_to.window("tab3")
driver.implicitly_wait(3)
#AtoZTabElement = driver.find_element_by_xpath('//*[@id="main-content"]/div[2]/ul/li[2]/a')
#AtoZTabElement.click()
driver.close()
driver.switch_to.window("tab2")