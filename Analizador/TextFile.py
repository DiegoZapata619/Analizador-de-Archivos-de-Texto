import re 
import os

def escribir_coincidencias(nombre_texto_final, coincidencias):
    with open(nombre_texto_final, "w", encoding="utf-8") as f:
        for coincidencia in coincidencias:
            f.write(coincidencia + "\n")

#Entrada del nombre del archivo
archivo= input("Ingrese la dirección del archivo de texto (Incluya la terminación .txt): ")
#Verifica si el archivo existe antes de intentar leerlo
while True:
    if os.path.isfile(archivo):
        break
    else:
        print("El archivo no existe. Intente de nuevo.")
        archivo= input("Ingrese la dirección del archivo de texto: ")

#Se crea yb array que almacenará las coincidencias
coincidencias = []

#Input de la expresión regular y el nombre del archivo de salida
expresionRegular = input("Ingrese una expresión regular para buscar en el archivo: ")
nombre_texto_final = input("Ingrese el nombre del archivo donde se guardarán las coincidencias: ")

# Lee el archivo y busca las coincidencias. 
with open(archivo, "r", encoding="utf-8") as f:
    for linea in f:
# Divide la línea en palabras usando espacios como separadores. re.findall(r"\S+", linea) encuentra palabras e ignora tabulaciones, espacios múltiples y saltos de línea.
        palabras = re.findall(r"\S+", linea)
        for palabra in palabras:
            if re.fullmatch(expresionRegular, palabra,re.IGNORECASE):
                coincidencias.append(palabra)

if coincidencias:
    escribir_coincidencias(nombre_texto_final, coincidencias)
    #Si se encuentran coincidencias, se guardan en el archivo con el nombre proporcionado
    print(f"Se encontraron {len(coincidencias)} coincidencias. Se han guardado en '{nombre_texto_final}'.")
else:
    print("No se encontraron coincidencias.")
