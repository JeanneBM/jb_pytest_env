from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('/home/travis/virtualenv/python3.8.7/lib/python3.8/site-packages/selenium/webdriver/firefox')
browser = webdriver.Firefox(firefox_binary=binary)

