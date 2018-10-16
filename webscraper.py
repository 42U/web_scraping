import re
import requests
from bs4 import BeautifulSoup as soup

# the website i am scraping
url = "https://www.craigslist.org/about/sites#US"

# gets the website requested and downloads it
source = requests.get(url)

# pointer to the file just created
plain_text = source.text

# parses the file in to easy to read lines
bowl = soup(plain_text, "html.parser")

# the beautifulsoup4 (bs4) library has features (functions)
test = bowl.body.article.section.findAll("div", {"class" : "box"})

# print a value of a tag
state_link = bowl.body.article.section.ul.a['href']

print(len(test))
#print(bowl.h1)
