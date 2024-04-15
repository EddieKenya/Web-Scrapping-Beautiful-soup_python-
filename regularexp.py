import requests
from bs4 import BeautifulSoup
import re

base_url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

doc = requests.get(base_url)
print(doc)
soup = BeautifulSoup(doc.text, "lxml")
# title = (soup.find_all('a', {"class" : "title"}))
title = (soup.find_all(string=  re.compile("Galaxy Tab")))
print (title)