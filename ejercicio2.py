# Obtener los 10 numeros enteros.
print("Obtener 10 numeros enteros:")
numeros = []
for i in range(10):
    x = input ("Inserte el numero: ")
    numeros.append(int(x))
print("Los numeros ingresados son: ", numeros)

# mostrar por pantalla las veces que aparecio el 0.
print("El numero 0 aparecio", numeros.count(0)," veces")

# Mostrar numero total de numeros enteros mayores que 0 introducidos.
print("El numero total de numeros enteros mayores que 0 es:" , len([i for i in numeros if i > 0]))

# Mostrar numero total de numeros enteros menores que 0 intoroducidos.
print("El numero total de numeros enteros mayores que 0 es:" , len([i for i in numeros if i < 0]))





