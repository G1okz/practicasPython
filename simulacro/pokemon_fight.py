import random

class PokemonCard:
    def __init__(self, nombre, tipo, ataque, defensa, hp, habilidad_especial):
        self.nombre = nombre
        self.tipo = tipo
        self.ataque = ataque
        self.defensa = defensa
        self.hp = hp
        self.habilidad_especial = habilidad_especial
        self.habilidad_usada = False

    def atacar(self, oponente):
        if not self.habilidad_usada:
            print(f"{self.nombre} usa {self.habilidad_especial}")
            ataque_modificado = int(self.ataque * 1.2)
            self.habilidad_usada = True
        else:
            ataque_modificado = self.ataque

        dano = max(0, ataque_modificado - oponente.defensa)
        print(f"{self.nombre} ataca a {oponente.nombre} y le hace {dano} puntos de daño")
        oponente.recibir_dano(dano)
        print(f"{oponente.nombre} tiene {oponente.hp} puntos de vida")

    def recibir_dano(self, dano):
        self.hp -= dano
        if self.hp <= 0:
            self.hp = 0
            print(f"{self.nombre} ha sido derrotado")

class PokemonBattle:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def iniciarBatalla(self):
        turno = 1
        while self.pokemon1.hp > 0 and self.pokemon2.hp > 0:
            print(f"Turno {turno}")

            if turno % 2 != 0:
                self.pokemon1.atacar(self.pokemon2)
            else:
                self.pokemon2.atacar(self.pokemon1)

            if self.pokemon1.hp <= 0:
                print(f"{self.pokemon2.nombre} ha ganado")
                break
            elif self.pokemon2.hp <= 0:
                print(f"{self.pokemon1.nombre} ha ganado")
                break

            turno += 1

def crear_pokemon():
    nombre = input("Nombre: ")
    tipo = input("Tipo: ")
    ataque = int(input("Ataque (10 - 50): "))
    defensa = int(input("Defensa (5 - 20): "))
    hp = int(input("HP (50 - 150): "))
    habilidad_especial = input("Habilidad especial: ")

    return PokemonCard(nombre, tipo, ataque, defensa, hp, habilidad_especial)

def crear_pokemon_aleatorio():
    nombre = "Pokemon" + str(random.randint(1, 100))
    tipo = random.choice(["Fuego", "Agua", "Planta"])
    ataque = random.randint(10, 50)
    defensa = random.randint(5, 20)
    hp = random.randint(50, 150)
    habilidad_especial = "Habilidad" + str(random.randint(1, 100))

    return PokemonCard(nombre, tipo, ataque, defensa, hp, habilidad_especial)

def main():
    print("Hola, bienvenido a Pokemon Fight")
    print("Elige tu pokemon")
    pokemon1 = crear_pokemon()
    print("Eligiendo el pokemon del oponente")
    pokemon2 = crear_pokemon_aleatorio()

    print("Comienza la batalla")
    batalla = PokemonBattle(pokemon1, pokemon2)
    batalla.iniciarBatalla()

if __name__ == "__main__":
    main()
