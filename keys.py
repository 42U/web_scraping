import requests
from time import sleep
from bs4 import BeautifulSoup as soup
# adding selenium because i'm only getting partial results
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# direct path to the chromedriver for selenium
dlo = '/nfs/2018/i/issmith/CH_DR/chromedriver-Darwin'

# this doesn't work idk why
class ezClap(object):
    def __init__(self, locale, make, model, min_price, max_price, min_disp, max_disp, min_miles, max_miles, url):
        self.locale = locale
        self.make = make
        self.model = model
        self.min_price = min_price
        self.max_price = max_price
        self.min_disp = min_disp
        self.max_disp = max_disp
        self.min_miles = min_miles
        self.max_miles = max_miles
        self.url = url
        self.driver = webdriver.Chrome(dlo)
        self.delay = 4
    
    def load_craigslist_url(self):
        self.driver.get(self.url)
        try:
            wait = WebDriverWait(self.driver, self.delay)
            wait.until(EC.presence_of_element_located((By.ID, "searchform")))
            print('page is ready!')
        except TimeoutException:
            print('loading failed?')
    
    def extract_post_titles(self):
        all_post = self.driver.find_elements_by_class_name("result-row")
        post_title_list = []
        for post in all_posts:
            print(post.text)
            post_title_list.append(post.text)
        return post_title_list

    def extract_post_urls(self):
        url_list = []
        html_page = requests.get(self.url)
        plain = html_page.text
        bowl_ft = (plain, "html.parser")
        for link in bowl_ft.findAll('a', attrs={'class' : 'result-title hdrlnk'}):
            print(link['href'])
            url_list.append(link['href'])
        return url_list

    def extract_post_information(self):
        all_posts = self.driver.find_elements_by_class_name("result-row")
        dates = []
        titles = []
        prices = []
        for post in all_posts:
            print(post.text)
            title = post.text.split("$")
            if title[0] == '':
                title[0] = title[1]
            else:
                title = title[0]

            title = title.split('\n')
            price = title[0]
            title = title[-1]

            title = title.split(' ')
            
            month = title[0]
            day = title[1]
            title = ' '.join(title[2:])
            date = month + ' ' + day

            print("Price: " + price)
            print("Title: " + title)
            print("Date: " + date)

            titles.append(title)
            prices.append(price)
            dates.append(date)

    def quit(self):
        self.driver.close()

    
# input configuration file (kind off)
html_file = open("garage_door", 'r')

# locale links are extracted here
bowl_ll = soup(html_file, "html.parser")
locale = []
for locales in bowl_ll.find_all('a', href=True):
	locale.append(locales['href'])

fd1 = open('locales', 'a')
for line in locale:
	fd1.write(line)
	fd1.write('\n')

# had to finagle the all_links string to extract a list of the locales (ezclap)
l_town = []
town = []
for loco in locale:
    town = loco.split("//")
    town = town[1].split(".")
    l_town.append(town[0])
    fd1.write(town[0])
    fd1.write('\n')

fd1.close()
# variables for the url search
locale = l_town[int(input("Number of the locale you want to search\n"))]
make = input("Make: Suzuki, Yamaha, Honda, Kawasaki, etc..\n")
model = input("Model: GSXR, R1, CBR, ZX10R, etc...\n")
sep = "+"
min_price = input("Enter min price\n")
max_price = input("Enter max price\n")
min_disp = input("Enter min displacement\n")
max_disp = input("Enter max displacement\n")
min_miles = input("Enter min miles\n")
max_miles = input("Enter max miles\n")

# website template link
url = f"https://{locale}.craigslist.org/search/mca?min_price={min_price}&max_price={max_price}&auto_make_model={make}'+'{model}&min_engine_displacement_cc={min_disp}&max_engine_displacement_cc={max_disp}&min_auto_year=2002&max_auto_year=2019&min_auto_miles={min_miles}&max_auto_miles={max_miles}&auto_title_status=1&auto_title_status=5"

fd = open('bikes', 'a')

# how to call ezClap
scrape = ezClap(locale, make, model, min_price, max_price, min_disp, max_disp, min_miles, max_miles, url)
scrape.load_craigslist_url()
titles, prices, dates = scrape.extract_post_information()
#scrape.extract_post_urls()
#scrape.quit()

fd.close()
print(titles)
