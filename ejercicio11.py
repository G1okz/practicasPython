# Ejercicio de tabla multidimensional
class GestionSalarios:
    def __init__(self, salarios, empleados):
        # Inicializamos las listas de salarios y empleados
        self.salarios = salarios
        self.empleados = empleados

    def mostrar(self):
        # Muestra los salarios de cada empleado junto con la suma total
        if len(self.salarios) == len(self.empleados):
            print("---------- MOSTRAR ----------")
            for i in range(len(self.salarios)):
                print(f"{self.empleados[i]} -> ", end="")
                suma = 0
                for x in range(len(self.salarios[i])):
                    suma += self.salarios[i][x]
                    operador = "+" if x != len(self.salarios[i]) - 1 else "= " + str(suma)
                    print(f"{self.salarios[i][x]} {operador} ", end="")
                print("")

    def ordenar(self):
        # Ordena los salarios de cada empleado de menor a mayor
        if len(self.salarios) == len(self.empleados):
            print("---------- ORDENAR ----------")
            for i in range(len(self.salarios)):
                print(f"{self.empleados[i]} -> ", end="")
                self.salarios[i].sort()
                for x in range(len(self.salarios[i])):
                    operador = "/" if x != len(self.salarios[i]) - 1 else ""
                    print(f"{self.salarios[i][x]} {operador} ", end="")
                print("")

if __name__ == "__main__":
	# MAIN
	salarios = [[700, 900, 1300], [1000, 950, 1080], [1300, 930, 1200]]
	empleados = ["Javier Marías", "Antonio Muñoz", "Isabel Allende"]

	gestion = GestionSalarios(salarios, empleados)
	gestion.mostrar()
	gestion.ordenar()

"""
# --------- LO QUE SE VE EN CONSOLA ---------- #
---------- MOSTRAR ----------
Javier Marías -> 700 + 900 + 1300 = 2900
Antonio Muñoz -> 1000 + 950 + 1080 = 3030
Isabel Allende -> 1300 + 930 + 1200 = 3430
---------- ORDENAR ----------
Javier Marías -> 700 / 900 / 1300
Antonio Muñoz -> 950 / 1000 / 1080
Isabel Allende -> 930 / 1200 / 1300
# --------- LO QUE SE VE EN CONSOLA ---------- #
"""
