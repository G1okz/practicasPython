class CadenaManipulacion:
    def __init__(self, cadena):
        # Inicializamos la cadena de caracteres
        self.cadena = cadena

    def intercambiar_primera_y_ultima(self):
        # Intercambia la primera y la última letra de la cadena
        if len(self.cadena) <= 1:
            return self.cadena
        cadena_cambiada = self.cadena[-1] + self.cadena[1:-1] + self.cadena[0]
        return cadena_cambiada

    def invertir_cadena(self):
        # Invierte la cadena de caracteres
        return self.cadena[::-1]

    def intercambiar_dos_primeras_y_dos_ultimas(self):
        # Intercambia las dos primeras y las dos últimas letras de la cadena
        if len(self.cadena) < 4:
            return "La cadena es demasiado corta para intercambiar las dos primeras y las dos últimas letras."
        primeras_dos = self.cadena[:2]
        ultimas_dos = self.cadena[-2:]
        centro = self.cadena[2:-2]
        return ultimas_dos + centro + primeras_dos


# Solicitar la cadena de caracteres al usuario
cadena_usuario = input("Dame una cadena de caracteres: ")

# Crear una instancia de la clase CadenaManipulacion
cadena = CadenaManipulacion(cadena_usuario)

# Mostrar resultados de las operaciones
print("Intercambio de primera y última letra:", cadena.intercambiar_primera_y_ultima())
print("Cadena invertida:", cadena.invertir_cadena())
print("Intercambio de dos primeras y dos últimas letras:", cadena.intercambiar_dos_primeras_y_dos_ultimas())
