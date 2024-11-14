class Matriz:
    def __init__(self, fila, col, matriz_inicial=None):
        self.fila = fila
        self.col = col
        if matriz_inicial:
            self.matrix = matriz_inicial
        else:
            self.matrix = [[0] * col for _ in range(fila)]

    def get_number_fila(self):
        return self.fila

    def get_number_col(self):
        return self.col

    def set_element(self, x, j, element):
        if 0 <= x < self.fila and 0 <= j < self.col:
            self.matrix[x][j] = element
        else:
            print("Índice fuera de los límites de la matriz.")

    def add_matrix(self, other_matrix):
        if len(other_matrix) != self.fila or len(other_matrix[0]) != self.col:
            print("Error: Las matrices deben tener el mismo tamaño para sumar.")
            return
        
        for i in range(self.fila):
            for j in range(self.col):
                self.matrix[i][j] += other_matrix[i][j]

    def mult_matrix(self, other_matrix):
        if len(other_matrix) != self.fila or len(other_matrix[0]) != self.col:
            print("Error: Las matrices deben tener el mismo tamaño para multiplicar elemento a elemento.")
            return
        
        for i in range(self.fila):
            for j in range(self.col):
                self.matrix[i][j] *= other_matrix[i][j]

    def print_matrix(self):
        for row in self.matrix:
            print(" ".join(map(str, row)))

if __name__ == "__main__":
    # Crear la matriz inicial con los valores correctos
    matriz = Matriz(2, 2, [[1, 2], [3, 4]])

    # Imprimir matriz original
    print("Matriz original:")
    matriz.print_matrix()

    # Matriz para suma
    matriz_suma = [[1, 10], [15, 25]]
    matriz.add_matrix(matriz_suma)
    print("\nDespués de la suma:")
    matriz.print_matrix()

    # Matriz para multiplicación
    matriz_mult = [[3, 2], [1, 5]]
    matriz.mult_matrix(matriz_mult)
    print("\nDespués de la multiplicación elemento a elemento:")
    matriz.print_matrix()

"""
# --------- LO QUE SE VE EN CONSOLA ----------
Matriz original:
1 2
3 4

Después de la suma:
2 12
18 29

Después de la multiplicación elemento a elemento:
6 24
18 145
# --------- LO QUE SE VE EN CONSOLA ----------
"""
