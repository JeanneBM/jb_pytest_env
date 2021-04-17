from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

options = webdriver.FirefoxOptions()
options.headless = True
options.add_argument('--no-sandbox')
driver = webdriver.Firefox(options=options, executable_path='geckodriver')
driver.get('https://www.google.com/')

driver.close()
