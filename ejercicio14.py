"""
    Realiza un programa en Python en el que muestres un menú que te permita 3 opciones:
    - 1. Volcado (escritura) de una lista con todos los números pares e impares comprendidos entre 0 y 100.
    - 2. Mostrar (lectura) por pantalla el contenido del fichero de texto creado.
    - 3. Salir del Programa.
"""

class Menu:
    def __init__(self, opciones):
        self.opciones = opciones
        
    def escribirPares(self):
        with open("numeros_pares.txt", "w") as file:
            for i in range(0, 101, 2):
                file.write(str(i) + "\n")
        print("Archivo de números pares creado con éxito.")
        
    def escribirImpares(self):
        with open("numeros_impares.txt", "w") as file:
            for i in range(1, 101, 2):
                file.write(str(i) + "\n")
        print("Archivo de números impares creado con éxito.")
        
    def leerPares(self):
        try:
            with open("numeros_pares.txt", "r") as file:
                print("Contenido de numeros_pares.txt:")
                print(file.read())
        except FileNotFoundError:
            print("El archivo numeros_pares.txt no existe.")
            
    def leerImpares(self):
        try:
            with open("numeros_impares.txt", "r") as file:
                print("Contenido de numeros_impares.txt:")
                print(file.read())
        except FileNotFoundError:
            print("El archivo numeros_impares.txt no existe.")
    
    def menu(self):
        while True:
            print("Menú:")
            for opcion in self.opciones:
                print(opcion)
            
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                subopcion = int(input("Seleccione: 1. Pares, 2. Impares, 3. Ambos: "))
                if subopcion == 1:
                    self.escribirPares()
                elif subopcion == 2:
                    self.escribirImpares()
                elif subopcion == 3:
                    self.escribirPares()
                    self.escribirImpares()
                else:
                    print("Opción no válida.")
            elif opcion == 2:
                subopcion = int(input("Seleccione: 1. Pares, 2. Impares, 3. Ambos: "))
                if subopcion == 1:
                    self.leerPares()
                elif subopcion == 2:
                    self.leerImpares()
                elif subopcion == 3:
                    self.leerPares()
                    self.leerImpares()
                else:
                    print("Opción no válida.")
            elif opcion == 3:
                break
            else:
                print("Opción no válida.")
                
if __name__ == "__main__":
    opciones = ["1. Volcado (escritura) de una lista con todos los números pares e impares comprendidos entre 0 y 100.",
                "2. Mostrar (lectura) por pantalla el contenido del fichero de texto creado.",
                "3. Salir del Programa."]
    menu = Menu(opciones)
    menu.menu()
