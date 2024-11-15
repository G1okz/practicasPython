def traspuesta(matriz):
    # Usamos zip(*) para trasponer la matriz
    traspuesta = [list(fila) for fila in zip(*matriz)]
    return traspuesta

# Ejemplo de uso
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

resultado = traspuesta(matriz)
print("Matriz original:")
for fila in matriz:
    print(fila)

print("Matriz traspuesta:")
for fila in resultado:
    print(fila)


""""
# ------- LO QUE SE VE EN CONSOLA ------- #
Matriz original:
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
Matriz transversa:
[1, 4, 7]
[2, 5, 8]
[3, 6, 9]
# ------- LO QUE SE VE EN CONSOLA ------- # 
"""

# Matriz escalonada #
def es_escalonada(matriz):
    fila_anterior = -1  # Índice del primer elemento no cero de la fila anterior
    
    for fila in matriz:
        indice_actual = 0 
        lider_encontrado = False

        for valor in fila:
            if valor != 0:
                if indice_actual <= fila_anterior:
                    return False  # No cumple la regla del líder más a la derecha
                fila_anterior = indice_actual
                lider_encontrado = True
                break
            indice_actual += 1  

        if not lider_encontrado:  # Si toda la fila es cero
            fila_anterior = len(fila)
            
    return True

# Ejemplo de uso
matriz1 = [
    [1, 2, 0],
    [0, 3, 4],
    [0, 0, 5]
]

matriz2 = [
    [1, 2, 0],
    [0, 0, 4],
    [0, 3, 5]
]

print("Matriz 1", es_escalonada(matriz1))
print("Matriz 2", es_escalonada(matriz2))

