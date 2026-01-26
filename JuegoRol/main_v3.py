import random
import os
import time
from dataclasses import dataclass
from typing import Optional


@dataclass
class EstadisticasCombate:
    daño_total: int = 0
    curacion_total: int = 0
    criticos: int = 0
    fallos: int = 0
    hechizos_usados: int = 0

    def mostrar(self):
        print(f"  📊 Daño total: {self.daño_total}")
        print(f"  💚 Curación total: {self.curacion_total}")
        print(f"  🔥 Críticos: {self.criticos}")
        print(f"  ❌ Fallos: {self.fallos}")
        if self.hechizos_usados > 0:
            print(f"  🔮 Hechizos: {self.hechizos_usados}")


class Interfaz:
    @staticmethod
    def limpiar_pantalla():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def mostrar_titulo(titulo):
        print(f"\n{'═' * 60}")
        print(f"║{titulo:^58}║")
        print(f"{'═' * 60}")

    @staticmethod
    def mostrar_barra_vida(nombre, vida_actual, vida_maxima, ancho=30):
        porcentaje = vida_actual / vida_maxima
        barras = int(porcentaje * ancho)
        color = "🟩" if porcentaje > 0.5 else "🟨" if porcentaje > 0.25 else "🟥"

        barra = f"{color * barras}{'⬛' * (ancho - barras)}"
        print(f"{nombre:15} {barra} {vida_actual:3}/{vida_maxima:3} ({porcentaje * 100:.0f}%)")

    @staticmethod
    def mostrar_barra_mana(nombre, mana_actual, mana_maximo, ancho=20):
        if mana_maximo == 0:
            return
        porcentaje = mana_actual / mana_maximo
        barras = int(porcentaje * ancho)

        barra = f"🔵" * barras + f"⚫" * (ancho - barras)
        print(f"{nombre:15} {barra} {mana_actual:3}/{mana_maximo:3}")

    @staticmethod
    def mostrar_estado_combate(jugador1, jugador2):
        Interfaz.limpiar_pantalla()
        Interfaz.mostrar_titulo("⚔️ ESTADO DEL COMBATE ⚔️")

        print("\n❤️  VIDA:")
        Interfaz.mostrar_barra_vida(jugador1.nombre, jugador1.vida, jugador1.vida_maxima)
        Interfaz.mostrar_barra_vida(jugador2.nombre, jugador2.vida, jugador2.vida_maxima)

        print("\n🔮 RECURSOS:")
        if hasattr(jugador1, 'mana'):
            Interfaz.mostrar_barra_mana(jugador1.nombre, jugador1.mana, jugador1.mana_maximo)
        if hasattr(jugador2, 'mana'):
            Interfaz.mostrar_barra_mana(jugador2.nombre, jugador2.mana, jugador2.mana_maximo)
        if hasattr(jugador1, 'furia') and jugador1.furia > 0:
            print(f"{jugador1.nombre:15} {'😡' * int(jugador1.furia / 20)} Furia: {jugador1.furia}/100")
        if hasattr(jugador2, 'furia') and jugador2.furia > 0:
            print(f"{jugador2.nombre:15} {'😡' * int(jugador2.furia / 20)} Furia: {jugador2.furia}/100")

        print(f"\n📊 NIVEL: {jugador1.nombre}: {jugador1.nivel}  |  {jugador2.nombre}: {jugador2.nivel}")
        print(f"✨ XP: {jugador1.nombre}: {jugador1.experiencia}/100  |  {jugador2.nombre}: {jugador2.experiencia}/100")
        print(f"{'─' * 60}")


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
        self.estadisticas = EstadisticasCombate()
        self.efectos = []  # Para efectos temporales

    def agregar_efecto(self, efecto):
        self.efectos.append(efecto)

    def actualizar_efectos(self):
        for efecto in self.efectos[:]:
            efecto.turnos_restantes -= 1
            if efecto.turnos_restantes <= 0:
                self.efectos.remove(efecto)
                print(f"  ⏰ {efecto.nombre} ha terminado")

    def mostrar_efectos(self):
        if self.efectos:
            print(f"  ⚡ Efectos activos: {', '.join([e.nombre for e in self.efectos])}")

    def atributos_detallados(self):
        print(f"\n📋 ESTADÍSTICAS DE {self.nombre.upper()}")
        print(f"{'─' * 40}")
        print(f"  Nivel: {self.nivel}")
        print(f"  Vida: {self.vida}/{self.vida_maxima}")
        print(f"  Fuerza: {self.fuerza}")
        print(f"  Inteligencia: {self.inteligencia}")
        print(f"  Defensa: {self.defensa}")
        print(f"  XP: {self.experiencia}/100")

        # Mostrar modificadores de efectos
        for efecto in self.efectos:
            print(f"  {efecto.nombre}: {efecto.descripcion} ({efecto.turnos_restantes} turnos)")

        print(f"\n📊 ESTADÍSTICAS DE COMBATE:")
        self.estadisticas.mostrar()

    def subir_nivel(self, mejoras):
        self.fuerza += mejoras.get('fuerza', 0)
        self.inteligencia += mejoras.get('inteligencia', 0)
        self.defensa += mejoras.get('defensa', 0)
        self.vida_maxima += mejoras.get('vida', 0)
        self.vida = self.vida_maxima
        self.nivel += 1
        self.experiencia = 0

        print(f"\n🎉 ¡{self.nombre} ha subido al nivel {self.nivel}!")
        print(f"   +{mejoras.get('fuerza', 0)} Fuerza")
        print(f"   +{mejoras.get('inteligencia', 0)} Inteligencia")
        print(f"   +{mejoras.get('defensa', 0)} Defensa")
        print(f"   +{mejoras.get('vida', 0)} Vida máxima")
        time.sleep(1.5)

    def ganar_experiencia(self, cantidad):
        self.experiencia += cantidad
        if self.experiencia >= 100:
            mejoras = {
                'fuerza': random.randint(1, 3),
                'inteligencia': random.randint(1, 3),
                'defensa': random.randint(1, 2),
                'vida': random.randint(10, 20)
            }
            self.subir_nivel(mejoras)
            return True
        return False

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(f"\n💀 {self.nombre} ha sido derrotado!")
        time.sleep(1)

    def daño(self, enemigo):
        daño_base = self.fuerza - enemigo.defensa
        variacion = random.uniform(0.9, 1.1)
        daño_final = int(daño_base * variacion)

        # Daño mínimo de 1 si el ataque es exitoso
        if daño_base > 0:
            return max(1, daño_final)
        # Si la defensa es muy alta, posibilidad de daño reducido
        else:
            return 1 if random.random() < 0.3 else 0

    def atacar(self, enemigo):
        if not self.esta_vivo():
            return

        self.actualizar_efectos()
        enemigo.actualizar_efectos()

        daño = self.daño(enemigo)
        es_critico = False

        if daño > 0:
            # Probabilidad de crítico (5% base)
            prob_critico = 0.05
            if random.random() < prob_critico:
                daño = int(daño * 1.5)
                es_critico = True
                self.estadisticas.criticos += 1

            enemigo.vida -= daño
            enemigo.vida = max(0, enemigo.vida)
            self.estadisticas.daño_total += daño

            if es_critico:
                print(f"\n🔥 ¡GOLPE CRÍTICO! {self.nombre} inflige {daño} de daño")
            else:
                print(f"\n⚔️ {self.nombre} ataca a {enemigo.nombre} por {daño} de daño")

            if enemigo.esta_vivo():
                print(f"   ❤️ {enemigo.nombre}: {enemigo.vida}/{enemigo.vida_maxima}")
            else:
                enemigo.morir()
                experiencia_ganada = random.randint(20, 40)
                if self.ganar_experiencia(experiencia_ganada):
                    print(f"   ✨ ¡Ganas {experiencia_ganada} XP y subes de nivel!")
                else:
                    print(f"   ✨ Ganas {experiencia_ganada} XP")
        else:
            print(f"\n🛡️ {enemigo.nombre} bloquea completamente el ataque")
            self.estadisticas.fallos += 1

        time.sleep(1)

    def curar(self, cantidad=None):
        if cantidad is None:
            cantidad = int(self.vida_maxima * 0.3)

        vida_anterior = self.vida
        self.vida = min(self.vida_maxima, self.vida + cantidad)
        curado = self.vida - vida_anterior

        if curado > 0:
            print(f"\n💚 {self.nombre} se cura {curado} puntos de vida")
            print(f"   ❤️ Vida: {self.vida}/{self.vida_maxima}")
            self.estadisticas.curacion_total += curado
        else:
            print(f"\n⚠️ {self.nombre} ya tiene la vida al máximo")

        time.sleep(1)
        return curado


class Efecto:
    def __init__(self, nombre, descripcion, turnos):
        self.nombre = nombre
        self.descripcion = descripcion
        self.turnos_restantes = turnos


class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
        self.furia = 0
        self.armas_disponibles = {
            'Acero Valyrio': 8,
            'Matadragones': 10,
            'Espada del Caos': 12,
            'Mandoble Pesado': 9
        }
        self.arma_actual = 'Acero Valyrio' if espada == 8 else 'Matadragones'

    def cambiar_arma(self):
        print(f"\n🔪 {self.nombre} elige un arma:")
        armas = list(self.armas_disponibles.keys())

        for i, arma in enumerate(armas, 1):
            daño = self.armas_disponibles[arma]
            print(f"  {i}. {arma} (Daño: {daño})")
            if arma == 'Espada del Caos':
                print("     ⚠️  20% probabilidad de fallar")
            elif arma == 'Mandoble Pesado':
                print("     🐌 -10% velocidad de ataque")

        try:
            opcion = int(input("\nElige arma: ")) - 1
            if 0 <= opcion < len(armas):
                self.arma_actual = armas[opcion]
                self.espada = self.armas_disponibles[self.arma_actual]
                print(f"\n✅ Equipas {self.arma_actual}")
            else:
                print("\n⚠️ Opción inválida")
        except:
            print("\n⚠️ Entrada inválida")

        time.sleep(1)

    def daño(self, enemigo):
        # Acumular furia
        self.furia = min(100, self.furia + random.randint(5, 15))

        # Ataque de furia
        if self.furia >= 100:
            return self._ataque_furia(enemigo)

        # Penalización por arma pesada
        multiplicador = 1.0
        if self.arma_actual == 'Mandoble Pesado' and random.random() < 0.1:
            print(f"  🐌 El mandoble es muy pesado, pierdes un turno")
            return 0

        # Fallo con Espada del Caos
        if self.arma_actual == 'Espada del Caos' and random.random() < 0.2:
            print(f"  💢 La Espada del Caos se rebela contra ti")
            return 0

        daño_base = self.fuerza * self.espada - enemigo.defensa
        variacion = random.uniform(0.85, 1.15)
        daño_final = int(daño_base * variacion * multiplicador)

        return max(1, daño_final) if daño_base > 0 else (1 if random.random() < 0.4 else 0)

    def _ataque_furia(self, enemigo):
        self.furia = 0
        daño = int((self.fuerza * self.espada * 1.8) - enemigo.defensa)
        print(f"\n😡 ¡{self.nombre} entra en FURIA DESCONTROLADA!")
        # Aplicar efecto de sangrado al enemigo
        enemigo.agregar_efecto(Efecto("Sangrado", "Pierde 3 de vida por turno", 3))
        return max(8, daño)

    def mostrar_recursos(self):
        if self.furia > 0:
            print(f"  😡 Furia: [{self.furia}/100]")


class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro
        self.mana_maximo = 100
        self.mana = self.mana_maximo
        self.hechizos = {
            'Bola de Fuego': {'costo': 30, 'descripcion': 'Daño alto'},
            'Rayo Helado': {'costo': 25, 'descripcion': 'Reduce defensa'},
            'Drenar Vida': {'costo': 40, 'descripcion': 'Daño y curación'},
            'Escudo Arcano': {'costo': 20, 'descripcion': 'Aumenta defensa'},
            'Tormenta Eléctrica': {'costo': 50, 'descripcion': 'Daño área'}
        }

    def mostrar_mana(self):
        porcentaje = self.mana / self.mana_maximo
        barras = int(porcentaje * 20)
        return f"[{'█' * barras}{'░' * (20 - barras)}] {self.mana}/{self.mana_maximo}"

    def regenerar_mana(self):
        regeneracion = random.randint(5, 10)
        self.mana = min(self.mana_maximo, self.mana + regeneracion)

    def lanzar_hechizo(self, enemigo=None):
        print(f"\n🔮 {self.nombre} prepara un hechizo")
        print(f"   Maná disponible: {self.mostrar_mana()}")
        print(f"\nHechizos disponibles:")

        hechizos_lista = list(self.hechizos.keys())
        for i, hechizo in enumerate(hechizos_lista, 1):
            info = self.hechizos[hechizo]
            puede_usar = self.mana >= info['costo']
            indicador = "✅" if puede_usar else "❌"
            print(f"  {i}. {hechizo} ({info['costo']} mana) {indicador}")
            print(f"     {info['descripcion']}")

        try:
            opcion = int(input("\nElige hechizo (0 para cancelar): "))
            if opcion == 0:
                return False

            if 1 <= opcion <= len(hechizos_lista):
                hechizo = hechizos_lista[opcion - 1]
                costo = self.hechizos[hechizo]['costo']

                if self.mana >= costo:
                    self.mana -= costo
                    self._ejecutar_hechizo(hechizo, enemigo)
                    self.estadisticas.hechizos_usados += 1
                    return True
                else:
                    print(f"\n⚠️ No tienes suficiente maná para {hechizo}")
                    time.sleep(1)
                    return False
            else:
                print("\n⚠️ Hechizo no válido")
                time.sleep(1)
                return False

        except:
            print("\n⚠️ Entrada inválida")
            time.sleep(1)
            return False

    def _ejecutar_hechizo(self, hechizo, enemigo):
        if hechizo == 'Bola de Fuego':
            daño = int(self.inteligencia * 2.5 * random.uniform(0.9, 1.3))
            enemigo.vida -= daño
            enemigo.agregar_efecto(Efecto("Quemadura", "Daño adicional por fuego", 2))
            print(f"\n🔥 ¡BOLA DE FUEGO! {daño} puntos de daño")
            print(f"   📛 {enemigo.nombre} sufre quemaduras")

        elif hechizo == 'Rayo Helado':
            daño = int(self.inteligencia * 1.8)
            enemigo.vida -= daño
            enemigo.defensa = max(0, enemigo.defensa - 3)
            enemigo.agregar_efecto(Efecto("Congelado", "Movimiento reducido", 2))
            print(f"\n❄️ ¡RAYO HELADO! {daño} puntos de daño")
            print(f"   🛡️ Defensa de {enemigo.nombre} reducida")

        elif hechizo == 'Drenar Vida':
            daño = int(self.inteligencia * 2.2)
            enemigo.vida -= daño
            curacion = int(daño * 0.6)
            self.vida = min(self.vida_maxima, self.vida + curacion)
            print(f"\n💀 ¡DRENAR VIDA! {daño} puntos de daño")
            print(f"   💚 {self.nombre} se cura {curacion} puntos")

        elif hechizo == 'Escudo Arcano':
            self.defensa += 5
            self.agregar_efecto(Efecto("Escudo Arcano", "+5 defensa", 3))
            print(f"\n🛡️ ¡ESCUDO ARCANO! Defensa aumentada por 3 turnos")

        elif hechizo == 'Tormenta Eléctrica':
            daño = int(self.inteligencia * 3.0 * random.uniform(0.8, 1.2))
            enemigo.vida -= daño
            if random.random() < 0.4:  # 40% de aturdir
                enemigo.agregar_efecto(Efecto("Aturdido", "Pierde próximo turno", 1))
                print(f"\n⚡ ¡TORMENTA ELÉCTRICA! {daño} puntos de daño")
                print(f"   ⚡ {enemigo.nombre} queda aturdido")
            else:
                print(f"\n⚡ ¡TORMENTA ELÉCTRICA! {daño} puntos de daño")

        self.estadisticas.daño_total += daño if 'daño' in locals() else 0
        time.sleep(1.5)

    def daño(self, enemigo):
        # Regenerar mana automáticamente
        self.regenerar_mana()

        # Ataque mágico básico (sin costo de mana)
        daño_base = self.inteligencia * self.libro - enemigo.defensa
        variacion = random.uniform(0.8, 1.2)
        daño_final = int(daño_base * variacion)

        return max(1, daño_final) if daño_base > 0 else (1 if random.random() < 0.3 else 0)


class MenuCombate:
    @staticmethod
    def mostrar_acciones(personaje, enemigo):
        print(f"\n🎮 TURNO DE {personaje.nombre}")
        print(f"{'─' * 40}")

        # Mostrar estado rápido
        print(f"❤️  Vida: {personaje.vida}/{personaje.vida_maxima}")
        if hasattr(personaje, 'mana'):
            print(f"🔮 Maná: {personaje.mostrar_mana()}")
        if hasattr(personaje, 'furia'):
            print(f"😡 Furia: {personaje.furia}/100")

        personaje.mostrar_efectos()
        print(f"\n🎯 Enemigo: {enemigo.nombre} ({enemigo.vida}/{enemigo.vida_maxima} HP)")

        print(f"\n📋 ACCIONES DISPONIBLES:")
        print(f"  1. ⚔️  Atacar")
        print(f"  2. 💚 Curarse")

        if isinstance(personaje, Mago):
            print(f"  3. 🔮 Lanzar hechizo")
        elif isinstance(personaje, Guerrero):
            print(f"  3. 🔪 Cambiar arma")

        print(f"  4. 📊 Ver estadísticas")
        print(f"  5. ⏭️  Pasar turno")

        try:
            opcion = int(input("\nElige acción: "))
            return opcion
        except:
            return 1

    @staticmethod
    def ejecutar_accion(personaje, enemigo, accion):
        if accion == 1:
            personaje.atacar(enemigo)
        elif accion == 2:
            personaje.curar()
        elif accion == 3:
            if isinstance(personaje, Mago):
                if not personaje.lanzar_hechizo(enemigo):
                    return False  # Cancela el hechizo
            elif isinstance(personaje, Guerrero):
                personaje.cambiar_arma()
        elif accion == 4:
            personaje.atributos_detallados()
            input("\nPresiona Enter para continuar...")
            return False  # No consume turno
        elif accion == 5:
            print(f"\n⏭️ {personaje.nombre} pasa el turno")
            time.sleep(1)
        else:
            print(f"\n⚠️ Acción no válida, atacas por defecto")
            personaje.atacar(enemigo)

        return True


def combate(jugador1, jugador2):
    turno = 1
    max_turnos = 30

    print(f"\n🎲 ¡COMIENZA EL COMBATE!")
    print(f"   {jugador1.nombre} vs {jugador2.nombre}")
    time.sleep(2)

    while (jugador1.esta_vivo() and jugador2.esta_vivo()
           and turno <= max_turnos):

        Interfaz.mostrar_estado_combate(jugador1, jugador2)
        print(f"\n📅 TURNO {turno}/{max_turnos}")

        # Turno jugador 1
        if jugador1.esta_vivo():
            accion_valida = False
            while not accion_valida:
                accion = MenuCombate.mostrar_acciones(jugador1, jugador2)
                accion_valida = MenuCombate.ejecutar_accion(jugador1, jugador2, accion)

                if accion_valida:
                    # Verificar si el enemigo murió durante la acción
                    if not jugador2.esta_vivo():
                        break

        # Turno jugador 2 (podría ser IA o segundo jugador)
        if jugador2.esta_vivo():
            # IA simple para el segundo personaje
            accion = _decidir_accion_ia(jugador2, jugador1)
            MenuCombate.ejecutar_accion(jugador2, jugador1, accion)

        turno += 1

    # Mostrar resultado final
    Interfaz.mostrar_estado_combate(jugador1, jugador2)
    print(f"\n{'=' * 60}")
    print("🎯 RESULTADO FINAL")
    print(f"{'=' * 60}")

    if not jugador1.esta_vivo() and not jugador2.esta_vivo():
        print("💀 ¡DOBLE ELIMINACIÓN! Ambos combatientes han caído")
    elif not jugador1.esta_vivo():
        print(f"🏆 ¡VICTORIA DE {jugador2.nombre}!")
    elif not jugador2.esta_vivo():
        print(f"🏆 ¡VICTORIA DE {jugador1.nombre}!")
    else:
        print("⏱️  ¡TIEMPO AGOTADO! Empate por límite de turnos")

    print(f"\n📊 ESTADÍSTICAS FINALES:")
    jugador1.atributos_detallados()
    print()
    jugador2.atributos_detallados()


def _decidir_accion_ia(personaje, enemigo):
    """IA simple para decidir acciones del enemigo"""
    # Prioridades según tipo de personaje
    if isinstance(personaje, Mago):
        if personaje.mana >= 40 and enemigo.vida > enemigo.vida_maxima * 0.5:
            return 3  # Lanzar hechizo
        elif personaje.vida < personaje.vida_maxima * 0.4:
            return 2  # Curarse
        else:
            return 1  # Atacar

    elif isinstance(personaje, Guerrero):
        if personaje.vida < personaje.vida_maxima * 0.3:
            return 2  # Curarse
        elif personaje.furia >= 80:
            return 1  # Atacar para activar furia
        elif random.random() < 0.2:  # 20% de cambiar arma
            return 3
        else:
            return 1

    else:
        # Personaje genérico
        if personaje.vida < personaje.vida_maxima * 0.4:
            return 2
        else:
            return 1


def mostrar_menu_principal():
    Interfaz.limpiar_pantalla()
    Interfaz.mostrar_titulo("⚔️ ARENA DE COMBATE RPG ⚔️")

    print("\n🎮 OPCIONES PRINCIPALES:")
    print("  1. 🆕 Nuevo combate (1 vs 1)")
    print("  2. 👤 Crear personaje personalizado")
    print("  3. 🎲 Combate aleatorio")
    print("  4. 📊 Ver tutorial")
    print("  5. 🚪 Salir")

    try:
        opcion = int(input("\nElige opción: "))
        return opcion
    except:
        return 1


def crear_personaje_interactivo(numero=1):
    Interfaz.limpiar_pantalla()
    Interfaz.mostrar_titulo(f"👤 CREACIÓN PERSONAJE {numero}")

    nombre = input(f"\n¿Nombre del personaje {numero}?: ")

    print(f"\n🎭 Clases disponibles para {nombre}:")
    print("  1. 🗡️  Guerrero - Alta fuerza, vida resistente")
    print("  2. 🔮 Mago - Alta inteligencia, hechizos poderosos")
    print("  3. 🎲 Aleatorio - Elige por mí")

    try:
        clase_opcion = int(input("\nElige clase: "))

        if clase_opcion == 3:
            clase_opcion = random.randint(1, 2)

        if clase_opcion == 1:  # Guerrero
            print(f"\n⚔️ {nombre} será un Guerrero")
            print("\n🔪 Elige tu arma inicial:")
            print("  1. Acero Valyrio (Daño: 8, Balanceada)")
            print("  2. Matadragones (Daño: 10, Ofensiva)")

            arma_opcion = int(input("\nElige arma: "))
            espada = 8 if arma_opcion == 1 else 10

            return Guerrero(
                nombre=nombre,
                fuerza=random.randint(16, 20),
                inteligencia=random.randint(6, 10),
                defensa=random.randint(4, 7),
                vida=random.randint(95, 115),
                espada=espada
            )

        elif clase_opcion == 2:  # Mago
            print(f"\n🔮 {nombre} será un Mago")
            print("\n📖 Elige tu libro de hechizos:")
            print("  1. Grimorio Elemental (Poder: 4, Versátil)")
            print("  2. Tome de los Ancestros (Poder: 5, Poderoso)")

            libro_opcion = int(input("\nElige libro: "))
            libro = 4 if libro_opcion == 1 else 5

            return Mago(
                nombre=nombre,
                fuerza=random.randint(5, 9),
                inteligencia=random.randint(16, 20),
                defensa=random.randint(2, 5),
                vida=random.randint(80, 100),
                libro=libro
            )

    except:
        print("\n⚠️ Error en creación, usando valores por defecto")
        return Guerrero(nombre, 18, 8, 4, 100, 8)


# Programa principal
if __name__ == "__main__":
    while True:
        opcion = mostrar_menu_principal()

        if opcion == 1:  # Nuevo combate 1vs1
            p1 = crear_personaje_interactivo(1)
            p2 = crear_personaje_interactivo(2)

            print(f"\n{'═' * 60}")
            print("⚔️  LOS COMBATIENTES:")
            print(f"{'═' * 60}")
            p1.atributos_detallados()
            print()
            p2.atributos_detallados()

            input("\n🎬 Presiona Enter para comenzar el combate...")
            combate(p1, p2)

            input("\n🏁 Presiona Enter para volver al menú principal...")

        elif opcion == 2:  # Solo crear personaje
            p = crear_personaje_interactivo()
            p.atributos_detallados()
            input("\n👤 Presiona Enter para continuar...")

        elif opcion == 3:  # Combate aleatorio
            nombres_guerreros = ["Guts", "Kratos", "Artorias", "Garen", "Darius"]
            nombres_magos = ["Gandalf", "Merlín", "Vivi", "Yennefer", "Gwydion"]

            if random.choice([True, False]):
                p1 = Guerrero(
                    nombre=random.choice(nombres_guerreros),
                    fuerza=random.randint(15, 22),
                    inteligencia=random.randint(5, 10),
                    defensa=random.randint(3, 7),
                    vida=random.randint(90, 120),
                    espada=random.choice([8, 10, 12])
                )
            else:
                p1 = Mago(
                    nombre=random.choice(nombres_magos),
                    fuerza=random.randint(4, 9),
                    inteligencia=random.randint(15, 22),
                    defensa=random.randint(2, 5),
                    vida=random.randint(75, 100),
                    libro=random.choice([4, 5, 6])
                )

            if random.choice([True, False]):
                p2 = Guerrero(
                    nombre=random.choice(nombres_guerreros),
                    fuerza=random.randint(15, 22),
                    inteligencia=random.randint(5, 10),
                    defensa=random.randint(3, 7),
                    vida=random.randint(90, 120),
                    espada=random.choice([8, 10, 12])
                )
            else:
                p2 = Mago(
                    nombre=random.choice(nombres_magos),
                    fuerza=random.randint(4, 9),
                    inteligencia=random.randint(15, 22),
                    defensa=random.randint(2, 5),
                    vida=random.randint(75, 100),
                    libro=random.choice([4, 5, 6])
                )

            print(f"\n🎲 ¡COMBATE ALEATORIO GENERADO!")
            print(f"   {p1.nombre} vs {p2.nombre}")
            time.sleep(2)
            combate(p1, p2)
            input("\n🏁 Presiona Enter para continuar...")

        elif opcion == 4:  # Tutorial
            Interfaz.limpiar_pantalla()
            Interfaz.mostrar_titulo("📚 TUTORIAL")
            print("\n🎯 OBJETIVO:")
            print("   Derrotar al oponente reduciendo su vida a 0")

            print("\n⚔️ ACCIONES DISPONIBLES:")
            print("   1. Atacar - Inflige daño basado en tu fuerza")
            print("   2. Curar - Recupera parte de tu vida")
            print("   3. Habilidad de clase - Especial según tu clase")

            print("\n🎭 CLASES:")
            print("   🗡️  GUERRERO:")
            print("     - Alta fuerza y vida")
            print("     - Acumula furia para ataques especiales")
            print("     - Puede cambiar armas")

            print("\n   🔮 MAGO:")
            print("     - Alta inteligencia")
            print("     - Usa maná para hechizos")
            print("     - Efectos especiales (quemar, congelar, etc.)")

            print("\n📊 INTERFAZ:")
            print("   - Barras de vida y maná en tiempo real")
            print("   - Efectos activos visibles")
            print("   - Estadísticas detalladas disponibles")

            input("\n📖 Presiona Enter para volver al menú...")

        elif opcion == 5:  # Salir
            print("\n👋 ¡Gracias por jugar!")
            break

        else:
            print("\n⚠️ Opción no válida")
            time.sleep(1)