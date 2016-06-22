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

browser.get("https://app.bill.com/")

emailElem = browser.find_element_by_id('email')
emailElem.send_keys("yourusername")
passwordElem = browser.find_element_by_id("password")
passwordElem.send_keys("yourpassword")
passwordElem.submit()
linkElem = browser.find_element_by_link_text('your org name')
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

browser.quit()
