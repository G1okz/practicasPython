import random

print("Generar numero aleatorio")

nAleatorio = random.randint(1, 20)

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
        if adivina > nAleatorio:
            print("El numero ingresado es mayor al numero generado")
        else:
            print("El numero ingresado es menor al numero generado")
        adivina = int(input("Prueba de nuevo: "))
    print("Felicidades, adivinaste el numero")    


