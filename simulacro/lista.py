# Dada una lista ordenada de enteros y con posibles repeticiones,
# obterner como salida una lista de enteros sin repeticiones

class Lista:
    def __init__(self, lista):
        self.lista = lista
        
    def sin_repeticiones(self):
        # Eliminar duplicados utilizando set y luego ordenar
        sin_repeticiones = list(set(self.lista))
        sin_repeticiones.sort()
        return sin_repeticiones
    
if __name__ == "__main__":
    lista = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    lista_obj = Lista(lista)
    print("Lista original:", lista)
    print("Lista sin repeticiones:", lista_obj.sin_repeticiones())
