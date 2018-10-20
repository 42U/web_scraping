import requests
from time import sleep
from bs4 import BeautifulSoup as soup

make = input("Make: Suzuki, Yamaha, Honda, Kawasaki, etc..\n")
model = input("Model: GSXR, R1, CBR, ZX10R, etc...\n")
sep = "+"
min_price = input("Enter min price\n")
max_price = input("Enter max price\n")
min_disp = input("Enter min displacement\n")
max_disp = input("Enter max displacement\n")
min_miles = input("Enter min miles\n")
max_miles = input("Enter max miles\n")
html_file = open('garage_door', 'r')
bowl_ll = soup(html_file, "html.parser")
locale = []

fd1 = open('locales', 'w')
for locales in bowl_ll.find_all('a', href=True):
    locale.append(locales['href'])
    fd1.write(str(locales))
    fd1.write('\n')

fd1.close()
l_town = []
town = []
i = 1
fd = open('bikes', 'a')
for loco in locale:
    l_town = loco.split('//')
    l_town = l_town[1].split('.')
    town.append(l_town[0])
    locale = l_town[0]
    source = requests.get(f"https://{locale}.craigslist.org/search/mca?min_price={min_price}&max_price={max_price}&auto_make_model={make}'+'{model}&min_engine_displacement_cc={min_disp}&max_engine_displacement_cc={max_disp}&min_auto_year=2002&max_auto_year=2019&min_auto_miles={min_miles}&max_auto_miles={max_miles}&auto_title_status=1&auto_title_status=5")
    plain = source.text
    bowl = soup(plain, "html.parser")
    bikes = []
    for bike in bowl.find_all('li', attrs={'class' : 'result-row'}):
        fd.write("___LISTING____ # ")
        fd.write(str(i))
        fd.write("\n")
        fd.write("__ B R I E F __\n\n")
        quick = bike.find('a').get('href')
        fd.write(" quick link \n")
        fd.write(str(quick))
        fd.write('\n')
        sleep(0.42)
        source2 = requests.get(quick)
        plain2 = source2.text
        desc = soup(plain2, "html.parser")
        b_title = desc.find('span', attrs={'id' : 'titletextonly'}).text.strip()
        b_price = desc.find('span', attrs={'class' : 'price'}).text.strip()
        b_text = desc.find('section', attrs={'id' : 'postingbody'}).text.strip()
        plain2 = desc.find('p', attrs={'class' : 'attrgroup'}).text.strip()
        fd.write(str(plain2))
        fd.write('\n')
        fd.write('\n')
        fd.write(str(b_title))
        print(b_title)
        fd.write('\n')
        fd.write('\n')
        fd.write(str(b_price))
        fd.write('\n')
        fd.write('\n')
        fd.write(str(b_text))
        fd.write('\n')
        fd.write('\n')
        fd.write('_____ END OF BIKE DETAILS _____\n')
        fd.write('\n')
        fd.write('\n')
        fd.write('\n')
        fd.write('\n')
        fd.write('\n')
        fd.write('\n')
        fd.write('\n')
        i += 1

end = 0
