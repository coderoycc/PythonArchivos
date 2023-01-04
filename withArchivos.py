#El manejo de archivo con with hace que un bloque se ejecute
# sin manejo de excepciones y sin tener que cerrar el archivo

with open('nuevo.dat','r+', encoding='utf8') as archivo:
    for i in archivo:
        print(i)

    archivo.write('\no te meas')

