from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup as soup
import urllib.request

class craigScraper(object):
    def __init__(self, locale, miles, m_price, info, disp_min, disp_max):
        self.locale = locale
        self.miles = miles
        self.m_price = m_price
        self.info = info
        self.disp_min = disp_min
        self.disp_max = disp_max

        self.url = f"https://{locale}.craigslist.org/search/mca"
#?min_price=0&max_price={m_price}&min_engine_displacement_cc={dis_min}&max_engine_displacement_cc={disp_max}&min_auto_year=2002&max_auto_year=2019&auto_title_status=1&auto_title_status=5"
    def test(self):
        print(self.url)

locale = "auburn"
miles = "0"
m_price = "4000"
info = ""
disp_min = "748"
disp_max = "1002"

scrape = craigScraper(locale, miles, m_price, info, disp_min, disp_max)
scrape.test()
