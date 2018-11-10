from bs4 import BeautifulSoup
from selenium import webdriver
import urllib
import urllib.request

def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

i=1
soup = make_soup('https://www.imdb.com/chart/top?ref_=nv_mv_250')

for img in soup.find_all("img"):
    image = img.get('src')

    filename = str(i)  # set the name of files
    i=i+1

    imagefile = open(filename + ".jpeg", 'wb')
    imagefile.write(urllib.request.urlopen(image).read())
    imagefile.close()
