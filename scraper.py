import json
import requests
import lxml
from bs4 import BeautifulSoup

url = 'https://www.list.am/category/23?n=0&bid=55&mid=3462&price1=&price2=&crc=-1&_a2_1=&_a2_2=&_a27=0&_a1_1=&_a1_2=&_a15=0&_a28_1=&_a28_2=&_a13=0&_a23=0&_a43=0&_a22=0&_a16=0&_a17=0'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all()

print(quotes)
