#pip install webdriver_manager
#pip install selenium

import requests
import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import os
import time
from webdriver_manager.chrome import ChromeDriverManager


#Instalem el driver:
driver = webdriver.Chrome(ChromeDriverManager().install())

url='https://es.investing.com/indices/world-indices' 
driver.get(url) # Obrim la pg web a fer scraping.


# XPath de les taules = //table[contains(@id,"indice_table_")]
taules = driver.find_elements_by_xpath('//table[contains(@id,"indice_table_")]')
paisos_list = []
for p in range(len(paisos)):
    paisos_list.append(paisos[p].text)

