from Pokemon import Pokemon
from utils import initPokemon, getCsvPokemonData


if __name__ == "__main__":
    print("Bienvenido al simulador")
    cont = True
    selectedPokemon: Pokemon = None
    while cont:
        name = input("Ingrese el nombre del primer Pokémon: ")
        result = getCsvPokemonData(name)
        if(result != None):
            selectedPokemon, efectividad = initPokemon(result)
            cont = False
        print(
            f"El Pokemon '{name}' no esta en nuestra data, intenta con otro.")
    print(selectedPokemon)
    print("\n")
    selectedPokemon.setEfectividad(efectividad)
    selectedPokemon.imprimirEstadisticas()
    selectedPokemon.mostrarMovimientos()
    mov = int(input("Seleccione un ataque a ejecutar: "))
    movSelected = selectedPokemon.getMovimientoPorIndice(mov)
    print("El ataque seleccionado es: ", movSelected)
    print("Poder de ataque es: ", selectedPokemon.getStatMov(movSelected))
    selectedPokemon.imprimirEstadisticasAvanzadas()
    cont = True
    while cont:
        conter = input("Ingrese el nombre a atacar Pokémon: ")
        resultConter = getCsvPokemonData(conter)
        if(resultConter != None):
            conterSelectedPokemon, efectividad = initPokemon(resultConter)
            cont = False
    print(conterSelectedPokemon)
    conterSelectedPokemon.setEfectividad(efectividad)
    print("\n")
    selectedPokemon.generateDamage(conterSelectedPokemon)
