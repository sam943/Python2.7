# Web Scraping with BeautifulSoup
# pip install bs4 and lxml
# bs4 - beautifulsoup4
# lxml - xml parser used for web scraping

import urllib
from bs4 import BeautifulSoup
url = "http://somewebsite/html_page.html"

# open the site and download the html into the variable
html_data = urllib.urlopen(url).read()

#parse the data using BeautifulSoup
soup = BeautifulSoup(html_data,"lxml")

#find the specific tags needed

sections = soup.find_all
