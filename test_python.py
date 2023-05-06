from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install()

browser = webdriver.Chrome()
browser.get("https://www.python.org")
assert "Welcome to Python.org" in browser.title
time.sleep(10)
browser.close()