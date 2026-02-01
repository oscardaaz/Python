# Ejercicio 4.
# Escribe un programa que pida al
# usuario: nombre, edad, dirección, y
# teléfono. Esa información se deberá
# guardar en un diccionario, y mostrarla
# por pantalla.

def introducirUsuario(nombre, edad, direccion, telefono):
    # Creamos un diccionario con los datos del usuario
    usuarios = {
        "nombre": nombre,
        "edad": edad,
        "direccion": direccion,
        "telefono": telefono
    }
    # Hacemos un return del diccionario
    return usuarios

def main():
    # Pedimos los datos por teclado
    nombre = input("Introduce el nombre del usuario: ")
    edad = input("Introduce la edad del usuario: ")
    direccion = input("Introduce la dirección del usuario: ")
    telefono = input("Introduce el teléfono del usuario: ")

    # Guardamos todo en un diccionario usando la función
    diccionario1 = introducirUsuario(nombre, edad, direccion, telefono)

    # Mostramos el diccionario
    print(diccionario1)

if __name__ == '__main__':
    main()
