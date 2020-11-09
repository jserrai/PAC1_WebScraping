#pip install webdriver_manager
#pip install selenium
#pip install more-itertools

import requests
import selenium
from selenium import webdriver
import csv
import os
import time
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from more_itertools import split_before

# Per mesurar el temps que triga en fer el procediment d'obtenció de les dades:
start_time = time.time()

# Instalem el driver:
driver = webdriver.Chrome(ChromeDriverManager().install())

url = 'https://es.investing.com/indices/world-indices' 
driver.get(url) # Obrim la pg web a fer scraping.
time.sleep(5) # Esperem 5 segons a que es carregui la pagina completament

# Fem click al banner per treure l'avís de les coockies
driver.find_elements_by_xpath('//*[@id="onetrust-accept-btn-handler"]')[0].click()

print('----Obtenint les dades...----', '\n')


# XPath del nom dels paisos:'//*[@id="leftColumn"]//h2'
paisos = driver.find_elements_by_xpath('//*[@id="leftColumn"]//h2')

# XPath del titol de les taules:'//*[contains(@id,"indice_table_")]/thead//tr/th'
rows_title = driver.find_elements_by_xpath('//*[@id="indice_table_28"]/thead/tr/th')

# Inicialitzem les taules:
paisos_list = [] # Nom del pais
rows_title_list = [] # Header de les taules

# Obtenim el text dels elements i els afegim a una llista:
for p in range(len(paisos)):
    paisos_list.append(paisos[p].text)


for rt in range(len(rows_title)):
    rows_title_list.append(rows_title[rt].text)


# Obtenim les id de cada una de les taules:
leftCol = driver.find_elements_by_xpath('//*[contains(@id,"indice_table_")]')
tables_id = []
for i in leftCol:
    tables_id.append(i.get_attribute('id'))


# Obtenim el directori i creem un nou csv file
currentDir = os.getcwd()
filename = 'Cotitzacions mundials.csv'
filePath = os.path.join(currentDir, filename)

csvFile = open(filePath, 'wt', newline='')
writer = csv.writer(csvFile)

print('----Escribint el csv...----', '\n')
print('Això pot trigar aproximadament 1 minut i mitg.', '\n')
print('Avisarem amb un missatge quan hagi acabat.')


# Omplim el csv
c = 0
for iid in tables_id : # Per a cada taula:
    
    pais = paisos_list[c] # Obtenim el pais de la taula on sóm
    
    # Escribim el pais i la header de la taula el csv file
    writer.writerow([pais])
    writer.writerow(rows_title_list[1:])
    
    # XPath de les dades de les taules:'//*[@id='iid')]/tbody//tr//td'
    xpath = '//*[@id="' + iid + '"]/tbody//tr//td'
    rows_data = driver.find_elements_by_xpath(xpath) # Obtenim les dades de les taules
    
    rows_data_list = [] # Inicialitzem la llista on aniran les dades de les taules
    # Afegim el text (les dades) a la llista:
    for rd in range(len(rows_data)): 
        rows_data_list.append(rows_data[rd].text) 
    
    by_rows_data = list(split_before(rows_data_list, lambda x: x == ' ')) # Tallem la llista per files (rows)
    
    # Escribim les rows al document csv:
    for row in by_rows_data:
        if len(row)!=1:
            writer.writerow(row[1:len(row)])
    
    #Afegim una fila en blanc per a separar les taules:
    writer.writerow(' ')
    c += 1


# Obtenim el moment en el que hem extret les dades i l'afegim al final del dataset:
data = datetime.now()
ara = [data.strftime("%d/%m/%Y %H:%M:%S")]
writer.writerow(ara)

# Tanquem el dataset:
csvFile.close()

# Calculem el temps d'execució: 
t = int(time.time() - start_time)
minuts = t//60
segons = t - (minuts*60)
print('----Fet!----', '\n')
print('Temps total: ', minuts, 'minuts', segons,'segons') # ~ 2 miniuts 30 segons
