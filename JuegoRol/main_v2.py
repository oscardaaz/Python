import random


class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida_maxima = vida
        self.vida = vida
        self.nivel = 1
        self.experiencia = 0

    def atributos(self):
        print(f"{self.nombre} (Nivel {self.nivel}):")
        print(f"  Vida: {self.vida}/{self.vida_maxima}")
        print(f"  Fuerza: {self.fuerza}")
        print(f"  Inteligencia: {self.inteligencia}")
        print(f"  Defensa: {self.defensa}")
        print(f"  XP: {self.experiencia}/100")

    def subir_nivel(self, fuerza=0, inteligencia=0, defensa=0, vida=0):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa
        self.vida_maxima += vida
        self.vida = self.vida_maxima  # Curar completamente al subir nivel
        self.nivel += 1
        self.experiencia = 0
        print(f"¡{self.nombre} ha subido al nivel {self.nivel}!")

    def ganar_experiencia(self, cantidad):
        self.experiencia += cantidad
        if self.experiencia >= 100:
            self.experiencia -= 100
            # Mejoras aleatorias al subir nivel
            mejoras = {
                'fuerza': random.randint(1, 3),
                'inteligencia': random.randint(1, 3),
                'defensa': random.randint(1, 2),
                'vida': random.randint(10, 20)
            }
            self.subir_nivel(**mejoras)
            return True
        return False

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(f"💀 {self.nombre} ha muerto")

    def daño(self, enemigo):
        daño_base = self.fuerza - enemigo.defensa
        # Añadir variabilidad aleatoria (±10%)
        variacion = random.uniform(0.9, 1.1)
        daño_final = int(daño_base * variacion)

        # Daño mínimo de 1 si hay ataque exitoso
        if daño_base > 0:
            return max(1, daño_final)
        # Si la defensa es mayor que la fuerza, posibilidad de daño 0 o 1
        else:
            # 30% de probabilidad de hacer 1 punto de daño aunque la defensa sea alta
            return 1 if random.random() < 0.3 else 0

    def atacar(self, enemigo):
        if not self.esta_vivo():
            return

        daño = self.daño(enemigo)

        if daño > 0:
            # Posibilidad de crítico (5%)
            if random.random() < 0.05:
                daño *= 2
                print(f"🔥 ¡GOLPE CRÍTICO! {self.nombre} inflige {daño} puntos de daño a {enemigo.nombre}")
            else:
                print(f"⚔️ {self.nombre} ha realizado {daño} puntos de daño a {enemigo.nombre}")

            enemigo.vida -= daño
            enemigo.vida = max(0, enemigo.vida)  # No permitir vida negativa

            if enemigo.esta_vivo():
                print(f"  ❤️ Vida de {enemigo.nombre}: {enemigo.vida}/{enemigo.vida_maxima}")
            else:
                enemigo.morir()
                # Ganar experiencia al derrotar enemigo
                experiencia_ganada = random.randint(20, 40)
                if self.ganar_experiencia(experiencia_ganada):
                    print(f"✨ {self.nombre} gana {experiencia_ganada} XP y sube de nivel!")
                else:
                    print(f"✨ {self.nombre} gana {experiencia_ganada} XP")
        else:
            print(f"🛡️ {enemigo.nombre} ha bloqueado completamente el ataque de {self.nombre}")

    def curar(self, cantidad=None):
        if cantidad is None:
            cantidad = int(self.vida_maxima * 0.3)  # Curar 30% por defecto

        vida_anterior = self.vida
        self.vida = min(self.vida_maxima, self.vida + cantidad)
        curado = self.vida - vida_anterior

        if curado > 0:
            print(f"💚 {self.nombre} se ha curado {curado} puntos de vida")
            print(f"  ❤️ Vida actual: {self.vida}/{self.vida_maxima}")
        return curado


class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
        self.furia = 0  # Nueva mecánica: furia acumulable

    def cambiar_arma(self):
        print("\n🔪 Elige un arma:")
        print("1. Acero Valyrio (daño 8)")
        print("2. Matadragones (daño 10)")
        print("3. Espada del Caos (daño 12, 20% probabilidad de fallar)")

        try:
            opcion = int(input("Opción: "))
            if opcion == 1:
                self.espada = 8
                print("Has equipado el Acero Valyrio")
            elif opcion == 2:
                self.espada = 10
                print("Has equipado el Matadragones")
            elif opcion == 3:
                self.espada = 12
                print("Has equipado la Espada del Caos (¡peligrosa!)")
            else:
                print("Opción no válida, manteniendo arma actual")
        except:
            print("Entrada inválida, manteniendo arma actual")

    def atributos(self):
        super().atributos()
        print(f"  Espada: {self.espada}")
        print(f"  Furia: {self.furia}/100")

    def daño(self, enemigo):
        # El guerrero acumula furia al atacar
        self.furia = min(100, self.furia + random.randint(5, 15))

        # Si tiene furia máxima, puede hacer un ataque especial
        if self.furia >= 100 and random.random() < 0.5:
            return self._ataque_furia(enemigo)

        daño_base = self.fuerza * self.espada - enemigo.defensa

        # Verificar arma especial
        if self.espada == 12 and random.random() < 0.2:
            print(f"💢 ¡La Espada del Caos se vuelve incontrolable! {self.nombre} falla el ataque")
            return 0

        variacion = random.uniform(0.85, 1.15)
        daño_final = int(daño_base * variacion)

        return max(1, daño_final) if daño_base > 0 else (1 if random.random() < 0.4 else 0)

    def _ataque_furia(self, enemigo):
        self.furia = 0
        daño = int((self.fuerza * self.espada * 1.5) - enemigo.defensa)
        print(f"😡 ¡{self.nombre} entra en FURIA!")
        return max(5, daño)  # Daño mínimo garantizado en furia


class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro
        self.mana = 100  # Nueva mecánica: mana para hechizos
        self.mana_maximo = 100

    def atributos(self):
        super().atributos()
        print(f"  Libro: {self.libro}")
        print(f"  Maná: {self.mana}/{self.mana_maximo}")

    def daño(self, enemigo):
        # El mago usa inteligencia en lugar de fuerza
        daño_base = self.inteligencia * self.libro - enemigo.defensa

        # Consumir mana
        mana_cost = random.randint(5, 15)
        if self.mana >= mana_cost:
            self.mana -= mana_cost
            daño_base = int(daño_base * 1.2)  # Bonus por usar mana
        else:
            print(f"⚠️ {self.nombre} no tiene suficiente maná para potenciar el hechizo")

        variacion = random.uniform(0.8, 1.2)
        daño_final = int(daño_base * variacion)

        # Regenerar mana lentamente
        self.mana = min(self.mana_maximo, self.mana + random.randint(1, 3))

        return max(1, daño_final) if daño_base > 0 else (1 if random.random() < 0.3 else 0)

    def lanzar_hechizo(self, enemigo):
        if self.mana < 30:
            print(f"⚠️ {self.nombre} no tiene suficiente maná para un hechizo especial")
            return self.atacar(enemigo)

        print(f"\n🔮 {self.nombre} está preparando un hechizo...")
        print("1. Bola de Fuego (30 mana, daño alto)")
        print("2. Rayo Helado (25 mana, reduce defensa)")
        print("3. Drenar Vida (40 mana, daño y curación)")

        try:
            opcion = int(input("Elige hechizo: "))
            self.mana -= 30

            if opcion == 1:
                daño = int(self.inteligencia * 2 * random.uniform(0.9, 1.3))
                enemigo.vida -= daño
                print(f"🔥 ¡Bola de Fuego! {daño} puntos de daño")

            elif opcion == 2:
                daño = int(self.inteligencia * 1.5)
                enemigo.vida -= daño
                enemigo.defensa = max(0, enemigo.defensa - 2)
                print(f"❄️ ¡Rayo Helado! {daño} puntos de daño y reduce defensa")

            elif opcion == 3:
                daño = int(self.inteligencia * 1.8)
                enemigo.vida -= daño
                curacion = int(daño * 0.5)
                self.vida = min(self.vida_maxima, self.vida + curacion)
                print(f"💀 ¡Drenar Vida! {daño} puntos de daño y cura {curacion}")

            else:
                print("Hechizo fallido, ataque normal")
                return self.atacar(enemigo)

            if not enemigo.esta_vivo():
                enemigo.morir()

        except:
            print("Hechizo interrumpido, ataque normal")
            return self.atacar(enemigo)


def combate(jugador_1, jugador_2, turnos_maximos=20):
    print(f"\n{'=' * 50}")
    print(f"⚔️  COMBATE: {jugador_1.nombre} vs {jugador_2.nombre}  ⚔️")
    print(f"{'=' * 50}")

    turno = 1
    while jugador_1.esta_vivo() and jugador_2.esta_vivo() and turno <= turnos_maximos:
        print(f"\n{'─' * 30}")
        print(f"📊 TURNO {turno}")
        print(f"{'─' * 30}")

        # Personaje 1 decide acción
        print(f"\n▶️  Turno de {jugador_1.nombre}:")
        accion_1 = _elegir_accion(jugador_1)
        _ejecutar_accion(jugador_1, jugador_2, accion_1)

        if not jugador_2.esta_vivo():
            break

        # Personaje 2 decide acción
        print(f"\n▶️  Turno de {jugador_2.nombre}:")
        accion_2 = _elegir_accion(jugador_2)
        _ejecutar_accion(jugador_2, jugador_1, accion_2)

        turno += 1

    # Determinar resultado
    print(f"\n{'=' * 50}")
    print("🎯 FIN DEL COMBATE")
    print(f"{'=' * 50}")

    if not jugador_1.esta_vivo() and not jugador_2.esta_vivo():
        print("💀 ¡DOBLE KO! Ambos han caído en combate")
    elif not jugador_1.esta_vivo():
        print(f"🏆 ¡VICTORIA DE {jugador_2.nombre}!")
    elif not jugador_2.esta_vivo():
        print(f"🏆 ¡VICTORIA DE {jugador_1.nombre}!")
    else:
        print("⏱️  ¡TIEMPO AGOTADO! Combate empatado")

    # Mostrar estado final
    print("\nEstado final:")
    jugador_1.atributos()
    print()
    jugador_2.atributos()


def _elegir_accion(personaje):
    """Menú para elegir acción en el turno"""
    print("¿Qué quieres hacer?")
    print("1. Atacar")
    print("2. Curarse")

    if isinstance(personaje, Mago):
        print("3. Lanzar hechizo")
    elif isinstance(personaje, Guerrero):
        print("3. Cambiar arma")

    try:
        opcion = int(input("Elige (1-3): "))
        return opcion
    except:
        return 1  # Por defecto atacar


def _ejecutar_accion(atacante, defensor, accion):
    """Ejecuta la acción elegida"""
    if accion == 1:
        atacante.atacar(defensor)
    elif accion == 2:
        atacante.curar()
    elif accion == 3:
        if isinstance(atacante, Mago):
            atacante.lanzar_hechizo(defensor)
        elif isinstance(atacante, Guerrero):
            atacante.cambiar_arma()
    else:
        atacante.atacar(defensor)


def crear_personaje():
    """Crea un personaje personalizado"""
    print("\n🎮 CREACIÓN DE PERSONAJE")
    nombre = input("Nombre del personaje: ")

    print("\nElige una clase:")
    print("1. Guerrero (alta fuerza, baja inteligencia)")
    print("2. Mago (alta inteligencia, baja fuerza)")

    try:
        clase = int(input("Clase (1-2): "))

        if clase == 1:
            print("\nElige tu arma inicial:")
            print("1. Espada de Hierro (daño 5)")
            print("2. Hacha de Batalla (daño 6)")
            arma = int(input("Opción: "))
            espada = 5 if arma == 1 else 6

            return Guerrero(
                nombre=nombre,
                fuerza=random.randint(15, 20),
                inteligencia=random.randint(5, 10),
                defensa=random.randint(3, 6),
                vida=random.randint(90, 110),
                espada=espada
            )
        else:
            print("\nElige tu libro de hechizos:")
            print("1. Grimorio Elemental (poder 4)")
            print("2. Tome de los Ancestros (poder 5)")
            libro_op = int(input("Opción: "))
            libro = 4 if libro_op == 1 else 5

            return Mago(
                nombre=nombre,
                fuerza=random.randint(5, 10),
                inteligencia=random.randint(15, 20),
                defensa=random.randint(2, 5),
                vida=random.randint(80, 100),
                libro=libro
            )
    except:
        print("Error en creación, usando valores por defecto")
        return Guerrero(nombre, 18, 8, 4, 100, 5)


# Ejemplo de uso mejorado
if __name__ == "__main__":
    print("⚔️  ARENA DE COMBATE RPG ⚔️")

    # Crear personajes de forma interactiva
    print("\n--- Personaje 1 ---")
    p1 = crear_personaje()

    print("\n--- Personaje 2 ---")
    print("¿Crear manualmente o generar automático?")
    print("1. Crear manualmente")
    print("2. Generar automático")

    try:
        opcion = int(input("Opción: "))
        if opcion == 1:
            p2 = crear_personaje()
        else:
            # Generar enemigo aleatorio
            if random.choice([True, False]):
                p2 = Guerrero(
                    nombre="Orco Salvaje",
                    fuerza=random.randint(16, 22),
                    inteligencia=random.randint(3, 8),
                    defensa=random.randint(4, 7),
                    vida=random.randint(95, 115),
                    espada=random.choice([5, 6, 7])
                )
            else:
                p2 = Mago(
                    nombre="Hechicero Oscuro",
                    fuerza=random.randint(4, 9),
                    inteligencia=random.randint(16, 22),
                    defensa=random.randint(1, 4),
                    vida=random.randint(75, 95),
                    libro=random.choice([4, 5, 6])
                )
    except:
        p2 = Guerrero("Enemigo", 18, 8, 4, 100, 5)

    # Mostrar los personajes
    print("\n" + "=" * 50)
    print("COMBATIENTES:")
    print("=" * 50)
    p1.atributos()
    print()
    p2.atributos()

    # Iniciar combate
    input("\nPresiona Enter para comenzar el combate...")
    combate(p1, p2)