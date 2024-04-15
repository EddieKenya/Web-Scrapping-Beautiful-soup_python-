import requests
from bs4 import BeautifulSoup
import pandas as pd


base_url = "https://www.skysports.com/premier-league-table"

r = requests.get(base_url)
soup = BeautifulSoup(r.text, "lxml")
th = soup.find("table", class_ = "standing-table__table")
heading = th.find_all('th')
rows = th.find_all("tr", class_="standing-table__row")
# print (heading)
print(rows)

table_headings = []

for i  in  heading:
    head = i.text
    print(head)
    table_headings.append(head)

print(table_headings)

table_data =[]
for j in  rows[1:]:
    row=  j.find_all('td')
    data = [td.text for td in row ]
    l = len(pd)
    pd.loc[l] = row
    table_data.append(data)

print(table_data)
premier_table = pd.DataFrame()