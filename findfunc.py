import requests
from bs4 import BeautifulSoup

base_url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

response = requests.get(base_url)
print(response)

soup = BeautifulSoup(response.text, "lxml")
price = soup.find("h4" ,{"class" :"float-end price card-title pull-right"})
print(price.string)

prices= soup.find_all("h4", {"class" : "float-end price card-title pull-right"})
print(prices[3])
print(len(prices))

for i in prices:
    print(i.text)