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


# XPath dels paisos = //*[@id="leftColumn"]//h2
paisos = driver.find_elements_by_xpath('//*[@id="leftColumn"]//h2')

# XPath de les taules = //table[contains(@id,"indice_table_")]
taules = driver.find_elements_by_xpath('//table[contains(@id,"indice_table_")]')

paisos_list = []
for p in range(len(paisos)):
    paisos_list.append(paisos[p].text)
    
taules_list = []   
for t in range(len(taules)):
    taules_list.append(taules[t].text)
    
# Creem un diccionari per ajuntar els paisos amb la seva taula
diccionari = {paisos_list[i]: taules_list[i] for i in range(len(paisos_list))}



