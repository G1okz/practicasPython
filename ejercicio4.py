"""
Ingresar una cadena de texto que solo acepte de tipo string y no acepte numeros ni espacios en blanco.
Despues mostrar por pantalla la longitud de la cadena.
"""

print("Escriba la cadena de texto: ")

cadena = input()

# Verificar que la entrada no esté vacía, sea de tipo string y no contenga números o espacios
if not isinstance(cadena, str) or not cadena.isalpha():
    print("Cadena de texto vacía, no válida o contiene números")
else:
    print("La longitud es: ", len(cadena))
