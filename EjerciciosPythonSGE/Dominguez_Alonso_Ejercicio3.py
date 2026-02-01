# Ejercicio 3.
# Escribe un programa donde se le pida
# al usuario una frase, y una letra, y
# se muestre cuántas veces esa letra
# aparece en la frase:

def contadorLetras(frase, letra):
   
    resultado = 0    # aquí guardamos cuántas veces aparece la letra

    # Recorremos la frase letra por letra
    for i in frase:
        # Si la letra actual coincide con la letra que buscamos...
        if i == letra:
            # Sumamos 1 al contador
            resultado += 1
            # Otra forma sería: frase.count(letra) (pero aquí lo hacemos a mano)
            # cantidad = frase.count(letra)

    # Devolvemos el resultado 
    return resultado


def main():
    # Pedimos la frase al usuario
    frase = input("Introduce una frase:\n> ")

    # Pedimos la letra a buscar (strip quita espacios al principio y al final)
    letra = input("Introduce la letra a buscar:\n> ").strip()

    # Llamamos a la función para contar
    resultado = contadorLetras(frase, letra)

    # Si el usuario no escribió nada (cadena vacía)
    if letra == "":
        
        print(f"Las veces que aparece el caracter especial espacio: {letra}\n"
              f"en la frase: {frase}\n"
              f"son: {resultado} espacios")
    else:
        #Si escribió una letra válidas
        # Mostramos cuántas veces aparece la letra
        print(f"Las veces que aparece la letra: {letra}\n"
              f"en la frase: {frase}\n"
              f"son: {resultado} veces")


if __name__ == '__main__':
    # Solo se ejecuta si abrimos este archivo directamente
    main()
