# web_scraping
This is a WebScraper that currently only scrapes Craigslist for motorcycles. *(I made this to help me sift through all the bookmarks I had when looking for a motorcycle for myself)

the system you run this on should have python3 AND python3-bs4 installed already.
there are multiple ways to install these libraries the following is most common for unix:

sudo apt install python3 python3-bs4

![alt text](https://github.com/42U/web_scraping/blob/master/resources/clist_42u3.png)

You can download the files into a directory on any unix based machine running python3,
run the following command using a terminal, from the directory containing all the files from this repo:

![alt text](https://github.com/42U/web_scraping/blob/master/resources/clist_42u.png)

python3 clist_motorcycle_scraper.py

![alt text](https://github.com/42U/web_scraping/blob/master/resources/clist_42u2.png)

you do not have to fill out each field but you will get a lot off results and it will take a long time. you would be
essentially searching all of craigslist for every motorcycle listed.

after it finds all the motorcycles listed, it will output the description and a link to the posting, in a file called bikes.

