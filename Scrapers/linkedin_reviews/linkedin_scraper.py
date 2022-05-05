# Importing the necessary packages
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import config

# Creating webdriver instance and specifying the path where it's located
driver = webdriver.Chrome(executable_path=r'Scrapers\linkedin_reviews\chromedriver.exe')

# Opening LinkedIn Login page
driver.get("https://linkedin.com/uas/login")

# Waiting for the page to load
time.sleep(5)

# Find the username field
username = driver.find_element_by_id("username")

# Enter Your Email Address
username.send_keys("nahif65174@bunlets.com")

# Find the password field
pword = driver.find_element_by_id("password") 

# Enter Your Password
pword.send_keys("I(o(h7M9M;,Y")

# This will click the login button on LinkedIn
driver.find_element_by_xpath("//button[@type='submit']").click()


search = driver.find_element_by_xpath("//*[@id="global-nav-typeahead"]/input")

search.send_keys('#Cronosgroep')
