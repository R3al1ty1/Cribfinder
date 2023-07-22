import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

def yandexCaptchaPass(parser):
    try:
        button = parser.find_element(by=By.CLASS_NAME, value="CheckboxCaptcha-Button")
        button.click()
        time.sleep(1)
    except:
        return


# options = webdriver.FirefoxOptions()
# #options.add_argument('headless')
# browser = webdriver.Firefox(options=options)
# browser.get('https://solnechnogorsk.cian.ru/sale/flat/265421703/')
# test = browser.find_element('')
# print(test)
# test = 'https://www.cian.ru/rent/flat/146997922/'

def cribScanner(url):
    parser.get(url)
    yandexCaptchaPass(parser)
    soup = BeautifulSoup(parser.page_source, "html.parser")

    def containerParser():
        mainContainer = soup.find_all('div', class_='a10a3f92e9--item--Jp5Qv')
        tempDct = {}
        for elem in mainContainer:
            elemName = elem.find('span', class_='a10a3f92e9--color_gray60_100--MlpSF a10a3f92e9--lineHeight_4u--fix4Q a10a3f92e9--fontWeight_normal--P9Ylg a10a3f92e9--fontSize_12px--EdtE5 a10a3f92e9--display_block--pDAEx a10a3f92e9--text--g9xAG a10a3f92e9--text_letterSpacing__0--mdnqq')
            elemValue = elem.find('span', class_='a10a3f92e9--color_black_100--kPHhJ a10a3f92e9--lineHeight_6u--A1GMI a10a3f92e9--fontWeight_bold--ePDnv a10a3f92e9--fontSize_16px--RB9YW a10a3f92e9--display_block--pDAEx a10a3f92e9--text--g9xAG')
            elemName = elemName.text
            elemValue = elemValue.text
            if "\xa0" in elemValue:
                elemValue.replace("\xa0", ' ')
            tempDct[elemName] = elemValue
        print(tempDct)
    def getPrice():
        priceBox = soup.find_all('div', class_='a10a3f92e9--amount--ON6i1')
        price = priceBox[0].find('span', class_='a10a3f92e9--color_black_100--kPHhJ a10a3f92e9--lineHeight_9u--qr919 a10a3f92e9--fontWeight_bold--ePDnv a10a3f92e9--fontSize_28px--xlUV0 a10a3f92e9--display_block--pDAEx a10a3f92e9--text--g9xAG')
        price = price.text
        return price

    def getSpace():
        spaceBox = soup.find_all('div', class_='a10a3f92e9--item--Jp5Qv')
        space = spaceBox[0].find('span',class_='a10a3f92e9--color_black_100--kPHhJ a10a3f92e9--lineHeight_6u--A1GMI a10a3f92e9--fontWeight_bold--ePDnv a10a3f92e9--fontSize_16px--RB9YW a10a3f92e9--display_block--pDAEx a10a3f92e9--text--g9xAG')
        space = space.text
        return space

    def getFloor():
        floorBox = soup.find_all('div', class_='a10a3f92e9--item--Jp5Qv')
        floor = floorBox[1].find('span',class_='a10a3f92e9--color_black_100--kPHhJ a10a3f92e9--lineHeight_6u--A1GMI a10a3f92e9--fontWeight_bold--ePDnv a10a3f92e9--fontSize_16px--RB9YW a10a3f92e9--display_block--pDAEx a10a3f92e9--text--g9xAG')
        floor = floor.text
        return floor

    def getYear():
        yearBox = soup.find_all('div', class_='a10a3f92e9--item--Jp5Qv')
        year = yearBox[2].find('span',class_='a10a3f92e9--color_black_100--kPHhJ a10a3f92e9--lineHeight_6u--A1GMI a10a3f92e9--fontWeight_bold--ePDnv a10a3f92e9--fontSize_16px--RB9YW a10a3f92e9--display_block--pDAEx a10a3f92e9--text--g9xAG')
        year = year.text
        print(year)
    containerParser()

cribScanner('https://solnechnogorsk.cian.ru/sale/flat/265421703/')