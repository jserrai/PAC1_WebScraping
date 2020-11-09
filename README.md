# _Web scraping_ de Cotitzacions mundials de borsa

## Components del grup:
Jordi Serra i Paula Sobrevals

## Index

Cotitzacions mundials.csv - Dataset extret en format csv.
Imatges - Carpeta amb les imatges utilitzades a la wiki del Repositori.
main.py - Codi utilitzat per a dur a terme el Web Scraping i crear el dataset.
PAC1_WebScraping.pdf - Document PDF amb les preguntes i respostes + taula de contribucions.

Wiki del repositori - Descripcioó de la PAC, Bibliografia i components del grup.



![https://www.altonivel.com.mx/empresas/listar-empresa-bolsa-de-valores/](https://github.com/PSobrevals/PAC1_WebScraping/blob/main/Imatges/bolsa.jpg) 

(foto: https://www.altonivel.com.mx/empresas/listar-empresa-bolsa-de-valores/)

## Descripció de la PAC:
 
Es crea un repositori de dades obtingudes a partir de la web https://es.investing.com on es mostren les cotitzacions de les diferents borses mundials a temps real. A la pàgina web es pot veure com varien els principals índex bursàtils de cada país durant el temps en que estan obertes i operant les borses. Un cop tancades es manté el valors fins a la següent actualització.

El codi per fer web _scraping _obté les dades reals en el moment d'executar-lo, ceant un document CSV de tots els valors en aquell moment i guardant en el mateix fitxer de dades la data i hora en que s'ha obtingut les dades.

La web exacte des d'on es treuren les dades es:

[https://es.investing.com/indices/world-indices](https://es.investing.com/indices/world-indices)

<p align="center">
  <img width="920" height="600" src="https://github.com/PSobrevals/PAC1_WebScraping/blob/main/Imatges/Web.jpg">
</p>

<br><br>
S'ha fet servir **SELENIUN** per tal d'obtenir les dades de la pàgina web, ja que aquestes no es publiquen directament en codi html, sinó que es fà de manera dinàmica i per tant s'ha de simular un navegador que accedeix a la web per poder lleguir-les d'allà. 

Per tal de simular el navegador hem fet servir la següent comanda que genera una crida al navegador Chrome

```
#Instalem el driver:
driver = webdriver.Chrome(ChromeDriverManager().install())
```

A la vegada, el codi té en compte l'acceptació de les cookies de la web de manera automàtica, ja que surt un pop-up d'acceptació de les cookies del lloc web que tractem acceptant-lo automàticament. Fent servir la següent comanda:

```
#per treure les coockies
driver.find_elements_by_xpath('//*[@id="onetrust-accept-btn-handler"]')[0].click()
```

A partr d'aquí es fa una cerca de les diferents taules per cada un dels països, mirant primer quins països hi ha a la web en aquell moment, fent servir la comanda:

```
# XPath del nom dels paisos:'//*[@id="leftColumn"]//h2'
paisos = driver.find_elements_by_xpath('//*[@id="leftColumn"]//h2')

# XPath del titol de les taules:'//*[contains(@id,"indice_table_")]/thead//tr/th'
rows_title = driver.find_elements_by_xpath('//*[@id="indice_table_28"]/thead/tr/th')
```

A partir d'aquí es pasa a una taula general i es netejen els valors vuits que genera en aquest cas la propia estructura de la publicació, ja que crea espais en blanc entre cada una de les files de cada indentificador, no es un error de dades mal obtingudes, ja que estan totes publicades i en aquesta part no es fa la neteja de dades sinó només la obtenció.

Amb la següent comanda eliminem les files en blanc que trobem entre les files dels indexs. Oobtenim les dades i les guardem al repositori en format CSV.

```
if len(row)!=1:
    writer.writerow(row[1:len(row)]) # Escribim les rows al document csv
```


## Bibliografia

> * Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd. Scraping the Data.<br>
> * Mitchel, R. (2015). Web Scraping with Python: Collecting Data from the Modern Web. O'Reilly Media, Inc. Chapter 1. Your First Web Scraper. <br>
> * "Web Scraping de páginas dinámicas con Selenium, Python y Beautifulsoup" https://blogs.solidq.com/es/business-analytics/web-scraping-de-paginas-dinamicas-con-selenium-python-y-beautifulsoup-en-azure-data-studio/

