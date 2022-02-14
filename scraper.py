from bs4 import BeautifulSoup
import requests
import lxml
import boto3
from database_query import get_names
import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('sas_products')
resp = table.scan()

url = 'https://www.sas.am/food/search/?SORTBY=RELEVANSE&q=karag'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
quotes = soup.find_all("div", class_="product__name hidden-sm")
prices = soup.find_all("span", class_="price__text")
titles = ""
exec_date = datetime.datetime.now()
idx = 0
names =  get_names()
for title in quotes:
    titles =titles + f"{str(idx+1)}) " + title.text + " >> " + prices[idx].text + "<br><hr>" # puts information to web page
    if title.text not in names:  # adds date to databese
        table.put_item(Item= {'name': f'{title.text}','price':  f'{prices[idx].text}', 'date':f'{exec_date.strftime("%d %B %Y")}'})
    idx=idx+1
