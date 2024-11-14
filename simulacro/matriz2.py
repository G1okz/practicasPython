# Matriz simétrica

class Matriz:
    def __init__(self, matriz):
        self.matriz = matriz

    def es_simetrica(self):
        filas = len(self.matriz)
        
        # Verificar si la matriz es cuadrada
        for i in range(filas):
            if len(self.matriz[i]) != filas:
                return False
        
        # Verificar la propiedad de simetría A(i, j) == A(j, i)
        for i in range(filas):
            for j in range(i + 1, filas):  # Sólo revisamos la parte superior triangular
                if self.matriz[i][j] != self.matriz[j][i]:
                    return False
        return True

    def imprimir(self):
        for fila in self.matriz:
            print(fila)
            
# Ejemplo de uso
matriz = Matriz([
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
])

matriz.imprimir()
if matriz.es_simetrica():
    print("La matriz es simétrica.")
else:
    print("La matriz no es simétrica.")
