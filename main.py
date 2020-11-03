
#pip install webdriver_manager
#pip install selenium

import requests
import selenium
from selenium import webdriver
import csv
import os
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys

#Instalem el driver:
driver = webdriver.Chrome(ChromeDriverManager().install())

url='https://es.investing.com/indices/world-indices' 
driver.get(url) # Obrim la pg web a fer scraping.

# XPath del nom dels paisos:'//*[@id="leftColumn"]//h2'
paisos = driver.find_elements_by_xpath('//*[@id="leftColumn"]//h2')

# XPath del titol de les taules:'//*[contains(@id,"indice_table_28")]/thead//tr/th'
rows_title = driver.find_elements_by_xpath('//*[@id="indice_table_28"]/thead/tr/th')
# XPath del titol de les taules:'//*[contains(@id,"indice_table_")]/tbody//tr//td'
rows_data = driver.find_elements_by_xpath('//*[contains(@id,"indice_table_")]/tbody//tr//td')

paisos_list = []
rows_title_list = []
rows_data_list = []


for p in range(len(paisos)):
    paisos_list.append(paisos[p].text)
for rt in range(len(rows_title)):
    rows_title_list.append(rows_title[rt].text)
for rd in range(len(rows_data)):
    rows_data_list.append(rows_data[rd].text)

#diccionari = {rows_title_list[i]: rows_data_list[i] for i in range(len(rows_title_list))}

 currentDir = os.path.dirname(__file__)
    filename = 'Index_investments_mundial.csv'
    filePath = os.path.join(currentDir, filename)

    csvFile = open(filePath, 'wt', newline=' ')
    writer = csv.writer(csvFile)

    #anem fent fins que troba el final de row.
    for p in paisos_list:
        writer.writerow(p)
        writer.writerow(rows_title_list)
        # A partir d'aqui no ho he canviat encara
        try:
            for c in rows_data_list:  # per cada cella
                td = c.find_all('td')
                row2 = [i.text.replace('\xa0','') for i in td]  # per eliminar el &nspb
                writer.writerow(row2)
        finally:
            csvFile.close()  # si final de row
        return 0

