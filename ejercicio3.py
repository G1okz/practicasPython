import random

class JuegoAdivinanza:
    def __init__(self):
        # Inicializamos el número aleatorio entre 0 y 20
        self.nAleatorio = random.randint(0, 20)
        # Inicializamos el contador de intentos
        self.intentos = 0

    def jugar(self):
        print("Número generado. \n -- ¡QUE COMIENCE EL JUEGO! --")

        # El primer intento del jugador
        adivina = int(input("Adivina el número: "))

        # Verificamos si el número ingresado es correcto
        if adivina == self.nAleatorio:
            print("¡Felicidades, adivinaste el número!")
        else:
            # Si no es correcto, seguimos pidiendo intentos hasta adivinar
            while adivina != self.nAleatorio:
                self.intentos += 1
                if adivina > self.nAleatorio:
                    print("El número ingresado es mayor al número generado.")
                else:
                    print("El número ingresado es menor al número generado.")
                adivina = int(input("Prueba de nuevo: "))
            # Al acertar, mostramos los intentos realizados
            print(f"¡Felicidades, adivinaste el número en {self.intentos} intentos!")


if __name__ == "__main__":
    # Crear una instancia del juego y empezar a jugar
    juego = JuegoAdivinanza()
    juego.jugar()
