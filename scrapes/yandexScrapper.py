import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from secrets import geckodriverPath, firefoxProfile
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
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

def yandexCribScanner(url):
    parser.get(url)
    CaptchaPass(parser)
    soup = BeautifulSoup(parser.page_source, "html.parser")

    def getPrice():
        priceBox = soup.find_all('div', class_='OfferCardSummary__description--2q8jE OfferCardSummaryInfo__root--2AF-z')
        price = priceBox[0].find('span', class_='OfferCardSummaryInfo__price--3WinQ OfferCardSummaryInfo__priceWithLeftMargin--dZLTe')
        price = price.text
        return price

    def getMainStats():
        statsBox = soup.find_all('div', class_='OfferCard__content--3LFIj')
        stats = statsBox[0].find_all('div',class_='OfferCardHighlights__feature--3FbLx')
        mainStatsDct = {}
        for elem in stats:
            statValue = elem.find('div', class_='OfferCardHighlights__featureValue--2wfJ7')
            statName = elem.find('div', class_='OfferCardHighlights__featureLabel--1FzBQ')
            statName = statName.text
            statValue = statValue.text
            value = statValue.replace('\xa0', ' ')
            name = statName.replace('\xa0', ' ')
            mainStatsDct[name] = value
        return mainStatsDct

    def getDescription():
        descBox = soup.find_all('div', class_='OfferCard__textDescription--36D2f')
        description = descBox[0].find('p', class_='OfferCardTextDescription__text--3na1F')
        description = description.text
        desc = description.replace('\xa0', ' ')
        return desc

    def getOptionalStats():
        buttons = parser.find_elements(By.CLASS_NAME, value='Link.Link_js_inited.Link_size_unset.Link_theme_islands.OfferCardExpandableData__expandControl--2Jn9c')
        for button in buttons:
            button.click()
        # button_element = WebDriverWait(parser, 10).until(
        #     EC.presence_of_element_located((By.CLASS_NAME,
        #                                     "Link.Link_js_inited.Link_size_unset.Link_theme_islands.OfferCardExpandableData__expandControl--2Jn9c"))
        # )
        # button_element.click()
        optionsBox = soup.find_all('div', class_='OfferCardDetailsFeatures__container--2URxF')
        print((len(optionsBox)))
        frstOptions = optionsBox[0].find_all('a', class_='Link Link_js_inited Link_size_l Link_theme_islands Link_view_text OfferCardDetailsFeatures__feature--3YXhs OfferCardFeature__root--1uCzg')
        scndOptions = optionsBox[0].find_all('div', class_='OfferCardDetailsFeatures__feature--3YXhs OfferCardFeature__root--1uCzg')
        lst = frstOptions + scndOptions
        optionsLst = []
        for elem in lst:
            option = elem.find('div', class_='OfferCardFeature__text--3NIwE')
            option = option.text
            option = option.replace('\xa0', ' ')
            optionsLst.append(option)
        print(optionsLst)
    getOptionalStats()

yandexCribScanner('https://realty.ya.ru/offer/7126703710585570957/#location')