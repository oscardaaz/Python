# Ejercicio 5.
# Escribe un programa que pida al usuario
# una frase, y la imprima por pantalla al revés.
# Pista: usa la función split para dividir la frase en palabras.

# No se si el enunciado se refiere a invertir por caracteres o por palabras,
# así que dejo las dos posibilidades.

def imprimirRevesCaracteres(frase):
    # Aquí iremos guardando la frase al revés
    frase_invertida = ""

    # Recorremos la frase al reves
    for i in reversed(frase):
        # Vamos añadiendo cada carácter a la nueva cadena
        frase_invertida += i

    # Devolvemos la frase invertida
    return frase_invertida

def imprimirRevesPorPalabras(frase):
    # Separamos la frase en una lista de palabras
    palabras = frase.split()

    # Guardamos la frase al reves
    frase_invertida = ""

    # Recorremos la lista de las palabras al reves tambien
    for palabra in reversed(palabras):
        # Vamos añadiendo cada palabra y un espacio
        frase_invertida += palabra + " "

    # Quitamos el espacio final que sobra y devolvemos la frase
    return frase_invertida


def main():
    # Pedimos una frase al usuario
    frase = input("Introduce una frase a imprimir al revés,\n > ")

    # Imprimimos la frase invertida por caracteres
    print("\nFrase invertida por caracteress:")
    print(imprimirRevesCaracteres(frase))

    #Imprimimos la frase invertida por palabras
    print("\nFrase invertida por palabras:")
    print(imprimirRevesPorPalabras(frase))

if __name__ == '__main__':
    main()
