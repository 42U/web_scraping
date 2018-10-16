import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import requests

my_url = 'https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=graphics+cards&ignorear=0&N=-1&isNodeId=1'

uClient = uReq(my_url, None, 10)
page_html = uClient.read()
uClient.close()

