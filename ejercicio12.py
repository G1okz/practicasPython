class Cuenta:
    def __init__(self, titular, saldo=50.0):
        # Atributos: titular (obligatorio) y saldo (opcional)
        self._titular = titular
        self._saldo = float(saldo)
    
    # Métodos getter y setter para el atributo titular
    def get_titular(self):
        return self._titular
    
    def set_titular(self, titular):
        self._titular = titular
    
    # Métodos getter y setter para el atributo saldo
    def get_saldo(self):
        return self._saldo
    
    def set_saldo(self, saldo):
        self._saldo = float(saldo)
    
    # Método toString para mostrar la información de la cuenta
    def __str__(self):
        return f"Titular --> {self._titular}, con saldo: {self._saldo}"
    
    # Método para ingresar una saldo (no se ingresa si es negativa)
    def ingresar(self, saldo):
        if saldo > 0:
            self._saldo += saldo
        else:
            print("saldo negativa. No se realizó el ingreso.")

    # Método para retirar una saldo (se ajusta a 0 si queda negativa)
    def retirar(self, saldo):
        if self._saldo - saldo < 0:
            print("saldo insuficiente. No se realizó el retiro.")
        else:
            self._saldo -= saldo

# Crear una cuenta y solicitar ingreso o retiro
def gestionar_cuenta():
    titular = input("Ingrese el nombre del titular: ")
    cuenta = Cuenta(titular)

    while True:
        print("\nOpciones:")
        print("1. Ingresar dinero")
        print("2. Retirar dinero")
        print("3. Mostrar estado de la cuenta")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cantidad = float(input("Ingrese la cantidad a ingresar: "))
            cuenta.ingresar(cantidad)
        elif opcion == "2":
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cuenta.retirar(cantidad)
        elif opcion == "3":
            print(cuenta)
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar la gestión de la cuenta
gestionar_cuenta()
