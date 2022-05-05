# Importing the necessary packages
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time

# Creating webdriver instance and specifying the path where it's located
driver = webdriver.Chrome(executable_path=r'Scrapers\linkedin_reviews\chromedriver.exe')

# Opening LinkedIn Login page
driver.get("https://linkedin.com/uas/login")

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


search = driver.find_element(By.CSS_SELECTOR, '.search-global-typeahead')

search_term = 'cronosgroep'

search_url = f'https://www.linkedin.com/search/results/content/?keywords=%23{search_term}&sid=zo(&update=urn%3Ali%3Afs_updateV2%3A(urn%3Ali%3Aactivity%3A6883854498977132544%2CBLENDED_SEARCH_FEED%2CEMPTY%2CDEFAULT%2Cfalse)'

driver.get(search_url)


start = time.time()
  
# will be used in the while loop
initialScroll = 0
finalScroll = 1000
  
while True:
    driver.execute_script(f"window.scrollTo({initialScroll}, {finalScroll})")
    # this command scrolls the window starting from
    # the pixel value stored in the initialScroll 
    # variable to the pixel value stored at the
    # finalScroll variable
    initialScroll = finalScroll
    finalScroll += 1000
  
    # we will stop the script for 3 seconds so that 
    # the data can load
    time.sleep(3)
    # You can change it as per your needs and internet speed
  
    end = time.time()
  
    # We will scroll for 20 seconds.
    # You can change it as per your needs and internet speed
    if round(end - start) > 20:
        break

src = driver.page_source
  
# Now using beautiful soup
soup = BeautifulSoup(src, 'lxml')
soup.find('span', class_ = 'break-words').text
print(soup)