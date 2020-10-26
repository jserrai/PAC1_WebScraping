import requests
from bs4 import BeautifulSoup
import pandas as pd
'''
# Aixó ho eliminem, però així ho tenim més a mà ja que els hem de mirar totes 
URL's de les dades evolutives per barris, demografia Barcelona:

Naixements: 'https://www.bcn.cat/estadistica/catala/dades/tdemo/naix/evo/sexe03.htm'
Defuncions: 'https://www.bcn.cat/estadistica/catala/dades/tdemo/defu/evo/sexe03.htm'
Immigrants: 'https://www.bcn.cat/estadistica/catala/dades/tdemo/imi/evo/sexe03.htm'
Emmigrants: 'https://www.bcn.cat/estadistica/catala/dades/tdemo/emi/evo/sexe03.htm'
Altes per omisió: 'https://www.bcn.cat/estadistica/catala/dades/tdemo/omi/evo/sexe03.htm'
Baixes per inscripció indeguda: 'https://www.bcn.cat/estadistica/catala/dades/tdemo/baixes/evo/sexe03.htm'
Canvis de nacionalitat: 'https://www.bcn.cat/estadistica/catala/dades/tdemo/canvisnacio/evo/t03.htm'

urls = ['https://www.bcn.cat/estadistica/catala/dades/tdemo/naix/evo/sexe03.htm', 'https://www.bcn.cat/estadistica/catala/dades/tdemo/defu/evo/sexe03.htm',
        'https://www.bcn.cat/estadistica/catala/dades/tdemo/imi/evo/sexe03.htm', 'https://www.bcn.cat/estadistica/catala/dades/tdemo/emi/evo/sexe03.htm', 
        'https://www.bcn.cat/estadistica/catala/dades/tdemo/omi/evo/sexe03.htm', 'https://www.bcn.cat/estadistica/catala/dades/tdemo/baixes/evo/sexe03.htm',
        'https://www.bcn.cat/estadistica/catala/dades/tdemo/canvisnacio/evo/t03.htm']
'''
if __name__ == '__main__':
    url = 'https://www.bcn.cat/estadistica/catala/dades/tdemo/naix/evo/sexe03.htm' # He canviat l'URL per als naixements.
    pag_web = requests.get(url)
    soup= BeautifulSoup(pag_web.content)
    table = soup.find('table') # Per a obtenir el codi de la taula de la primera url.
    row = table.find_all("tr") # Per a trobar totes les files
    taula = [] # Inicialitzem la taula
    row_num = -1 # inicialitzem la fila en la que ens trobem
    for r in row: # Itenerm per totes les files
   	row_num += 1 
	taula.append([]) 
	for c in r.find_all("td"): 
		columna = c.get_text(strip=True)
		taula[row_num].append(columna)
		
df = pd.DataFrame(taula)
df
df.to_csv('/Users/paula/Desktop/Taula.csv', index = False) # Crea un df amb la taula dels naixements.

    # per mirar si recupera be la primera web
    # sha de canviar la url per cada una de les que hem de mirar

