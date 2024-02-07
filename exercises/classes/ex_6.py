"""
Ejercicio 6: Composición y Agregación

Tarea: Construye una clase `Biblioteca` que contenga una lista de objetos `Libro`. La `Biblioteca`
debería tener métodos para añadir y mostrar los `Libro`s.

Bonus: Implementa la eliminación de libros y asegúrate de que, al eliminar una `Biblioteca`,
los objetos `Libro` no se destruyan.
"""


class Library:
    def __init__(self):
        self.books = []

    # add a book
    def add_book(self, book):
        self.books.append(book)

    # delete a book
    def delete_book(self, book_to_delete):
        if book_to_delete in self.books:
            self.books.remove(book_to_delete)

    # show books
    def show_books(self):
        for book in self.books:
            print(book)

    def __del__(self):
        pass


# example of use
book_1 = "The Haunting of Hill House"
library = Library()

library.add_book(book_1)
library.show_books()
library.delete_book(book_1)
library.show_books()

del library
