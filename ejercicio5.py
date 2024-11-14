class CadenaCaracteres:
    def __init__(self, cadena):
        # Inicializamos la cadena de caracteres
        self.cadena = cadena

    def longitud(self):
        # Retorna la longitud de la cadena
        return len(self.cadena)

    def contar_aaa(self):
        # Verifica cuántas veces aparece "aaa" en la cadena
        if "aaa" in self.cadena:
            nVeces = self.cadena.count('aaa')
            return f"La cadena 'aaa' apareció un total de {nVeces} veces."
        else:
            return f"La cadena 'aaa' NO está dentro de '{self.cadena}'."

if __name__ == "__main__":
	# Solicitar la cadena de caracteres al usuario
	cadena_usuario = input("Dame una cadena de caracteres: ")

	# Crear una instancia de la clase CadenaCaracteres
	cadena = CadenaCaracteres(cadena_usuario)

	# Mostrar la longitud de la cadena
	print("Longitud de la cadena de caracteres =", cadena.longitud())

	# Mostrar la cantidad de veces que "aaa" aparece en la cadena
	print(cadena.contar_aaa())


""""
# ------- LO QUE SE VE EN CONSOLA ------- #
Dame una cadena de caracteres: holaaa como estaaas
Longitud de la cadena de caracteres = 19
La cadena 'aaa' apareció un total de 2 veces.
# ------- LO QUE SE VE EN CONSOLA ------- #
"""
