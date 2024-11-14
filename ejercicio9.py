# busca en una lista de cadenas el índice de un valor igual a 
# una cadena dada. Si no encuentra coincidencias, devuelve -1
class Buscador:
    def __init__(self, tabla):
        # Inicializamos la lista tabla en el constructor
        self.tabla = tabla

    def indexContains(self, cadena):
        # Busca el índice del valor igual a "cadena"
        for i in range(len(self.tabla)):
            if self.tabla[i] == cadena:
                return i
        return -1

tabla = ["manzana", "banana", "cereza", "naranja"]
buscador = Buscador(tabla)  # Inicializamos la clase con la lista

cadena = "cereza"
indice = buscador.indexContains(cadena)

print(f"El índice de '{cadena}' es: {indice}")
