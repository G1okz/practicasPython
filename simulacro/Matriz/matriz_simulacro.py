# Calcular la transversa de una matriz

class Matriz:
    def __init__(self, matriz):
        self.matriz = matriz

    def transversa(self): 
        transversa = []
        for i in range(len(self.matriz[0])):
            fila = []
            for j in range(len(self.matriz)):
                fila.append(self.matriz[j][i])
            transversa.append(fila)
        return transversa

def main():
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matriz_obj = Matriz(matriz)
    print("Matriz original:")
    for fila in matriz:
        print(fila)
    print("Matriz transversa:")
    matriz_transversa = matriz_obj.transversa()
    for fila in matriz_transversa:
        print(fila)

if __name__ == "__main__":
    main()


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
