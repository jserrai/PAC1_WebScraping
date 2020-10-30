import requests
from bs4 import BeautifulSoup
import csv
import os
import pandas as pd   ### per que fas servir el pandas? es per tractament estadistic, per tractar csv hi ha el paquest csv


'''
# Aixó ho eliminem, però així ho tenim més a mà ja que els hem de mirar totes 
URL's de les dades evolutives per barris, demografia Barcelona:

Naixements: 'https://www.bcn.cat/estadistica/catala/dades/tdemo/naix/evo/sexe03.htm'
Defuncions: 'https://www.bcn.cat/estadistica/catala/dades/tdemo/defu/evo/sexe03.htm'
Immigrants: 'https://www.bcn.cat/estadistica/catala/dades/tdemo/imi/evo/sexe03.htm'
Emmigrants: 'https://www.bcn.cat/estadistica/catala/dades/tdemo/emi/evo/sexe03.htm'
Altes per omisió: 'https://www.bcn.cat/estadistica/catala/dades/tdemo/omi/evo/sexe03.htm'
Baixes per inscripció indeguda: 'https://www.bcn.cat/estadistica/catala/dades/tdemo/baixes/evo/sexe03.htm'
'''

urls = ['https://www.bcn.cat/estadistica/catala/dades/tdemo/naix/evo/sexe03.htm']
#, 'https://www.bcn.cat/estadistica/catala/dades/tdemo/defu/evo/sexe03.htm',
#'https://www.bcn.cat/estadistica/catala/dades/tdemo/imi/evo/sexe03.htm', 'https://www.bcn.cat/estadistica/catala/dades/tdemo/emi/evo/sexe03.htm',
#'https://www.bcn.cat/estadistica/catala/dades/tdemo/omi/evo/sexe03.htm', 'https://www.bcn.cat/estadistica/catala/dades/tdemo/baixes/evo/sexe03.htm']



def obtenir_taula(url):
    # Extraiem el titol del URL (Naix = Naixements, defu = defuncions, imi = imigrant, emi = emigrants, omi = omisió, baixes = baixes per inscripció indeguda o caducitat.
    name = url.split('https://www.bcn.cat/estadistica/catala/dades/tdemo/' )
    name = "".join(name)
    name = name.split('/evo/sexe03.htm' )
    name = "".join(name)

    # Extraiem les dades de la url:
    pag_web = requests.get(url)
    soup= BeautifulSoup(pag_web.content,'html.parser')
    table = soup.find("table") # Per a obtenir el codi de la taula de la url.
    row = table.find_all("tr") # Per a trobar totes les files
    taula = [] # Inicialitzem la taula
    row_num = -1 # Inicialitzem la fila en la que ens trobem
 #   for r in row: # Iterem per totes les files
 #       row_num += 1
 #       taula.append([])
 #       for c in r.find_all("td"):
 #           columna = c.get_text(strip=True) # (!) Obtenim només el text
 #           taula[row_num].append(columna)
    # Transformem i guardem les dades en forma de .csv
#    df = pd.DataFrame(taula)

    currentDir = os.path.dirname(__file__)
    filename = name + '.csv'
    filePath = os.path.join(currentDir, filename)


    csvFile = open(filePath, 'wt', newline='', encoding='utf-8')
    writer = csv.writer(csvFile)
    try:
        for cell in row:
            th = cell.find_all('th')
            th_data = [col.text.strip('\n') for col in th]
            td = cell.find_all('td')
            row2 = [i.text.replace('\xa0','') for i in td]
            writer.writerow(th_data + row2)
    finally:
        csvFile.close()
#    with open(filePath, 'wt', newline='', encoding='utf-8') as csvFile:

 #       writer = csv.writer(csvFile)
 #       for element in taula:
 #           writer.writerow(element)
    return 0



if __name__ == '__main__':

    for i in urls:
        obtenir_taula(i)
