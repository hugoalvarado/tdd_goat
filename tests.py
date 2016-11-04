
from selenium import webdriver

browser = webdriver.Chrome("D:\python\chromedriver_win32\chromedriver.exe")
browser.get("http://localhost:8000")

assert 'Django' in browser.title