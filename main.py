
#pip install webdriver_manager
#pip install selenium
#pip install more-itertools

import requests
import selenium
from selenium import webdriver
import csv
import os
import time
from webdriver_manager.chrome import ChromeDriverManager
from more_itertools import split_after
#from selenium.webdriver.common.keys import Keys

#Instalem el driver:
driver = webdriver.Chrome(ChromeDriverManager().install())

url='https://es.investing.com/indices/world-indices' 
driver.get(url) # Obrim la pg web a fer scraping.

# XPath del nom dels paisos:'//*[@id="leftColumn"]//h2'
paisos = driver.find_elements_by_xpath('//*[@id="leftColumn"]//h2')

# XPath del titol de les taules:'//*[contains(@id,"indice_table_")]/thead//tr/th'
rows_title = driver.find_elements_by_xpath('//*[@id="indice_table_28"]/thead/tr/th')

# Inicialitzem les taules:
paisos_list = [] # Nom del pais
rows_title_list = [] # Header de les taules

# Obtenim el text dels elements:
for p in range(len(paisos)):
    paisos_list.append(paisos[p].text)

for rt in range(len(rows_title)):
    rows_title_list.append(rows_title[rt].text)

rows_title_list.pop(0) # Cal el pop per a desfer-nos de la primera columna, la qual és un espai (' ').

# Obtenim les id de cada una de les taules:
leftCol = driver.find_elements_by_xpath('//*[contains(@id,"indice_table_")]')
tables_id = []
for i in leftCol:
    tables_id.append(i.get_attribute('id'))

# Inicialitzem la llista on aniran les dades de les taules
rows_data_list = []

# Obtenim el directori i creem un nou csv file
currentDir = os.getcwd()
filename = 'Index_investments_mundial.csv'
filePath = os.path.join(currentDir, filename)

csvFile = open(filePath, 'wt', newline='')
writer = csv.writer(csvFile)

# Creem el csv
try: 
    for iid in tables_id: # Per a cada taula
        pais = paisos_list.pop(0) # Obtenim el pais de la taula on sóm
        # Escribim el pais i la header de la taula el csv file
        writer.writerow(pais)
        writer.writerow(rows_title_list)
        # XPath de les dades de les taules:'//*[@id='iid')]/tbody//tr//td'
        xpath = '//*[@id="' + iid + '"]/tbody//tr//td'
        rows_data = driver.find_elements_by_xpath(xpath) # Obtenim les dades de les taules
        rows_data_list = [] # Inicialitzem la llista
        for rd in range(len(rows_data)):
            rows_data_list.append(rows_data[rd].text) # Afegim les dades
        by_rows_data = list(split_after(rows_data_list, lambda x: x == ' ')) # Tallem la llista per files (rows)
        for row in by_rows_data:
            writer.writerow(by_rows_data) # Escribim les rows al document csv

finally:
    csvFile.close()
