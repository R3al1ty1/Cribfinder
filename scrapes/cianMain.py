import requests
from bs4 import BeautifulSoup

test = 'https://www.cian.ru/rent/flat/146997922/'

def cribScanner(cnt):
    for i in range(146997922, cnt):
        url = f'https://www.cian.ru/rent/flat/{i}/'
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            print(soup)
            priceBox = soup.find('div', class_='a10a3f92e9--amount--ON6i1')
            print(priceBox)
            #price = priceBox[0].find_all('span', class_='a10a3f92e9--color_black_100--kPHhJ a10a3f92e9--lineHeight_9u--qr919 a10a3f92e9--fontWeight_bold--ePDnv a10a3f92e9--fontSize_28px--xlUV0 a10a3f92e9--display_block--pDAEx a10a3f92e9--text--g9xAG')
            #print(price)

cribScanner(146997923)