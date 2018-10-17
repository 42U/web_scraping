import re
import requests
from bs4 import BeautifulSoup as soup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# creating class for variables
class EZclapper(object):
    def __init__(self, locale, make, sep, model, min_price, max_price, min_disp, max_disp, min_miles, max_miles):
        self.locale = locale
        self.make = make
        self.sep = sep
        self.model = model
        self.min_price = min_price
        self.max_price = max_price
        self.min_disp = min_disp
        self.max_disp = max_disp
        self.min_miles = min_miles
        self.max_miles = max_miles
        self.url = f'https://{locale}.craigslist.org/search/mdc/mca?auto_make_model={model}&min_engine_displacement_cc={min_disp}&max_engine_displacement_cc={max_disp}&min_auto_year=2002&max_auto_year=2019&min_auto_miles={min_miles}&max_auto_miles={max_miles}'
        def test(self):
            print(self.locale)

# the website i am scraping
#url = "https://www.craigslist.org/about/sites#US"

# open html file for parsing
# garage_door is the config file
# garage is where the scraped content goes
html_file = open("garage_door")
fd = open("garage", "a")

# gets the website requested and downloads it
#source = requests.get(url)

# pointer to the file just created
#plain_text = source.text

# parses the file in to easy to read lines
if html_file:
    bowl = soup(html_file, "html.parser")
else:
    bowl = soup(plain_text, "html.parser")

# the beautifulsoup4 (bs4) library has features (functions)
#test = bowl.body.article.section

# print a value of a tag
#state_link = bowl.body.article.section.ul.a['href']

#print()
#print(bowl.h1)

# function 'findAll' to search for things
#test = str(bowl.findAll('li'))

#   this should list all the links from the list
all_links = []
for a in bowl.find_all('a', href=True):
    all_links.append(a['href'])
#    print(a['href'])
fd1 = open("short_list", "a")
for link in all_links:
    fd1.write(link)
    fd1.write('\n')
fd1.closed

locale = link
make = "suzuki"
model = "gsxr"
sep = "+"
min_price = "0"
max_price = "6500"
min_disp = "748"
max_disp = "1002"
min_miles = "500"
max_miles = "16666"

def init():

# this is the current params for the search. will add variables
    params = "search/mca?min_price={min_price}&max_price={max_price}&min_engine_displacement_cc={min_disp}&max_engine_displacement_cc={max_disp}&min_auto_year=2002&max_auto_year=2019&auto_title_status=1&auto_title_status=5"
    url_s = []
    bike_s = []
    locale_f = []
    info = []
    price = 0
    i = 0
    for x in link:
        i += 1
        url_s.append(x+params)
        src = requests.get(x+params)
        plu = src.text
        bike_g = soup(plu, "html.parser")
        fd.write("__LISTING__\n")
        fd.write(i, "\n")
        price = bike_g.

        fd.write("Price: ", price)
        fd.write(bike_g.findAll('li', {"class" : "result-row"}))
        bike_s = (bike_g.findAll('li', {"class" : "result-row"})
            #need to finish adding the path to the tag that has
            # price and web
    print(bike_g)

