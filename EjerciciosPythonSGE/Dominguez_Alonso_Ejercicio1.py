# Ejercicio 1:
# Escribe una función que devuelva la longitud
# de una lista o cadena, sin usar la función len().

def longitudCadena(lista):
    
    longitud = 0

    # Recorremos cada elemento
    for i in lista:
        # Por cada posición que encontramos, sumamos 1
        longitud += 1

    return longitud # Devolvemos el total

def main():
    # Lista de ejemplo
    lista = ["Oscar", "Jorge", "Patri", "Juan", "Dani"]

    # Mostramos el resultado por pantalla
    print(f"\nLa longitud de tu lista/cadena es de: {longitudCadena(lista)} elementos")

if __name__ == '__main__':
    # Esto hace que main() se ejecute solo si abrimos este archivo directamente
    main()