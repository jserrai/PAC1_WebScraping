
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

#Inicialitzem les taules
paisos_list = []
rows_title_list = []

for p in range(len(paisos)):
    paisos_list.append(paisos[p].text)


for rt in range(len(rows_title)):
    rows_title_list.append(rows_title[rt].text)

rows_title_list.pop(0)

# Obtenim totes les id de les taules:
leftCol = driver.find_elements_by_xpath('//*[contains(@id,"indice_table_")]')
tables_id = []
for i in leftCol:
    tables_id.append(i.get_attribute('id'))


rows_data_list = []

currentDir = os.getcwd()
filename = 'Index_investments_mundial.csv'
filePath = os.path.join(currentDir, filename)

csvFile = open(filePath, 'wt', newline='')
writer = csv.writer(csvFile)

c = 0
try: 
    for iid in tables_id:
        pais = paisos_list.pop(c)
        # XPath del titol de les taules:'//*[contains(@id,"indice_table_")]/tbody//tr//td'
        writer.writerow(pais)
        writer.writerow(rows_title_list)
        xpath = '//*[@id="' + iid + '"]/tbody//tr//td'
        rows_data = driver.find_elements_by_xpath(xpath)
        rows_data_list = []
        for rd in range(len(rows_data)):
            rows_data_list.append(rows_data[rd].text)
        by_rows_data = list(split_after(rows_data_list, lambda x: x == ' '))
        for row in by_rows_data:
            writer.writerow(by_rows_data)
        c += 1
finally:
    csvFile.close()
