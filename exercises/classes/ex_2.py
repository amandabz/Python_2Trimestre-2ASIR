"""
Ejercicio 2: Uso de Constructores

Tarea: Define una clase `Estudiante` con un constructor que acepte `nombre` y `edad`. Añade un método `es_mayor()`
que retorne `True` si el estudiante es mayor de edad (18 años o más).

Bonus: Incluye un atributo de lista `calificaciones` y un método que calcule el promedio de calificaciones.
"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def is_adult(self):
        if self.age >= 18:
            return True
        return False

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)


# examples of use
# check if is an adult
my_student = Student(name="Amanda", age=18)
print(f"{my_student.name} is an adult: {my_student.is_adult()}")

# average grades
my_student.add_grade(9)
my_student.add_grade(8.5)
my_student.add_grade(9.2)
print(f"{my_student.name} has an average grade: {my_student.calculate_average_grade()}")


