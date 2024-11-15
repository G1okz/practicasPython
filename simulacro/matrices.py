# Multiplicación de una matriz por un escalar #
def multiplicar_matriz_por_escalar(matriz, escalar):
    resultado = []
    for fila in matriz:
        nueva_fila = [elemento * escalar for elemento in fila]
        resultado.append(nueva_fila)
    return resultado

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

escalar = 2
resultado = multiplicar_matriz_por_escalar(matriz, escalar)
print(f"Matriz multiplicada por {escalar}:")
for fila in resultado:
    print(fila)


# Producto de dos matrices #
def multiplicar_matrices(matriz1, matriz2):
    # Verificar si las matrices son multiplicables
    if len(matriz1[0]) != len(matriz2):
        return "Las matrices no son multiplicables"
    
    # Crear la matriz resultante con las dimensiones adecuadas
    resultado = [[0] * len(matriz2[0]) for _ in range(len(matriz1))]
    
    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz2)):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]
    
    return resultado

matriz1 = [[1, 2], [3, 4]]

matriz2 = [[5, 6], [7, 8]]

resultado = multiplicar_matrices(matriz1, matriz2)
print("Producto de matrices:")
for fila in resultado:
    print(fila)


# Suma de todos los elementos de una matriz #
def suma_matriz(matriz):
    suma = 0
    for fila in matriz:
        suma += sum(fila)
    return suma

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

resultado = suma_matriz(matriz)
print(f"La suma de los elementos de la matriz es: {resultado}")

# Diagonal principal de una matriz #
def diagonal_principal(matriz):
    if len(matriz) != len(matriz[0]):
        return "La matriz no es cuadrada"
    
    diagonal = [matriz[i][i] for i in range(len(matriz))]
    return diagonal

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

resultado = diagonal_principal(matriz)
print(f"Diagonal principal: {resultado}")


# Diagonal secundaria #
def diagonal_secundaria(matriz):
    if len(matriz) != len(matriz[0]):
        return "La matriz no es cuadrada"
    
    diagonal = [matriz[i][len(matriz) - 1 - i] for i in range(len(matriz))]
    return diagonal

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Matriz de ceros y unos alternados #
resultado = diagonal_secundaria(matriz)
print(f"Diagonal secundaria: {resultado}")

def generar_matriz_alternada(n):
    matriz = []
    for i in range(n):
        fila = [(i + j) % 2 for j in range(n)]
        matriz.append(fila)
    return matriz

n = 3
resultado = generar_matriz_alternada(n)

print("Matriz alternada:")
for fila in resultado:
    print(fila)


# Intercambiar filas #
def intercambiar_filas(matriz, fila1, fila2):
    # Para intercambiar columnas --> 
    # if col1 >= len(matriz[0]) or col2 >= len(matriz[0]):
    if fila1 >= len(matriz) or fila2 >= len(matriz):
        return "Índices de filas fuera de rango"
    
    for fila in matriz:     
        matriz[fila1], matriz[fila2] = matriz[fila2], matriz[fila1]
    return matriz

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

fila1 = 0
fila2 = 2

resultado = intercambiar_filas(matriz, fila1, fila2)
print("Matriz después de intercambiar filas:")
for fila in resultado:
    print(fila)


# Buscar un elemento en la matriz #
def buscar_elemento(matriz, elemento):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == elemento:
                return (i, j)
    return "Elemento no encontrado"

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

elemento = 5
resultado = buscar_elemento(matriz, elemento)
print(f"Elemento {elemento} encontrado en: {resultado}")

# Crear una matriz identidad #
def crear_matriz_identidad(n):
    matriz = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    return matriz

n = 4
resultado = crear_matriz_identidad(n)

print("Matriz identidad:")
for fila in resultado:
    print(fila)

# Comprobar matriz identidad #
def es_identidad(matriz):
    n = len(matriz)
    
    # Verificar si es cuadrada
    for fila in matriz:
        if len(fila) != n:
            return False  # No es cuadrada

    # Comprobar condiciones de la identidad
    for i in range(n):
        for j in range(n):
            if i == j and matriz[i][j] != 1:  # Diagonal debe ser 1
                return False
            elif i != j and matriz[i][j] != 0:  # Fuera de la diagonal debe ser 0
                return False

    return True


# Verificar si la matriz es simetrica #
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

    def mostrar_matriz(self):
        print("Matriz simetrica:")
        for fila in self.matriz:
            print(fila)

# Crear una matriz
matriz = Matriz([[1, 2, 3], [2, 4, 5], [3, 5, 6]]) # Es simétrica

# Mostrar la matriz
matriz.mostrar_matriz()

# Verificar si es simétrica
if matriz.es_simetrica():
    print("La matriz es simétrica.")
else:
    print("La matriz NO es simétrica.")


# Suma de dos matrices #
def sumar_matrices(matriz1, matriz2):
    # Verificar que ambas matrices tengan las mismas dimensiones
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        return "Las matrices deben tener las mismas dimensiones"
    
    # Crear una nueva matriz para almacenar la suma
    resultado = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz1[i])):
            fila.append(matriz1[i][j] + matriz2[i][j])
        resultado.append(fila)
    
    return resultado

matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

resultado = sumar_matrices(matriz1, matriz2)
print("Suma de matrices:")
for fila in resultado:
    print(fila)


# Matriz ortogonal #
def es_ortogonal(matriz):
    def multiplicar_matrices(A, B):
        # Multiplica dos matrices cuadradas de tamaño n x n
        n = len(A)
        resultado = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                resultado[i][j] = sum(A[i][k] * B[k][j] for k in range(n))
        return resultado

    # Verificar si la matriz es cuadrada
    n = len(matriz)
    for fila in matriz:
        if len(fila) != n:
            return False  # No es cuadrada, por lo tanto no puede ser ortogonal

    # Generar la matriz identidad
    identidad = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    # Calcular la traspuesta
    traspuesta = [list(fila) for fila in zip(*matriz)]

    # Verificar si matriz * traspuesta == identidad
    producto = multiplicar_matrices(matriz, traspuesta)
    return producto == identidad

# Ejemplo de uso
matriz1 = [
    [1, 0],
    [0, 1]
]

matriz2 = [
    [1, 0],
    [1, 1]
]

print("¿La matriz1 es ortogonal?", es_ortogonal(matriz1))  # True
print("¿La matriz2 es ortogonal?", es_ortogonal(matriz2))  # False
