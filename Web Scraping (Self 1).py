# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 08:49:30 2020

@author: admin
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.worldometers.info/world-population/population-by-country/'
requests.get(url)
page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')
print(soup)

table_data = soup.find('table', class_ = 'table table-striped table-bordered')

headers = []
for i in table_data.find_all('th'):
    title = i.text
    headers.append(title)

data = pd.DataFrame(columns = headers)
print(data)

for j in table_data.find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [tr.text for tr in row_data]
        length = len(data)
        data.loc[length] = row
        
print (data)

