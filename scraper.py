from bs4 import BeautifulSoup
import requests
import lxml

url = 'https://www.sas.am/food/search/?SORTBY=RELEVANSE&q=hac'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
quotes = soup.find_all("div", class_="product__name hidden-sm")
prices = soup.find_all("span", class_="price__text")
titles = ""
idx = 0
for title in quotes:
    titles = titles + title.text + " >> " + prices[idx].text + "<br><hr>"
    idx=idx+1
