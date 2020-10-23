import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    url = 'https://www.bcn.cat/estadistica/catala/dades/tdemo/index.htm'
    pag_web = requests.get(url)
    soup= BeautifulSoup(pag_web.content)

    # per mirar si recupera be la primera web
    # sha de canviar la url per cada una de les que hem de mirar
    print(soup)
