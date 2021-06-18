import pandas as pd
from Pokemon import Pokemon
import numpy as np


def getCsv(filename):
    df = pd.read_csv(filename, header=None)
    df = df.replace('', np.nan)
    df = df.dropna(axis="columns", how="any")
    list_of_rows = [list(row) for row in df.values]
    return list_of_rows


def initLoadData():
    efectivity = "tabla_efectividad.csv"
    pokemon_data = "pokemon_data.csv"
    efectividad = getCsv(efectivity)
    poke_data = getCsv(pokemon_data)
    pokemonlist = list()
    for index in range(len(poke_data)):
        obj_pokemon = Pokemon(
            poke_data[index][0],
            poke_data[index][2],
            poke_data[index][3],
            poke_data[index][4],
            poke_data[index][5],
            poke_data[index][6],
            poke_data[index][7]
        )
        obj_pokemon.setTipo(poke_data[index][1])
        obj_pokemon.setMovimientos(poke_data[index][8].split(";"))
        obj_pokemon.setHp(obj_pokemon.getPuntosVida())
        obj_pokemon.setDef(obj_pokemon.getpuntosDefensaFisicoBase())
        obj_pokemon.setSDef(obj_pokemon.getPuntosDefensaEspecialBase())
        obj_pokemon.setAttk(obj_pokemon.getPuntosAtaqueFisicoBase())
        obj_pokemon.setSattk(obj_pokemon.getPuntosAtaqueEspecialBase())
        obj_pokemon.setSpe(obj_pokemon.getPuntosVelocidadBase())
        pokemonlist.append(obj_pokemon)
    return [pokemonlist, efectividad]
