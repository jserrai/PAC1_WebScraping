import requests
from bs4 import BeautifulSoup
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
    url = 'https://www.bcn.cat/estadistica/catala/dades/tdemo/naix/evo/sexe03.htm'
    pag_web = requests.get(url)
    soup= BeautifulSoup(pag_web.content)
    taula = soup.find('table').get_text() # He afegit aquesta linea per a obtenir la taula de la primera url.
    print(taula)

    # per mirar si recupera be la primera web
    # sha de canviar la url per cada una de les que hem de mirar

