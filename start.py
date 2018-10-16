import re
import requests
from bs4 import BeautifulSoup as soup

website = 'https://www.craigslist.org/about/sites'
source = requests.get(website)
page_html = source.text
page = soup(page_html, "html.parser")

print(page)
