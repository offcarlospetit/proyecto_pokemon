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
    mov: str
    tipoMov: str
    power: int
    categoria: str

    def efectividadPorTipo(self, tipoAttak, tipoDef):
        valores = self.EFECTIVIDAD[0]
        posAtak = 0
        posDef = 0
        posAtak = valores.index(tipoAttak)
        posDef = valores.index(tipoDef)
        efectividad = self.EFECTIVIDAD[posDef][posAtak]
        return efectividad

    def statCalc(self, base):
        value = ((((int(base)+IV)*2+((sqrt(EV)/4)))*50)/100)+5
        return value

    def getHp(self):
        return self.HP

    def setHpBattle(self, hp):
        self.HP = hp

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
        return self.SATTK

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

    def getPower(self):
        return self.power

    def setPower(self, power):
        self.power = power

    def getMov(self):
        return self.mov

    def setMov(self, mov):
        self.mov = mov

    def getCategoria(self):
        return self.categoria

    def setCategoria(self, categoria):
        self.categoria = categoria

    def getTipoMov(self):
        return self.tipoMov

    def setTipoMov(self, tipoMov):
        self.tipoMov = tipoMov

    def getStatMov(self, movimiento):
        movimiento_stats = get_move(movimiento)
        self.setMov(movimiento_stats[0])
        self.setPower(movimiento_stats[1])
        self.setTipoMov(movimiento_stats[2])
        self.setCategoria(movimiento_stats[3])
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
        TYPE = float(self.efectividadPorTipo(self.tipo, enemigoTipo))
        rand_number = random.uniform(0.85, 1)
        if(self.tipoMov != self.tipo):
            STAB = 1
        modifier = TYPE * STAB * rand_number * 1
        return modifier

    def calcDamage(self, power, a, d, enemigoTipo):
        damage = (((((2 * LEVEL)/5) + 2) * power *
                  (a/d) / 50) + 2) * self.getModifer(enemigoTipo)
        return damage

    def imprimirEstadisticas(self):
        print("Estadísticas base del Pokémon: ")
        print("\t- HP = ", self.getPuntosVida())
        print("\t- Ataque = ", self.getPuntosAtaqueFisicoBase())
        print("\t- Defensa = ", self.getpuntosDefensaFisicoBase())
        print("\t- Ataque especial = ", self.getPuntosAtaqueEspecialBase())
        print("\t- Defensa especial = ", self.getPuntosDefensaEspecialBase())
        print("\t- Velocidad = ", self.getPuntosVelocidadBase())

    def imprimirEstadisticasAvanzadas(self):
        print(f"El hp al nivel {LEVEL} de {self.nombre} es  ", self.getHp())
        print(f"El atk al nivel {LEVEL} de {self.nombre} es  ", self.getAttk())
        print(f"El def al nivel {LEVEL} de {self.nombre} es  ", self.getDef())
        print(
            f"El spa al nivel {LEVEL} de {self.nombre} es  ", self.getSattk())
        print(f"El spd al nivel {LEVEL} de {self.nombre} es  ", self.getSDef())
        print(f"El spe al nivel {LEVEL} de {self.nombre} es  ", self.getSpe())

    def generateDamage(self, pokemon):
        print(
            f"El hp al nivel {LEVEL} de {pokemon.getNombre().capitalize()} es  ", pokemon.getHp())
        categoria = self.getCategoria()
        enemigoTipo = pokemon.getTipo()
        if(categoria == "special"):
            atak = self.getSattk()
            deff = pokemon.getSDef()
        else:
            atak = self.getAttk()
            deff = pokemon.getDef()
        damage = self.calcDamage(self.getPower(), atak, deff, enemigoTipo)
        hp_rest = pokemon.getHp() - damage
        pokemon.setHpBattle(hp_rest)
        print(
            f"El daño que realizó {pokemon.getNombre().capitalize()} a {self.getNombre().capitalize()} fue de: {damage}")
        print("\n")
        print(
            f"{pokemon.getNombre().capitalize()} quedó con un HP de: {pokemon.getHp()}")

    def mostrarMovimientos(self):
        print("\nMovimientos que puede aprender el pokémon: ")
        for item in range(0, len(self.movimientos)):
            print(f"{item}   -    {self.movimientos[item]}")
