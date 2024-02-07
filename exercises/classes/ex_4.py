"""
Ejercicio 4: Encapsulamiento y Propiedades

Tarea: Diseña una clase `CuentaBancaria` que encapsule el atributo `saldo`, haciéndolo privado. Utiliza un decorador
`@property` para obtener el saldo y un método setter para depositar dinero, asegurándote de que no se pueda depositar
una cantidad negativa.

Bonus: Añade una función de retiro que verifique si hay suficiente saldo antes de permitir la transacción.
"""


class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def deposit(self, amount: float):
        if amount < 0:
            print("Error, cannot deposit a negative amount")
        else:
            self._balance += amount
            print(f"You have deposited {amount}, current balance is {self._balance}")

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f"You have withdrawn {amount}, current balance is {self._balance}")
        else:
            print("Error, insufficient balance. Try a smaller amount")


# examples of use
account = BankAccount()
account._balance = 200.0
account.deposit = 300.0
account.withdraw(10.0)
