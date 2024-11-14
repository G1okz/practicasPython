"""
Ingresar una cadena de texto que solo acepte de tipo string y no acepte numeros ni espacios en blanco.
Despues mostrar por pantalla la longitud de la cadena.
"""
class CadenaTexto:
    def __init__(self, cadena):
        # Inicializamos la cadena de texto
        self.cadena = cadena

    def verificar_cadena(self):
        # Verificamos que la cadena sea un string sin números ni espacios
        if not isinstance(self.cadena, str) or not self.cadena.isalpha():
            return "Cadena de texto vacía, no válida o contiene números"
        else:
            return f"La longitud es: {len(self.cadena)}"


if __name__ == "__main__":
    # Solicitar la cadena al usuario
    cadena_usuario = input("Escriba la cadena de texto: ")

    # Crear una instancia de la clase CadenaTexto
    cadena = CadenaTexto(cadena_usuario)

    # Mostrar el resultado de la verificación
    print(cadena.verificar_cadena())
