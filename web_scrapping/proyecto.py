import bs4
import requests
#EXTRACCION DE UNA PAGINA WEB LIBRO CON 4 O 5 ESTRELLAS DE PUNTACION

#Página donde extraemos los datos sin numero de pagina
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# Lista de titulos de 4 o 5 estrellas
titulos_rating_alto = []

#iterar paginas
for pagina in range(1, 51):
    
    #crear sopa de paginas
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
    
    #seleccionar datos de los libros
    libros = sopa.select('.product_pod')
    
    #iterar libros
    for libro in libros:
        
        #Chequear que tengan 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) !=0 or len(libro.select('.star-rating.Five')) !=0:
            
            #Guardar titulo en variable
            titulo_libro = libro.select('a')[1]['title']
            
            #Agregar libro a lista
            titulos_rating_alto.append(titulo_libro)

#Ver libros de 4 u 5 estrellas en pantalla
for t in titulos_rating_alto:
    print(t)