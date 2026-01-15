# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}') # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    name = "Oscar"
    print(f "Hello, {name}!")

    #if 5 > 2:
       # print ("Five is greater than two!")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""
from functools import total_ordering

from unicodedata import numeric


# Ejercicio 01
# def saludar(nombre):
#     print(f"Hola, {nombre}!")
#
# def main():
#     nombre2 = input("Introduce tu nombre: ")
#     saludar(nombre2)
#
# if __name__ == '__main__':
#     main()

# Ejercicio 02
# def es_par(numero):
#     if numero % 2 == 0:
#         return True
#     else:
#         return False
#     #Lo mismo, pero más fácil
#     # return if número % 2 == 0
#
#
# def main():
#     numero = int(input("Introduce un numero: "))
#     if es_par(numero):
#         print(f"El numero {numero} es par")
#     else:
#         print(f"El numero {numero} es impar")
#
# if __name__ == '__main__':
#     main()

# Ejercicio 03
def sumar_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

def main():
    numeros = []
    for i in range(3):
        numero = int(input(f"Introduce el número {i+1}: "))
        numeros.append(numero)  # guardamos en la lista
    print(f"La suma de los números es {sumar_lista(numeros)}")

if __name__ == '__main__':
    main()