"""
Ejercicio 3: Herencia

Tarea: Crea una clase base `Animal` con un método `hacer_sonido()`. Deriva dos clases `Perro` y `Gato` de `Animal`,
y sobrescribe el método `hacer_sonido()` para que retorne "Guau" y "Miau", respectivamente.

Bonus: Añade un atributo `nombre` en la clase `Animal` y demuestra cómo se puede acceder desde las clases derivadas.
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Woof"


class Cat(Animal):
    def make_sound(self):
        return "Miau"


# examples of use
dog = Dog("Dono")
cat = Cat("Coco")

print(f"{dog.name} makes the sound: {dog.make_sound()}")
print(f"{cat.name} makes the sound: {cat.make_sound()}")
