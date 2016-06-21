#!/usr/bin/env python

from pyvirtualdisplay import Display
from selenium import webdriver
import datetime
import urllib
from urlparse import urljoin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

browser = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
# browser.set_preference('browser.download.folderList', 2) # custom location
# browser.set_preference('browser.download.manager.showWhenStarting', False)
# browser.set_preference('browser.download.dir', '/tmp')
# browser.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')


# browser = webdriver.Chrome()
# browser = webdriver.Firefox()
# browser = webdriver.Firefox(executable_path='/Applications/Firefox.app/Contents/MacOS/firefox-bin')
# browser.set_window_size(1024, 768)
browser.get("https://app.bill.com/")
# browser.find_element_by_id('search_form_input_homepage').send_keys("realpython")
# browser.find_element_by_id("search_button_homepage").click()
emailElem = browser.find_element_by_id('email')
emailElem.send_keys("edunn@hq.bill.com")
passwordElem = browser.find_element_by_id("password")
passwordElem.send_keys("Warriorsrock1!")
passwordElem.submit()
linkElem = browser.find_element_by_link_text('Puryst Software QBE')
linkElem.click()
browser.get("https://app.bill.com/Exports/Profile?type=Bill")
buttonElem = browser.find_element_by_name("ExportAll")
buttonElem.click()
now = datetime.datetime.now()

print now.strftime("%m-%d-%y")
fileDate = now.strftime("%m-%d-%y")
print fileDate
partialLinkElem = WebDriverWait(browser, 120).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, fileDate)))
link = partialLinkElem.get_attribute('href')
print link
session = requests.Session()
cookies = browser.get_cookies()
for cookie in cookies:
	session.cookies.set(cookie['name'], cookie['value'])
response = session.get(link)
text_file = open(fileDate + ".csv", "w")
text_file.write(response.content)
text_file.close()
print response.content
# urllib.urlretrieve(link, "my.csv")
# print('Looping until file is retrieved')
# downloaded_file = None
# while downloaded_file is None:
#	partialLinkElem = browser.find_element_by_partial_link_text(fileDate)
#	if not downloaded_file:
#		print('\tNot downloaded, waiting ....')
#		time.sleep(0.5)
# partialLinkElem.click()
# print browser.current_url

browser.quit()
