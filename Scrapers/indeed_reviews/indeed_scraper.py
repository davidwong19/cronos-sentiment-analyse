import requests, re, pymongo
from bs4 import BeautifulSoup
from datetime import datetime
from googletrans import Translator
import pandas as pd
from pymongo import MongoClient

def extract():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; 6x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'}
    url = 'https://be.indeed.com/cmp/Cronos-Interactive/reviews'
    # url = 'https://be.indeed.com/cmp/Cronos/reviews'
    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):

    divs = soup.find_all('div', class_ = 'cmp-ReviewsList')
    
    for item in divs:
        translator = Translator()
        rating = item.find('button', class_ = 'css-1c33izo').text.strip()
        author_info = item.find('span', class_ = 'css-xvmbeo').text.strip()
        
        date = re.sub(r'^.*(?=(\d{2} \w{3,} \d{4}))', '', author_info) # Regex to extract the date 
        date_en = translator.translate(date).text #translate the date to english, otherwise it will give problems when converting to dd/mm/YYYY
        try: 
            date_clean = datetime.strptime(date_en, r'%d %B %Y').date()
            break
        except ValueError:
            date_clean = datetime.strptime(date_en, r'%B %d, %Y').date()
        date_clean_str = date_clean.strftime('%d/%m/%Y')

        opinion = item.find('div', class_ = 'css-rr5fiy').text.strip()
    
        translator = Translator()
        opinion_en = translator.translate(opinion).text
        
        review = {
            'rating': rating,
            'opinion': opinion_en,
            'date': date_clean_str,
            'source': 'indeed',
            'company': 'Cronos Interactive' # CHANGE THIS
        }
        reviewlist.append(review)
    return

reviewlist = []

c = extract()
transform(c)

# client = MongoClient ('mongodb+srv://user_2:123@cluster0.1g3pv.mongodb.net/test')
# db = client['cronos_sentiment']
# collection = db['NEW_reviews_cronos_groep']

# qry = { 'company': 'Cronos Interactive'}

# doc = collection.find(qry)

# for x in doc:
#     print(x)

# df = pd.DataFrame(reviewlist)
# print(df.head())
# df.to_csv(r'C:\Users\Rehts\Documents\Repositories\cronos-sentiment-analyse\Scrapers\indeed_reviews\CSV_Files\reviews_indeed.csv', mode='a', index=False, header=False) # The directory needs to be changed to where reviews_indeed.csv is located
