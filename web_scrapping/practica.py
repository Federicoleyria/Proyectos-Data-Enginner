#!C:/Users/fedel/OneDrive/Escritorio/juego_Python/python_juego/Scripts/python.exe
import bs4
import requests

# link : https://escueladirecta-blog.blogspot.com/

resultado = requests.get('https://escueladirecta-blog.blogspot.com/')



# print(sopa.select('title')[0].getText())


#Extraemos através de clases
# parrafo_especial = sopa.select('.title')[1].getText()
#print(parrafo_especial)

#Extraemos imágenes

link_img = requests.get('https://www.escueladirecta.com/courses/')

sopa = bs4.BeautifulSoup(link_img.text, 'lxml')

imagenes = sopa.select('.course-box-image')[0]['src']
print(imagenes)

imagen_curso_1 = requests.get(imagenes)

f = open('mi_imagen.jpg', 'wb')
f.write(imagen_curso_1.content)
f.close()

#EXTRACCION DE LIBROS
#Indicamos que página dentro del url queremos extraer
resultado = requests.get(url_base.format('1'))
#Guardamos en una variable el contenido de la página
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

#Traermos las clases donde estan alojadas los libros
libros = sopa.select('.product_pod')

#Traemos las clases donde se encuentra las estrellas del libro, si contiene un espacio la clase este debe ser remplazado por un '.'
ejemplo = libros[0].select('.star-rating.Three')
#Extraemos el titulo del libro, donde primero buscamos dentro d ela etiqueta 'a', buscamos la segunda etiqueta ya que la primera es la imagen [1] y buscamos el valor [title]
ejemplo2 =libros[0].select('a')[1]['title'] 

print(ejemplo)

# for n in range(1, 11):
#     print(url_base.format(n))