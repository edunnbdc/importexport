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

emailElem = browser.find_element_by_name('email')
emailElem.send_keys("your email username here")
passwordElem = browser.find_element_by_id('password')
passwordElem.send_keys("your password here")
passwordElem.submit()
linkElem = browser.find_element_by_link_text('Your og name here')
linkElem.click()
browser.get("https://app.bill.com/Imports/Upload?type=Vendor")
fileElem = browser.find_element_by_name('file1')
fileElem.send_keys("/Users/edunn/Downloads/VendorImportTest.csv")
print fileElem.text
fileElem.submit()
print browser.current_url
nextElem = WebDriverWait(browser, 120).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Preferences')))
nextElem = browser.find_element_by_id('uploadId')
nextElem.submit()
print browser.current_url

browser.quit()
