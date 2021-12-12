from bs4 import BeautifulSoup
import requests
#import lxml

url = 'https://www.armblog.net/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
quotes = soup.find_all("h2", class_="post-title entry-title")
titles = ""
for title in quotes:
    titles = titles + title.text + "<br><hr>"
