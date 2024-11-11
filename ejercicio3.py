import random

nAleatorio = random.randint(0, 20)
intentos = 0

print("Numero generado. \n -- QUE COMIENCE EL JUEGO --")

# print("Numero generado: ", nAleatorio)

adivina = int(input("Adivina el numero: "))

"""
Mientras el numero adivinado sea diferente al numero generado, 
se seguira pidiendo al usuario que adivine el numero diciendo 
si el numero ingresado por el usuario es mayor o menor al numero aleatorio.
"""

if adivina == nAleatorio:
    print("Felicidades, adivinaste el numero")
else:
    while adivina != nAleatorio:
        intentos = intentos + 1
        if adivina > nAleatorio:
            print("El numero ingresado es mayor al numero generado")
        else:
            print("El numero ingresado es menor al numero generado")
        adivina = int(input("Prueba de nuevo: "))
    print("Felicidades, adivinaste el numero en ", intentos, " intentos")    



