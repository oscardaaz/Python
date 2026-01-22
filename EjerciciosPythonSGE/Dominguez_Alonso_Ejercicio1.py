
# Ejercicio 1:
# Escribe una función que devuelva la longitud
# de una lista o cadena, sin usar la función len().

def longitudCadena(lista):

    longitud = 0
    for i in lista:
        longitud += 1
    return longitud

def main():
    lista = ["Oscar","Jorge","Patri","Juan","Dani"]
    print(f"\nLa longitud de tu lista/cadena es de: {longitudCadena(lista)} elementos")

if __name__ == '__main__':
    main()


