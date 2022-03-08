from pprint import pprint
from bs4 import BeautifulSoup
import requests
from time import sleep, time

# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
# source = requests.get(f'https://www.list.am/category/23/8?n=0&bid=7&mid=0&price1=25000&crc=-1&srt=1', headers=headers)
# print(source.status_code)

try:
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
	page = 1
	baza = {}
	mark = input("Enter mark...")
	marks = {"BMW":7, "Ford":22, "Kia":38,"Lexus": 42, "Mercedes":49}
	min_price = input("Mention min price")
	while not requests.head(f'https://www.list.am/category/23/{page}?n=0&bid={marks[mark]}&mid=0&price1={min_price}&crc=-1', headers=headers).is_redirect:
		source = requests.get(f'https://www.list.am/category/23/{page}?n=0&bid={marks[mark]}&mid=0&price1={min_price}&crc=-1', headers=headers)
		source.raise_for_status()
		print(source.status_code)
		soup = BeautifulSoup(source.text, 'html.parser')
		# ann = soup.find('div', class_='gl').find_next('div', class_='gl').find_all('a')
		ann = soup.find_all('div', class_='gl')[-1].find_all('a')
		# ann = soup.find("div", id_="contentr").findChild('div', class_='gl', recursive=False).find_all('a')
		for an in ann:
			ann_id = an['href'].split('/')[2]
			name = an.find('div', class_='l').text
			if an.find('div', class_='p'):
				price = an.find('div', class_='p').text
			else:
				price="0"
			info = an.find('div',class_='at').text
			place = an.find('div',class_='at').text.split(', ')[0]
			year = an.find('div',class_='at').text.split(', ')[1]
			milage = an.find('div',class_='at').text.split(', ')[2]
			fuel = an.find('div',class_='at').text.split(', ')[3]
			baza[ann_id]= {'page': page, "place": place, 'name': name, 'fuel':fuel, 'year': year, 'price': price, "milage":milage,'info':info}
		page = page +1
		sleep(2)
		continue
	pprint(baza)

except Exception as e:
	print(e)



'''
# comment 01
from selenium import webdriver
import time
#from urllib.request import urlopen, Request
#import requests

url = "https://www.list.am/category/23?bid=11&mid=184"
driver  = webdriver.Chrome(executable_path=r'C:\D\python\parser_aws_tg\chromedriver\chromedriver.exe')

try:
	driver.get(url=url)
	time.sleep(5)
	# driver.refresh()
	# time.sleep(5)
	links = driver.find_elements(by=By.CSS_SELECTOR, value=css_selector)
	for link in links:
		print(link.get_attribute('href'))
except Exception as ex:
	print(ex)
finally:
	driver.close()
	driver.quit()
'''



'''
# comment 02
def get_data(url):
	headers = {
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'n-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,hy;q=0.6',
	'cache-control': 'max-age=0',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
	}

	r = requests.get(url=url, headers = headers)

	with open("rete_l.html", "w", encoding="utf-8") as file:
		file.write(r.text)

def main():
	get_data("https://auto.am/offer/2714669")



if __name__ == '__main__':
	main()
'''
'''
url = "https://www.list.am/item/17404046"
headers = {
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'n-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,hy;q=0.6',
	'cache-control': 'max-age=0',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
	}
src = requests.get(url, headers=headers).text
# print(src.text)
# req = Request(url, headers=headers)
# page = urlopen(req).read()
# # html_bytes = page.read()
# # html = html_bytes.decode("utf-8")
# #r = requests.get(url, headers = headers)
# #r.encoding = 'ISO-8859-5'
# #soup = BeautifulSoup(r.content, 'html.parser')

# print(page.decode(errors='replace'))
with open("rete_l4.html", "w", encoding="utf-8") as file:
		file.write(src)

f = open("rete_l4.html", "r")
print(f.read())
'''