class Operaciones:
    def __init__(self, x, y):
        # Inicializamos los valores de x y y
        self.x = x
        self.y = y

    def suma(self):
        return self.x + self.y

    def resta(self):
        return self.x - self.y

    def multiplicacion(self):
        return self.x * self.y

    def division(self):
        if self.y != 0:
            return self.x / self.y
        else:
            return "Error: División por cero no permitida"

    def resto(self):
        if self.y != 0:
            return self.x % self.y
        else:
            return "Error: División por cero no permitida"

if __name__ == "__main__":
# Solicitamos los valores de x e y al usuario
    x = int(input("Inserte el primer número: "))
    y = int(input("Inserte el segundo número: "))

    # Creamos una instancia de la clase Operaciones
    operacion = Operaciones(x, y)

    # Mostramos los resultados de cada operación
    print("La suma de los números es:", operacion.suma())
    print("La resta de los números es:", operacion.resta())
    print("La multiplicación de los números es:", operacion.multiplicacion())
    print("La división de los números es:", operacion.division())
    print("El resto de la división es:", operacion.resto())
