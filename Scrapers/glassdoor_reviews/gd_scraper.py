# Import necessary packages
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from googletrans import Translator
import pandas as pd

# Function for extracting the page
def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'} # For additional information with request
    #url = f'https://nl.glassdoor.be/Reviews/Cronos-Reviews-E871033_{page}.htm?sort.sortType=RD&sort.ascending=false&filter.iso3Language=nld' 
    url = f'https://www.glassdoor.co.uk/Reviews/Cronos-Reviews-E871033_{page}.htm?sort.sortType=RD&sort.ascending=false&filter.iso3Language=eng'
    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

# Function for transforming the page content to a dictionary
def transform(soup):
    # Div with all the reviews inside
    divs = soup.find_all('div', class_ = 'gdReview')
    
    # Going over each review in the div
    for item in divs:
        rating = item.find('span', class_ = 'ratingNumber mr-xsm').text.strip() # Get Rating
        author_info = item.find('span', class_ = 'authorJobTitle').text.strip() # Get AuthorInfo
        
        index = author_info.find(' -') # Get index of '-'
        date = author_info[:index] # Get the date from 0 index
        date_clean = datetime.strptime(date, '%b %d, %Y').date() # Convert date to datetime object, %Y %m %d
        date_clean_str = date_clean.strftime('%d/%m/%Y') # Convert datetime to str with format of dd/mm/yyyy

        pros = item.find('span', {'data-test':'pros'}).text.strip().replace('\r\n', '') # Get pros
        cons = item.find('span', {'data-test':'cons'}).text.strip().replace('\r\n', '') # Get cons
        opinion = pros + ', ' + cons # Combining pros and cons in one opinion string

        # This piece of code will translate the opinion in whatever language to EN
        #translator = Translator()
        #opinion_tr = translator.translate(opinion).text # Get only the translated text
        
        # Put in an dictionary
        review = {
            'rating': rating,
            'opinion': opinion,
            'date': date_clean_str,
            'source': 'glassdoor'
        }
        reviewlist.append(review) # Adding the dictionary to a list
    return

reviewlist = []

# Going over the pages
for i in range(0, 10):
    print(f'Getting page {i}')
    c = extract(f'P{i}')
    transform(c)

# Writing to a CSV
df = pd.DataFrame(reviewlist) # List to pandas dataframe
print(df.head()) # Printing the first few entries of the pandas dataframe, to check
df.to_csv('./CSV_Files/reviews_gd_en.csv', index=False) # Converting pandas dataframe to a CSV file