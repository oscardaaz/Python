# Ejercicio 4.
# Escribe un programa que pida al
# usuario: nombre, edad, dirección, y
# teléfono. Esa información se deberá
# guardar en un diccionario, y mostrarla
# por pantalla.

def introducirUsuario(nombre,edad,direccion,telefono):
    usuarios = {
        "nombre": nombre,
        "edad": edad,
        "direccion": direccion,
        "telefono": telefono
    }
    return usuarios

def main():
    nombre = input("Introduce el nombre del usuario: ")
    edad = input("Introduce la edad del usuario: ")
    direccion = input("Introduce la dirección del usuario: ")
    telefono = input("Introduce el teléfono del usuario: ")
    diccionario1 = introducirUsuario(nombre,edad,direccion,telefono)
    print(diccionario1)

if __name__ == '__main__':
    main()


