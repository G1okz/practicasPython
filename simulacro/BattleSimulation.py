from PokemonCard import PokemonCard

"""
@author: Alvaro profe
"""

'''
    Metodo que simula la batalla entre dos pokemon. Esta finaliza
    cuando alguno de los dos pierde toda su vida. El metodo
    termina mostrando por pantalla el nombre del ganador
'''
def batalla(pokemonAtaca, pokemonDefiende):
    while(True):
        if not _hayGanador(pokemonAtaca, pokemonDefiende):
            _acciones(_mainMenu(pokemonAtaca), pokemonAtaca, pokemonDefiende)
            pokemonAtaca, pokemonDefiende = _cambiarTurno(pokemonAtaca, pokemonDefiende)
            _resumenEstado(pokemonAtaca, pokemonDefiende)
        else: exit()

'''
    Muestra por pantalla el menu de acciones para el Pokemon
    mandado por parametro.
'''
def _mainMenu(pokemon):
    print("---- Bienvenido al simulador de batallas Pokemon ---")
    print(f" Es turno del Pokemon: {pokemon.getNombre()} con vida actual = {pokemon.getHp()}")
    print(" Seleccione una de las siguientes opciones:")
    print(" 1 - Atacar")
    print(" 2 - Salir")
    return int(input(" > "))

'''
    Ejecuta la acccion solicitada por el usuario. La accion es realizada
    por [pokemonAtaca] y se ejecuta sobre [pokemonDefiende]
'''
def _acciones(opcion, pokemonAtaca, pokemonDefiende):
    if opcion == 1:
        pokemonAtaca.atacar(pokemonDefiende)
        print("Pokemon ataca")
    elif opcion == 2:
        exit()
    else: print("Error")

'''
    Devuelve un numero entero que indica el ganador de la batalla.
    En caso de que no exista un gnador para este turno, devuelve 3
'''
def _hayGanador(pokemon1, pokemon2):
    if pokemon1.estaMuerto(): 
      print(f"{pokemon2.getNombre()} ganador!!")
    elif pokemon2.estaMuerto(): 
      print(f"{pokemon1.getNombre()} ganador!!")
    else: return False
    return True

'''
    Intercambia los pokemon entre posicion de ataque y defensa
'''
def _cambiarTurno(pokemonAtaca, pokemonDefiende):
    return pokemonDefiende, pokemonAtaca

'''
    Muestra un resumen del estado actual de la batalla.
'''
def _resumenEstado(pokemon1, pokemon2):
    print("¡ESTADO ACTUAL DE LA BATALLA!")
    print(f"{pokemon1.getNombre()} -> hp = {pokemon1.getHp()}")
    print(f"{pokemon2.getNombre()} -> hp = {pokemon2.getHp()}")

pokemon1 = PokemonCard('Charizard', 'Fuego', 200, 20, 30, 'Llamarada')
pokemon2 = PokemonCard('Blastoise', 'Agua', 200, 25, 25, 'Hidrobomba')
batalla(pokemon1, pokemon2)
