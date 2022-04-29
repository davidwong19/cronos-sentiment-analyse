import requests
from bs4 import BeautifulSoup
from datetime import datetime
from googletrans import Translator
import pandas as pd

def extract():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'}
    #url = f'https://fr.glassdoor.be/Avis/Cronos-Avis-E871033.htm?sort.sortType=RD&sort.ascending=false&filter.iso3Language=fra'
    #url = f'https://nl.glassdoor.be/Reviews/Arxus-Reviews-E2467100.htm'
    #url = f'https://www.glassdoor.co.uk/Reviews/Big-Industries-Reviews-E2862189.htm?filter.iso3Language=eng'
    #url = f'https://www.glassdoor.co.uk/Reviews/Biztory-Reviews-E2541509.htm?filter.iso3Language=eng'
    #url = f'https://nl.glassdoor.be/Reviews/Codesense-Reviews-E6218788.htm'
    #url = f'https://nl.glassdoor.be/Reviews/Cronos-International-Reviews-E1321590.htm?filter.iso3Language=eng'
    #url = f'https://www.glassdoor.co.uk/Reviews/Cronos-International-Reviews-E1321590.htm?filter.iso3Language=eng'
    #url = 'https://www.glassdoor.co.uk/Reviews/Crosspoint-Solutions-Reviews-E812597.htm?filter.iso3Language=eng'
    #url = 'https://nl.glassdoor.be/Reviews/Dynatos-Reviews-E6034680.htm'
    url = 'https://www.glassdoor.co.uk/Reviews/HeadCount-Reviews-E1191477.htm?filter.iso3Language=eng'
    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):

    divs = soup.find_all('div', class_ = 'gdReview')
    
    for item in divs:
        rating = item.find('span', class_ = 'ratingNumber mr-xsm').text.strip()
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
        
        review = {
            'rating': rating,
            'opinion': opinion_en,
            'date': date_clean_str,
            'source': 'glassdoor',
            'company': 'HeadCount' # CHANGE THIS
        }
        reviewlist.append(review)
    return

reviewlist = []

c = extract()
transform(c)

df = pd.DataFrame(reviewlist)
print(df.head())
df.to_csv('./CSV_Files/reviews_gd_companies.csv', index=False, mode='a', header=False)
#df.to_csv('./CSV_Files/reviews_gd_CI.csv', index=False, mode='a', header=False)