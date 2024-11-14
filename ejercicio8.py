# Sumar elementos de una tabla
class OperacionesTabla:
    def __init__(self, tabla):
        # Inicializamos la tabla de números
        self.tabla = tabla
    
    """
        # Para ingresar una tabla de números por consola
        # Definimos una tabla vacia
        # self.tabla = []
        
     	# Pedimos exactamente 7 números al usuario
        print("Introduce 7 números para la tabla:")
        while len(self.tabla) < 7:
            try:
                # Pedimos un número y lo añadimos a la tabla
                numero = int(input(f"Número {len(self.tabla) + 1}: "))
                self.tabla.append(numero)
            except ValueError:
                print("Por favor, introduce un número válido.")
    """

    def suma(self):
        # Calcula la suma de los elementos en la tabla
        suma = 0
        for i in range(len(self.tabla)):
            suma += self.tabla[i]
        return suma


# MAIN
tabla = [1, 2, 3, 4, 5, 6]
operacion = OperacionesTabla(tabla)
# operacion = OperacionesTabla()
print("La suma de la tabla es:", operacion.suma())
