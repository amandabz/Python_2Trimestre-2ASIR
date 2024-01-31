"""
Ejercicio 1: Introducción a las Clases

Tarea: Crea una clase `Coche` que tenga dos atributos: `marca` y `modelo`. Incluye un método `mostrar_info()`
que imprima "Marca: [marca], Modelo: [modelo]".

Bonus: Añade un método `cambiar_modelo()` que permita modificar el atributo `modelo`.
"""


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_info(self):
        print(f"Marca: {self.brand}, Modelo: {self.model}")

    def change_model(self, new_model):
        self.model = new_model
        print(f"Nuevo modelo: {new_model}")


# examples of use
# get info
my_car = Car(brand="Toyota", model="Corolla")
my_car.get_info()

# change model
my_car.change_model("Camry")
my_car.get_info()