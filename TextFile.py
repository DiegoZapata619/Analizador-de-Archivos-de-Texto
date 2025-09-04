import re 
import os

#Función generadora que lee un archivo de texto y devuelve una palabra a la vez
def leer_palabras(nombre_archivo):
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        for linea in f:
#Distinque palabras, espacios y signos de puntuación
            for palabra in re.findall(r"\w+|\s|[^\w\s]", linea):
                yield palabra
#Entrada del nombre del archivo
archivo= input("Ingrese el nombre del archivo: ")
if os.path.isfile(archivo):
    for palabra in leer_palabras(archivo):
        print(palabra)
else:
    print("El archivo no existe.")
#Búsqueda de una expresión regular en el archivo
expresionRegular = input("Ingrese una expresión regular para buscar en el archivo: ")
with open(archivo, "r", encoding="utf-8") as f:
    contenido = f.read()
    #Se imprimen todas las coincidencias encontradas
    coincidencias = re.findall(expresionRegular, contenido)
    print(f"Se encontraron {len(coincidencias)} coincidencias:")
    #Resultado caracter por caracter
    for coincidencia in coincidencias:
        print(coincidencia)
