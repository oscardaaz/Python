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

def listarTodosDiccionarios(lista):
    return lista

def listarUnDiccionario(diccionario):
    return diccionario

def menu():
    menu = """
    1. Introduce un nuevo usuario
    2. Lista los diccionarios totales.
    3. Lista un diccionario en particular
    """
    return menu
def main():
    # nombre = input("Introduce el nombre del usuario: ")
    # edad = input("Introduce la edad del usuario: ")
    # direccion = input("Introduce la dirección del usuario: ")
    # telefono = input("Introduce el teléfono del usuario: ")
    # diccionario1 = introducirUsuario(nombre,edad,direccion,telefono)
    # print(diccionario1)

    global diccionario, i
    entrada = 1
    totalDiccionarios = []

    while entrada != 0:
        entrada = input("Elige una opcion")
        print(menu())
        diccionario = diccionario + i
        i = 1
        if entrada == 1:
            nombre = input("Introduce el nombre del usuario: ")
            edad = input("Introduce la edad del usuario: ")
            direccion = input("Introduce la dirección del usuario: ")
            telefono = input("Introduce el teléfono del usuario: ")
            diccionario = introducirUsuario(nombre,edad,direccion,telefono)
            totalDiccionarios.append(diccionario)
            i += 1
        if entrada == 2:
            print(listarTodosDiccionarios(totalDiccionarios))
        if entrada == 3:
            diccionario = input("Introduce el nombre del diccionario a buscar: ").strip()
            print(listarUnDiccionario(diccionario))
        else:
            print("Opcion invalida")

        entrada = input("Elige una opción: ")
if __name__ == '__main__':
    main()


