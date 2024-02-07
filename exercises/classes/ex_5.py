"""
Ejercicio 5: Polimorfismo y Métodos Especiales

Tarea: Crea una clase `Vector` que represente un vector en 2D, con métodos especiales para la suma (`__add__`),
la resta (`__sub__`), y la representación en string (`__str__`).

Bonus: Implementa la multiplicación de un vector por un escalar (no la multiplicación de dos vectores).
"""


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, var_sum):
        return Vector(self.x + var_sum.x, self.y + var_sum.y)

    def __sub__(self, var_rest):
        return Vector(self.x - var_rest.x, self.y - var_rest.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


# example of use
vec_1 = Vector(3, 12)
vec_2 = Vector(9, 11)

print(vec_1 + vec_2)
print(vec_1 - vec_2)


