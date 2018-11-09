from bs4 import BeautifulSoup
from selenium import webdriver

# set the path of chromeDriver
driver = webdriver.Chrome(executable_path=r'C:\Users\NastyPan\Downloads\chromeDriver\chromedriver.exe')

url = 'https://www.slickcharts.com/sp500'

driver.get(url)


soup = BeautifulSoup(driver.page_source, 'lxml')

table = soup.find_all('td')[1::6]  # extract the companies names from tags

for td in table:
    print(td.text.strip())