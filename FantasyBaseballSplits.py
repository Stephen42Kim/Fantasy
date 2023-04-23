# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 17:12:35 2023

@author: Stephen
"""

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# Fetch web page
url = "https://www.fangraphs.com/players/aaron-judge/15640/splits?position=OF&season=2023"
page = requests.get(url)

print(page.text)

soup = bs(page.text, 'html.parser')
table = soup.find(id = 'plato')
print(table)

tab_text = table.decode_contents().split('--')[1].strip()

tab_soup = bs(tab_text, 'html.parser')

print(tab_soup.prettify())





















# fetching web page
url = "https://www.baseball-reference.com/leagues/majors/2022-batting-pitching.shtml"
page = requests.get(url)

# extracting table from html
soup = bs(page.content,"html.parser")
table = soup.find(id = 'all_players_batting_pitching')
tab_text = table.decode_contents().split('--')[1].strip()

tab_soup = bs(tab_text,"html.parser")

# extracting records from table
records = []
for i, row in enumerate(tab_soup.find_all('tr')):
    record = [ele.text.strip() for j, ele in enumerate(row.find_all('td')) if j in [0, 3, 12]]
    if record != []:
        records.append([row.a['href']] + [i] + record)