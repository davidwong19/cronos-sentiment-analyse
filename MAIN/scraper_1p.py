import requests
from bs4 import BeautifulSoup
from datetime import datetime
from googletrans import Translator
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm.notebook import tqdm

sia = SentimentIntensityAnalyzer()

df = pd.read_csv(r'C:\Users\Rehts\Documents\Repositories\cronos-sentiment-analyse\MAIN\final_reviews.csv')
id = df['id'].iloc[-1]

def extract():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'}
    #url = f'https://fr.glassdoor.be/Avis/Cronos-Avis-E871033.htm?sort.sortType=RD&sort.ascending=false&filter.iso3Language=fra'
    #url = 'https://nl.glassdoor.be/Reviews/Dynatos-Reviews-E6034680.htm'
    # www.glassdoor.co.uk
    url = 'https://www.glassdoor.co.uk/Reviews/UFINITY-(Belgium)-Reviews-E1156114.htm?filter.iso3Language=eng'
    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):

    divs = soup.find_all('div', class_ = 'gdReview')
    
    for item in divs:
        raw_rating = item.find('span', class_ = 'ratingNumber mr-xsm').text.strip()
        rating = raw_rating.replace('.0', '')
        author_info = item.find('span', class_ = 'authorJobTitle').text.strip()
        
        index = author_info.find(' -')
        date = author_info[0:index]
        date_clean = datetime.strptime(date, '%b %d, %Y').date()
        date_clean_str = date_clean.strftime('%d/%m/%Y')

        pros = item.find('span', {'data-test':'pros'}).text.strip().replace('\r\n', '')
        cons = item.find('span', {'data-test':'cons'}).text.strip().replace('\r\n', '')
        opinion = pros + ', ' + cons

        translator = Translator()
        opinion_en = translator.translate(opinion).text

        new_id = int(id) + 1

        score = sia.polarity_scores(opinion_en)['compound']
        if score >= 0.05 : sentiment = 'positive'
        elif score <= - 0.05 : sentiment = 'negative'
        else : sentiment = 'neutral'

        review = {
            '\n''id': new_id,
            'company': 'Ufinity', # CHANGE THIS
            'opinion': opinion_en,
            'date': date_clean_str,
            'rating': rating,
            'source': 'glassdoor', 
            'score': score,
            'sentiment': sentiment 
        }
        reviewlist.append(review)
    return

reviewlist = []

c = extract()
transform(c)

df = pd.DataFrame(reviewlist)
print(df.head())
df.to_csv(r'C:\Users\Rehts\Documents\Repositories\cronos-sentiment-analyse\MAIN\final_reviews.csv', index=False, mode='a', header=False)