import requests
from bs4 import BeautifulSoup

def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'}
    url = f'https://nl.glassdoor.be/Reviews/Cronos-Reviews-E871033_{page}.htm?filter.iso3Language=nld'
    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    pros_list = []
    cons_list = []
    final_list = []
    divs = soup.find_all('div', class_ = 'gdReview')
    for item in divs:
        author_info = item.find('span', class_ = 'authorJobTitle').text.strip()
        for pros in item.find_all('span', {'data-test':'pros'}):
            pros_list.append(pros.get_text())
        for cons in item.find_all('span', {'data-test':'cons'}):
            cons_list.append(cons.get_text())

    length_list = len(cons_list)
    i = 0
    
    while i < length_list:
      final_list.append(pros_list[i] + ', ' + cons_list[i])
      i += 1
    print(final_list[0])

c = extract('P1')
transform(c)