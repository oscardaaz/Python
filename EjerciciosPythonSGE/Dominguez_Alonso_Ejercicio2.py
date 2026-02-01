# Ejercicio 2.
# Escribir un programa que pida al
# usuario una palabra y luego muestre
# por pantalla una a una las letras de
# la palabra introducida empezando por la última.

def letrasInvertidas(palabra):
    # Recorremos la palabra al revés (de la última letra a la primera)
    for i in reversed(palabra):
        # Imprimimos cada letra en una línea
        print(i)

def main():
    # Pedimos una palabra al usuario
    palabra = input("Introduce una palabra: ")
    
    # Llamamos a la función para mostrar las letras al revés
    letrasInvertidas(palabra)

if __name__ == '__main__':
    # Solo se ejecuta si este archivo se ejecuta directamente
    main()