import requests
from bs4 import BeautifulSoup as soup

# this doesn't work idk why
def to_file(fildes, info):
    filedes.write(info)
    filedes.write('\n')

# input configuration file (kind off)
html_file = open("garage_door", 'r')

# output files where the results go
fd = open("garage", "a")
fd1 = open("locales", "w")
fd2 = open("searches", "a")
fd3 = open("short_list", 'w')

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

quick_link = []
save_all = []
save = []
fd2.write(url)
cycles = []
random = []
i = 1

# this should be put in to a for loop so that it can go through all areas
source = requests.get(url)
plain = source.text

# this brings back the search in a locale
bowl = soup(plain, "html.parser")

# this will copy all the data i want from the search
save_all = bowl.find_all('li', attrs={'class' : 'result-row'})

# this separates each result into a pointer
for bike in bowl.find_all('li', attrs={'class' : 'result-row'}):
    fd.write("___LISTING____ # ")
    fd.write(i)
    fd.write("\n")
    fd.write(bike)
    fd.write('\n')
    fd.write("__ B R I E F __\n")
# this goes in to the bike description page
    quick = bike.find('a').get('href')
    fd.write(" quick link \n")
    fd.write(quick)
    fd.write('\n')
    source2 = requests.get(quick)
    plain2 = source2.text
    desc = soup(plain2, "html.parser")
# ref = save[0].find('a', href=True)
# ref.get('href')
    b_title = desc.find('span', attrs={'id' : 'titletextonly'}).text.strip()
    b_price = desc.find('span', attrs={'class' : 'price'}).text.strip()
    b_text = desc.find('section', attrs={'id' : 'postingbody'}).text.strip()
    plain2 = desc.find('p', attrs={'class' : 'attrgroup'}).text.strip()
    fd.write(str(plain2))
    fd.write('\n')
    fd.write('\n')
    fd.write(b_title)
    print(b_title)
    fd.write('\n')
    fd.write('\n')
    fd.write(b_price)
    fd.write('\n')
    fd.write('\n')
    fd.write(b_text)
    fd.write('\n')
    fd.write('\n')
    fd.write('_____ END OF BIKE DETAILS _____\n')
    fd.write('\n')
    fd.write('\n')
    fd.write('\n')
    fd.write('\n')
    fd.write('\n')
    fd.write('\n')
    i += 1

end_of_program = []
