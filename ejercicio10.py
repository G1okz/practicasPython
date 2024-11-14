# De la tabla, mostrar el string con mayor y menor longitud
class AnalisisTabla:
    def __init__(self, tabla):
        # Inicializamos la tabla de palabras
        self.tabla = tabla

    def mayor_menor(self):
        # Encuentra las palabras con mayor y menor longitud en la tabla
        if len(self.tabla) > 0:
            indice_mayor = 0
            indice_menor = 0
            for i in range(len(self.tabla)):
                if len(self.tabla[i]) > len(self.tabla[indice_mayor]):
                    indice_mayor = i
                elif len(self.tabla[i]) < len(self.tabla[indice_menor]):
                    indice_menor = i
            print(f"Índice {indice_mayor} contiene palabra con MÁS longitud: {self.tabla[indice_mayor]}")
            print(f"Índice {indice_menor} contiene palabra con MENOS longitud: {self.tabla[indice_menor]}")
        else:
            print("Error -> La tabla está vacía.")


# MAIN
tabla = ["Hola", "Adios", "Hasta Luego", "Hola como estas"]
analisis = AnalisisTabla(tabla)
analisis.mayor_menor()
