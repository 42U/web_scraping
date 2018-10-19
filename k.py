import requests
from bs4 import BeautifulSoup as soup

# input configuration file (kind off)
html_file = open("garage_door", 'r')

# output files where the results go
fd = open("garage", "a")
fd1 = open("locales", "w+")
fd2 = open("searches", "a")

# locale links are extracted here
bowl_ll = soup(html_file, "html.parser")
locale = []
for locales in bowl_ll.find_all('a', href=True):
	locale.append(locales['href'])
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

# variables for the url search
locale = l_town[1]
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

save = []
fd2.write(url)
source = requests.get(url)
plain = source.text
bowl = soup(plain, "html.parser")
fd.write("___LISTING____ # ")
fd.write("1")
fd.write("\n")
fd.write("something\n")
print()
