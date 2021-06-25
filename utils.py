from Pokemon import Pokemon


def getCsvPokemonData(name: str):
    f = open("pokemon_data.csv", "r")
    lines = f.readlines()
    selected = None
    for pokemon in lines:
        pokemon_ = pokemon.split(",")
        if(pokemon_[0] == name.lower()):
            return pokemon_
    return selected


def getCsvPokemonEfectivity():
    f = open("tabla_efectividad.csv", "r")
    lines = f.readlines()
    efect_list = list()
    for efectivity in lines:
        efect_list.append(efectivity.split(","))
    return efect_list


def initPokemon(pokemon):
    efectividad = getCsvPokemonEfectivity()
    obj_pokemon = Pokemon(
        pokemon[0],
        pokemon[2],
        pokemon[3],
        pokemon[4],
        pokemon[5],
        pokemon[6],
        pokemon[7]
    )
    print(obj_pokemon.getPuntosVida())
    obj_pokemon.setTipo(pokemon[1])
    obj_pokemon.setMovimientos(pokemon[8].split(";"))
    obj_pokemon.setHp(int(obj_pokemon.getPuntosVida()))
    obj_pokemon.setDef(obj_pokemon.getpuntosDefensaFisicoBase())
    obj_pokemon.setSDef(obj_pokemon.getPuntosDefensaEspecialBase())
    obj_pokemon.setAttk(obj_pokemon.getPuntosAtaqueFisicoBase())
    obj_pokemon.setSattk(obj_pokemon.getPuntosAtaqueEspecialBase())
    obj_pokemon.setSpe(obj_pokemon.getPuntosVelocidadBase())
    return [obj_pokemon, efectividad]
