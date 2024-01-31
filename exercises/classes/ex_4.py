"""
Ejercicio 4: Encapsulamiento y Propiedades

Tarea: Diseña una clase `CuentaBancaria` que encapsule el atributo `saldo`, haciéndolo privado.
Utiliza un decorador `@property` para obtener el saldo y un método setter para depositar dinero,
asegurándote de que no se pueda depositar una cantidad negativa.

Bonus: Añade una función de retiro que verifique si hay suficiente saldo antes de permitir la transacción.
"""


class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance