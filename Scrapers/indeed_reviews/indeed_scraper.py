import requests, re, locale
from bs4 import BeautifulSoup
from datetime import datetime
from googletrans import Translator
import pandas as pd


def extract():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'}
    url = 'https://be.indeed.com/cmp/Cronos-Interactive/reviews'
    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):

    divs = soup.find_all('div', class_ = 'cmp-ReviewsList')
    
    for item in divs:
        translator = Translator()
        rating = item.find('button', class_ = 'css-1c33izo').text.strip()
        author_info = item.find('span', class_ = 'css-xvmbeo').text.strip()
        
        date = re.sub(r'^.*(?=(\d{2} \w{3,} \d{4}))', '', author_info)
        date_en = translator.translate(date).text #translate the date to english, otherwise it will give problems when converting to dd/mm/YYYY
        date_clean = datetime.strptime(date_en, r'%B %d, %Y').date()
        date_clean_str = date_clean.strftime('%d/%m/%Y')

        sum = item.find('div', class_ = 'css-rr5fiy').text.strip()
        pros = item.find('div', class_ = 'css-82l4gy eu4oa1w0')[0].text.strip()
        print(pros)
        # cons = item.find('span', class_ = 'css-82l4gy eu4oa1w0').text.strip().replace('\r\n', '')
        # opinion = f'{sum}, {pros}, {cons}'

        # translator = Translator()
        # opinion_en = translator.translate(opinion).text
        
        # review = {
        #     'rating': rating,
        #     'opinion': opinion_en,
        #     'date': date_clean_str,
        #     'source': 'indeed',
        #     'company': '' # CHANGE THIS
        # }
        # reviewlist.append(review)
    return

# reviewlist = []

c = extract()
transform(c)

# df = pd.DataFrame(reviewlist)
# print(df.head())
# df.to_csv('indeed_reviews/CSV_Files/reviews_indeed.csv', index=False, mode='a', header=False)