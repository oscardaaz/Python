class Personaje:
    """
    self es un atributo que hace referencia a si mismo. 
    A través del punto, puedes llamar a los métodos y atributos de la clase.

    Además. con self, se están declarando qué atributos del objeto se van a inicializar en 
    el momento de crearse, por lo que no es necesario que se declaren los atributos.
    """

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("Fuerza:", self.fuerza)
        print("Inteligencia:", self.inteligencia)
        print("Defensa", self.defensa)
        print("Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    # TAREA!!!!!!
    # El daño no debe de ser negativo, es decir, si la defensa fuera mayor que la fuerza
    # debería de restarle la defensa al enemigo, y mostrárlo en pantalla. En cualquier caso, 
    # habría que devolver un daño que sería 0 dado que todavía le queda defensa

    # Ten en cuenta que hay que cambiarlo también en las clases hijas!
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("La vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()


class Guerrero(Personaje):

    # Sobreescribimos el constructor heredado de Personaje para incluir un parámetro más
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_Arma(self):
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10"))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Opción no encontrada")

    def atributos(self):
        super().atributos()
        print("Espada", self.espada)

    def daño(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa


class Mago(Personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        super().atributos()
        print("Libro", self.libro)

    def daño(self, enemigo):
        return self.fuerza * self.libro - enemigo.defensa


def combate(jugador_1, jugador_2):
    turno = 1
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de " + jugador_1.nombre + ":")
        jugador_1.atacar(jugador_2)
        print(">>> Acción de " + jugador_2.nombre + ":")
        jugador_2.atacar(jugador_1)
        turno = turno + 1

    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.nombre)

    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.nombre)
    else:
        print("\nEmpate")


personaje_1 = Guerrero("Guts", 20, 10, 4, 100, 4)
personaje_2 = Mago("Vanessa", 5, 15, 4, 100, 3)

personaje_1.atributos()
print()
personaje_2.atributos()

combate(personaje_1, personaje_2)