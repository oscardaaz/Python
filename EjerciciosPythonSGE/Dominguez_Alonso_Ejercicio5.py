# Ejercicio 5.
# Escribe un programa que pida al usuario
# una frase, y la imprima por pantalla al revés.
# Pista: usa la función Split para dividir la frase en palabras.

def imprimirReves(frase):

    frase_invertida = ""
    for i in reversed(frase):
        frase_invertida += i
    return frase_invertida

def main():
    frase = input("Introduce una frase a imprimir al revés,\n > ")
    print(imprimirReves(frase))

if __name__ == '__main__':
    main()


