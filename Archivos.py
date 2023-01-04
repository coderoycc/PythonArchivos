#Para dar rutas se debe poner doble diagonal c:\\Cursos\\Python (WINDOWS)
try:
    #abrimos el archivo, para escritura <w>, si no existe el archio lo crea
    archivo = open('prueba2.dat', 'x', encoding='utf8')
    archivo.write('Que tiene este archivo\n')
except Exception as e:
    print("Error: ",e)

finally:
    archivo.close()
    print("El archivo se ha cerrado")

"""
r --> abre un archivo para lectura (opcion por default) manda un error si es que el archivo no existe
*a --> abre un archivo para anexar informacion, cuando abras un archivo ya no se podra perder la informacion (Crea el archivo si no existe)
w --> Abre un archivo para escribir informacion, crea un archivo nuevo si no existe 
x --> crea un archivo y manda un error si el archivo ya existe
        manda otro error si tratas de cerrar el archivo existente

w+ --> Significa que se usara para escribir y para leer informacion
r+ --> para leer y escribir
"""