import requests
from  bs4 import BeautifulSoup
import pandas as pd


base_url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

res = requests.get(base_url)
soup = BeautifulSoup(res.text, "lxml")
title= soup.find_all('a', class_ = 'title')
description= soup.find_all('p', class_ = 'description')


product_names = []



for i in title:
    name = i.text
    product_names.append(name)
   




base_url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

res = requests.get(base_url)
soup = BeautifulSoup(res.text, "lxml")
description= soup.find_all('p', class_ = 'description')


product_description = []

for i in description:
    name = i.text
    product_description.append(name)






base_url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

res = requests.get(base_url)
soup = BeautifulSoup(res.text, "lxml")
description= soup.find_all('h4', class_ = 'float-end price card-title pull-right')


product_prices = []

for i in description:
    name = i.text
    product_prices.append(name)
    




base_url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

res = requests.get(base_url)
soup = BeautifulSoup(res.text, "lxml")
reviews= soup.find_all('p', class_ = 'float-end review-count')


product_reviews = []

for i in reviews:
    name = i.text
    product_reviews.append(name)



compiled_data = pd.DataFrame({"Product_title": product_names, "Product_description": product_description, "Product_price": product_prices, "Product_Reviews": product_reviews})
print(compiled_data)


compiled_data.to_csv('product_data.csv')


