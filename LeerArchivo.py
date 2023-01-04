archivo = open('prueba.dat', 'r', encoding='utf8')
# print(archivo.read())
# lee tod0 el archivo

# Leer algunos caracteres de algun archivo
# print(archivo.read(3)) #Primeros 3 caracteres
# print(archivo.read(3)) #siguientes 3 caracteres


# Leer una linea del archivo

# print(archivo.readline())


# Leer con un FOR
#for linea in archivo:
#    print(linea)

# leer t0do--> devuelve una lista
#print(archivo.readLines())


#Copiar un archivo
    #El archivo a copiar solo debe estar abierto y no leido, sino no tendra nada que copiar al nuevo archivo
archivocopia = open('nuevo.dat', 'a', encoding='utf8')
# a --> para adicionar nueva informacion y si no existe lo crea

archivocopia.write(archivo.read())