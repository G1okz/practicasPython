'''
    Esta clase contiene la estructura basica para la creacion
    de un pokemon.
    
    @author: Alvaro profe
'''
class PokemonCard:
    def __init__(self, nombre, tipo, hp, ataque, defensa, hab_especial):
        self.nombre = nombre
        self.tipo = tipo
        self.hp = hp
        self.ataque = ataque
        self.defensa = defensa
        self.hab_especial = hab_especial

    def getNombre(self):
        return self.nombre

    def getTipo(self):
        return self.tipo

    def getHp(self):
        return self.hp
    
    def getAtaque(self):
        return self.ataque
    
    def getDefensa(self):
        return self.defensa
    
    def getHab_especial(self):
        return self.hab_especial

    '''
        Metodo que simula el ataque. Este se realiza
        sobre [pokemon_atacado]
    '''
    def atacar(self, pokemon_atacado):
        pokemon_atacado.recibir_dano(self.ataque)
    
    '''
        Resta el dano recibido a la vida actual
        del pokemon
    '''
    def recibir_dano(self, dano):
        self.hp -= dano

    '''
        Devuelve True sí y solo si el pokemon ha muerto
    '''
    def estaMuerto(self):
        return self.hp <= 0

