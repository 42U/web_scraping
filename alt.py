import requests
from time import sleep
from bs4 import BeautifulSoup as soup
   
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
locale = l_town[int(input("Number of the locale you want to search"))]
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

save_all = []
i = 1

# this should be put in to a for loop so that it can go through all areas
source = requests.get(url)
plain = source.text

# this brings back the search in a locale
bowl = soup(plain, "html.parser")

# this will copy all the data i want from the search
save_all = bowl.find_all('li', attrs={'class' : 'result-row'})

fd = open('bikes', 'a')

fd.close()

# this separates each result into a pointer
for bike in bowl.find_all('li', attrs={'class' : 'result-row'}):
    fd.write("___LISTING____ # ")
    fd.write(str(i))
    fd.write("\n")
    fd.write(str(bike))
    fd.write('\n')
    fd.write('\n')
    fd.write("__ B R I E F __\n\n")
    quick = bike.find('a').get('href')
    fd.write(" quick link \n")
    fd.write(str(quick))
    fd.write('\n')
    sleep(3.42)
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
    fd.close()
    i += 1

