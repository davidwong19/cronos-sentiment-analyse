from email import header
from click import command
import requests
from bs4 import BeautifulSoup
from sympy import div

def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'}
    url = f'https://nl.glassdoor.be/Reviews/Cronos-Reviews-E871033_{page}.htm?filter.iso3Language=nld'
    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_ = 'gdReview')
    for item in divs:
        author_info = item.find('span', class_ = 'authorJobTitle').text.strip()
        pros = item.find('p', class_ = 'mt-0 mb-0 pb v2__EIReviewDetailsV2__bodyColor v2__EIReviewDetailsV2__lineHeightLarge v2__EIReviewDetailsV2__isExpanded').text.strip()
        cons = item.find('p', class_ = 'mt-0 mb-0 pb v2__EIReviewDetailsV2__bodyColor v2__EIReviewDetailsV2__lineHeightLarge v2__EIReviewDetailsV2__isExpanded')[0].text.strip()
        print(cons)

c = extract('P1')
transform(c)