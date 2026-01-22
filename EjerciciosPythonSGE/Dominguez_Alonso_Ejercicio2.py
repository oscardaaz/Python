
# Ejercicio 2.
# Escribir un programa que pida al
# usuario una palabra y luego muestre
# por pantalla una a una las letras de
# la palabra introducida empezando por la última.

def letrasInvertidas(palabra):

    for i in reversed(palabra):
        print(i)
    # for i in enumerate(palabra):
    #     print(i)

def main():
    palabra = input("Introduce una palabra: ")
    letrasInvertidas(palabra)

if __name__ == '__main__':
    main()


