class Matriz:
    def __init__(self, rows, columns, initial_matrix=None):
        self.rows = rows
        self.columns = columns
        if initial_matrix:
            self.matrix = initial_matrix
        else:
            self.matrix = [[0] * columns for _ in range(rows)]

    def get_number_rows(self):
        return self.rows

    def get_number_columns(self):
        return self.columns

    def set_element(self, x, j, element):
        if 0 <= x < self.rows and 0 <= j < self.columns:
            self.matrix[x][j] = element
        else:
            print("Índice fuera de los límites de la matriz.")

    def add_matrix(self, other_matrix):
        if len(other_matrix) != self.rows or len(other_matrix[0]) != self.columns:
            print("Error: Las matrices deben tener el mismo tamaño para sumar.")
            return
        
        for i in range(self.rows):
            for j in range(self.columns):
                self.matrix[i][j] += other_matrix[i][j]

    def mult_matrix(self, other_matrix):
        if len(other_matrix) != self.rows or len(other_matrix[0]) != self.columns:
            print("Error: Las matrices deben tener el mismo tamaño para multiplicar elemento a elemento.")
            return
        
        for i in range(self.rows):
            for j in range(self.columns):
                self.matrix[i][j] *= other_matrix[i][j]

    def print_matrix(self):
        for row in self.matrix:
            print(" ".join(map(str, row)))


# Crear la matriz inicial con los valores dados
matriz = Matriz(2, 2, [[1, 2], [1, 2]])

# Imprimir matriz original
print("Matriz original:")
matriz.print_matrix()

# Matriz para suma
matriz_suma = [[1, 2], [1, 2]]
matriz.add_matrix(matriz_suma)
print("\nDespués de la suma:")
matriz.print_matrix()

# Matriz para multiplicación
matriz_mult = [[2, 2], [2, 2]]
matriz.mult_matrix(matriz_mult)
print("\nDespués de la multiplicación elemento a elemento:")
matriz.print_matrix()
