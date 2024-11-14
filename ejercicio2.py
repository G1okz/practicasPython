class NumerosEnteros:
    def __init__(self):
        # Inicializamos una lista vacía para almacenar los números
        self.numeros = []

    # Método para agregar 10 números a la lista
    def agregar_numeros(self):
        print("Obtener 10 números enteros:")
        for i in range(10):
            x = int(input("Inserte el número: "))
            self.numeros.append(x)

    # Método para contar cuántas veces aparece el número 0 en la lista
    def contar_zeros(self):
        return self.numeros.count(0)

    # Método para contar cuántas veces aparece el dígito '0' en todos los números de la lista
    def contar_digitos_cero(self):
        return sum(str(num).count('0') for num in self.numeros)

    # Método para contar cuántos números son mayores que 0
    def contar_mayores_que_cero(self):
        return len([i for i in self.numeros if i > 0])

    # Método para contar cuántos números son menores que 0
    def contar_menores_que_cero(self):
        return len([i for i in self.numeros if i < 0])

    # Método para mostrar los resultados
    def mostrar_resultados(self):
        print("Números:", self.numeros)
        print("El número 0 apareció", self.contar_zeros(), "veces")
        print("El dígito '0' apareció", self.contar_digitos_cero(), "veces en total")
        print("Cantidad de números > 0:", self.contar_mayores_que_cero())
        print("Cantidad de números < 0:", self.contar_menores_que_cero())


if __name__ == "__main__":
    # Crear una instancia de la clase NumerosEnteros
    numeros = NumerosEnteros()

    # Agregar los números a la lista
    numeros.agregar_numeros()

    # Mostrar los resultados
    numeros.mostrar_resultados()


"""
# ------- LO QUE SE VE EN CONSOLA ------- #
Obtener 10 números enteros:
Números: [-1, -2, -3, -4, 5, 6, 7, 0, 10, 20]
El número 0 apareció 1 veces
El dígito '0' apareció 3 veces en total
Cantidad de números > 0: 5
Cantidad de números < 0: 4
# ------- LO QUE SE VE EN CONSOLA ------- #        
"""
