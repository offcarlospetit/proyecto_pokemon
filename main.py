from Pokemon import Pokemon
from utils import initLoadData


if __name__ == "__main__":
    print("Bienvenido al simulador")
    pokelist, efectividad = initLoadData()
    cont = True
    selectedPokemon: Pokemon = None
    while cont:
        name = input("Ingrese el nombre del primer Pokémon: ")
        result = [x for x in pokelist if x.nombre == name]
        if(len(result) > 0):
            selectedPokemon = result[0]
            cont = False
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
        resultConter = [x for x in pokelist if x.nombre == conter]
        if(len(result) > 0):
            conterSelectedPokemon = resultConter[0]
            cont = False
    print(conterSelectedPokemon)
    conterSelectedPokemon.setEfectividad(efectividad)
    print("\n")
    selectedPokemon.generateDamage(conterSelectedPokemon)
