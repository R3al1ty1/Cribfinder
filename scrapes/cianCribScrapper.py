import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from secrets import geckodriverPath, firefoxProfile
import time

geckodriverLocation = f"{geckodriverPath}" # Location of geckodriver
firefoxProfile = f"{firefoxProfile}" # Selected Firefox profile

service = Service(geckodriverLocation) # Setting up location

options = Options()
options.add_argument('-headless')
options.set_preference('profile', firefoxProfile) # Setting up profile
parser = webdriver.Firefox(service=service, options=options)  # Creating webdriver

def CaptchaPass(parser):
    try:
        button = parser.find_element(by=By.CLASS_NAME, value="CheckboxCaptcha-Button")
        button.click()
        time.sleep(1)
    except:
        return

def cianCribScanner(url):
    parser.get(url)
    CaptchaPass(parser)
    soup = BeautifulSoup(parser.page_source, "html.parser")

    def containerParser():
        mainContainer = soup.find_all('div', class_='a10a3f92e9--item--Jp5Qv')
        statsDct = {}
        for elem in mainContainer:
            elemName = elem.find('span', class_='a10a3f92e9--color_gray60_100--MlpSF a10a3f92e9--lineHeight_4u--fix4Q a10a3f92e9--fontWeight_normal--P9Ylg a10a3f92e9--fontSize_12px--EdtE5 a10a3f92e9--display_block--pDAEx a10a3f92e9--text--g9xAG a10a3f92e9--text_letterSpacing__0--mdnqq')
            elemValue = elem.find('span', class_='a10a3f92e9--color_black_100--kPHhJ a10a3f92e9--lineHeight_6u--A1GMI a10a3f92e9--fontWeight_bold--ePDnv a10a3f92e9--fontSize_16px--RB9YW a10a3f92e9--display_block--pDAEx a10a3f92e9--text--g9xAG')
            elemName = elemName.text
            elemValue = elemValue.text
            name = elemName.replace('\xa0', ' ')
            value = elemValue.replace('\xa0', ' ')
            statsDct[name] = value
        return statsDct
    def getPrice():
        priceBox = soup.find_all('div', class_='a10a3f92e9--amount--ON6i1')
        price = priceBox[0].find('span', class_='a10a3f92e9--color_black_100--kPHhJ a10a3f92e9--lineHeight_9u--qr919 a10a3f92e9--fontWeight_bold--ePDnv a10a3f92e9--fontSize_28px--xlUV0 a10a3f92e9--display_block--pDAEx a10a3f92e9--text--g9xAG')
        price = price.text
        return price

    def getDescription():
        descBox = soup.find_all('div', class_='a10a3f92e9--description--CGQRW')
        desc = descBox[0].find('span', class_='a10a3f92e9--color_black_100--kPHhJ a10a3f92e9--lineHeight_6u--A1GMI a10a3f92e9--fontWeight_normal--P9Ylg a10a3f92e9--fontSize_16px--RB9YW a10a3f92e9--display_block--pDAEx a10a3f92e9--text--g9xAG a10a3f92e9--text_letterSpacing__0--mdnqq a10a3f92e9--text_whiteSpace__pre-wrap--scZwb')
        desc = desc.text
        return desc

    def getResComplexLink():
        complexHeader = soup.find_all('div', class_='a10a3f92e9--container--mTzLi')
        complexLink = complexHeader[0].find('a', class_='a10a3f92e9--link--A5SdC')
        return complexLink.get('href')
    def getHouseInfo():
        mainBox = soup.find_all('div', class_='a10a3f92e9--item--qJhdR')
        infoDct = {}
        for elem in mainBox:
            houseInfoName = elem.find('p', class_='a10a3f92e9--color_gray60_100--MlpSF a10a3f92e9--lineHeight_22px--bnKK9 a10a3f92e9--fontWeight_normal--P9Ylg a10a3f92e9--fontSize_16px--RB9YW a10a3f92e9--display_block--pDAEx a10a3f92e9--text--g9xAG a10a3f92e9--text_letterSpacing__normal--xbqP6')
            houseInfoValue = elem.find('p', class_='a10a3f92e9--color_black_100--kPHhJ a10a3f92e9--lineHeight_22px--bnKK9 a10a3f92e9--fontWeight_normal--P9Ylg a10a3f92e9--fontSize_16px--RB9YW a10a3f92e9--display_block--pDAEx a10a3f92e9--text--g9xAG a10a3f92e9--text_letterSpacing__normal--xbqP6')
            houseInfoName = houseInfoName.text
            houseInfoValue = houseInfoValue.text
            houseInfoValue = houseInfoValue.replace('\xa0', ' ')
            houseInfoName = houseInfoName.replace('\xa0', ' ')
            infoDct[houseInfoName] = houseInfoValue
        return infoDct

    def getAdress():
        addressBox = soup.find_all('div', class_='a10a3f92e9--address-line--GRDTb')
        addressComponents = addressBox[0].find_all('a', class_='a10a3f92e9--address--SMU25')
        res = ''
        for elem in addressComponents:
            res += elem.text + ' '
        return res
    return containerParser(), getPrice(), getDescription(), getResComplexLink(), getHouseInfo(), getAdress()

print(cianCribScanner('https://solnechnogorsk.cian.ru/sale/flat/265421703/'))