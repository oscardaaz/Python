# Ejercicio 3.
# Escribe un programa donde se le pida
# al usuario una frase, y una letra, y
# se muestre cuántas veces esa letra
# aparece en la frase:

def contadorLetras(frase, letra):
    cantidad = 0
    resultado = 0
    for i in frase:
        if i == letra:
            resultado += 1
            # cantidad = frase.count(letra)
    return resultado, cantidad


def main():
    frase = input("Introduce una frase:\n> ")
    letra = input("Introduce la letra a buscar:\n> ").strip()
    resultado = contadorLetras(frase, letra)
    if letra == "":
        print(f"Las veces que aparece el caracter especial espacio: {letra}\n"
              f"en la frase: {frase}\n"
              f"son: {resultado} espacios")
    else:
        print(f"Las veces que aparece la letra: {letra}\n"
              f"en la frase: {frase}\n"
              f"son: {resultado} veces")


if __name__ == '__main__':
    main()
