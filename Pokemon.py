from math import sqrt
import random
from moves import get_move

IV = 31
EV = 250
LEVEL = 50


class Tipo:
    tipo: str

    def __init__(self, tipo):
        self.tipo = tipo

    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        self.tipo = tipo


class Movimientos:
    movimientos: list()

    def __init__(self, movimientos):
        self.movimientos = movimientos

    def getMovimientos(self):
        return self.movimientos

    def setMovimientos(self, movimientos):
        self.movimientos = movimientos

    def getMovimientoPorIndice(self, index):
        return self.movimientos[index]


class Stats:
    HP: int
    DEF: int
    SDEF: int
    ATTK: int
    SATTK: int
    SPE: int
    EFECTIVIDAD: list()

    def efectividadPorTipo(self, tipoAttak, tipoDef):
        valores = self.EFECTIVIDAD[0]
        posAtak = 0
        posDef = 0
        posAtak = valores.index(tipoAttak)
        posDef = valores.index(tipoDef)
        efectividad = self.EFECTIVIDAD[posDef][posAtak]
        return efectividad

    def statCalc(self, base):
        return ((((base+IV)*2)+(sqrt(EV)/4))*LEVEL/100)+5

    def getHp(self):
        return self.HP

    def setHp(self, base):
        hp = ((((base+IV)*2)+(sqrt(EV)/4))*LEVEL/100)+LEVEL + 10
        self.HP = hp

    def getDef(self):
        return self.DEF

    def setDef(self, base):
        value = self.statCalc(base)
        self.DEF = value

    def getSDef(self):
        return self.SDEF

    def setSDef(self, base):
        value = self.statCalc(base)
        self.SDEF = value

    def getAttk(self):
        return self.ATTK

    def setAttk(self, base):
        value = self.statCalc(base)
        self.ATTK = value

    def getSattk(self):
        return self.ATTK

    def setSattk(self, base):
        value = self.statCalc(base)
        self.SATTK = value

    def getSpe(self):
        return self.SPE

    def setSpe(self, base):
        value = self.statCalc(base)
        self.SPE = value

    def getEfectividad(self):
        return self.EFECTIVIDAD

    def setEfectividad(self, efectividad):
        self.EFECTIVIDAD = efectividad

    def getStatMov(self, movimiento):
        movimiento_stats = get_move(movimiento)
        return movimiento_stats[1]


class Pokemon(Tipo, Movimientos, Stats):
    nombre: str
    puntos_vida: int
    puntos_de_ataque_fisico_base: int
    puntos_de_defensa_fisica_base: int
    puntos_de_ataque_especial_base: int
    puntos_de_defensa_especial_base: int
    puntos_de_velocidad_base: int

    def __str__(self):
        return(f"\nNombre del Pokémon seleccionado: {self.nombre.capitalize()}")

    def __init__(self, nombre, puntos_vida, puntos_de_ataque_fisico_base, puntos_de_defensa_fisica_base, puntos_de_ataque_especial_base, puntos_de_defensa_especial_base, puntos_de_velocidad_base):
        self.nombre = nombre
        self.puntos_vida = puntos_vida
        self.puntos_de_ataque_fisico_base = puntos_de_ataque_fisico_base
        self.puntos_de_defensa_fisica_base = puntos_de_defensa_fisica_base
        self.puntos_de_ataque_especial_base = puntos_de_ataque_especial_base
        self.puntos_de_defensa_especial_base = puntos_de_defensa_especial_base
        self.puntos_de_velocidad_base = puntos_de_velocidad_base

    def getNombre(self):
        return self.nombre

    def getPuntosVida(self):
        return self.puntos_vida

    def getPuntosAtaqueFisicoBase(self):
        return self.puntos_de_ataque_fisico_base

    def getpuntosDefensaFisicoBase(self):
        return self.puntos_de_defensa_fisica_base

    def getPuntosAtaqueEspecialBase(self):
        return self.puntos_de_ataque_especial_base

    def getPuntosDefensaEspecialBase(self):
        return self.puntos_de_defensa_especial_base

    def getPuntosVelocidadBase(self):
        return self.puntos_de_velocidad_base

    def setNombre(self, nombre):
        self.nombre = nombre

    def setPuntosVida(self, puntos_vida):
        self.puntos_vida = puntos_vida

    def setPuntosAtaqueFisicoBase(self, puntos_de_ataque_fisico_base):
        self.puntos_de_ataque_fisico_base = puntos_de_ataque_fisico_base

    def setpuntosDefensaFisicoBase(self, puntos_de_defensa_fisica_base):
        self.puntos_de_defensa_fisica_base = puntos_de_defensa_fisica_base

    def setPuntosAtaqueEspecialBase(self, puntos_de_ataque_especial_base):
        self.puntos_de_ataque_especial_base = puntos_de_ataque_especial_base

    def setPuntosDefensaEspecialBase(self, puntos_de_defensa_especial_base):
        self.puntos_de_defensa_especial_base = puntos_de_defensa_especial_base

    def setPuntosVelocidadBase(self, puntos_de_velocidad_base):
        self.puntos_de_velocidad_base = puntos_de_velocidad_base

    def getModifer(self,  enemigoTipo):
        STAB = 1.2
        TYPE = self.efectividadPorTipo(self.tipo, enemigoTipo)
        rand_number = random.randint(0.85, 1)
        if(enemigoTipo != self.tipo):
            STAB = 1
        modifier = TYPE * STAB * rand_number * 1
        return modifier

    def calcDamage(self, level, power, a, d):
        damage = (((((2 * level)/5) + 2) * power *
                  (a/d) / 50) + 2) * self.getModifer()
        return damage

    def imprimirEstadisticas(self):
        print("Estadísticas base del Pokémon: ")
        print("\t- HP = ", self.getPuntosVida())
        print("\t- Ataque = ", self.getPuntosAtaqueFisicoBase())
        print("\t- Defensa = ", self.getpuntosDefensaFisicoBase())
        print("\t- Ataque especial = ", self.getPuntosAtaqueEspecialBase())
        print("\t- Defensa especial = ", self.getPuntosDefensaEspecialBase())
        print("\t- Velocidad = ", self.getPuntosVelocidadBase())

    def mostrarMovimientos(self):
        print("\nMovimientos que puede aprender el pokémon: ")
        for item in range(0, len(self.movimientos)):
            print(f"{item}   -    {self.movimientos[item]}")
