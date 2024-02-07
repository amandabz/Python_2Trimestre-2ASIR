"""
Ejercicio 7: Proyecto Integrador

Tarea: Desarrolla un pequeño sistema para una tienda que incluya clases para `Producto`, `Inventario`, `Carrito` y
`Cliente`. Implementa funcionalidades básicas como añadir/quitar productos al inventario, añadir productos al carrito,
y realizar una compra.

Bonus: Añade un sistema de descuentos, donde ciertos productos puedan tener un descuento y este se aplique al precio
final en el carrito.
"""


class Product:
    def __init__(self, name, price, discount=0):
        self.name = name
        self.price = price
        self.discount = discount

    def apply_discount(self):
        return self.price * (1 - self.discount / 100)


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product, quantity):
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity

    def remove_product(self, product, quantity):
        if product in self.products:
            if self.products[product] >= quantity:
                self.products[product] -= quantity
                if self.products[product] == 0:
                    del self.products[product]
            else:
                print("Error: Insufficient quantity in inventory")

        print("Error: Product not found in inventory")


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_to_cart(self, product, quantity):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def remove_from_cart(self, product, quantity):
        if product in self.items:
            if self.items[product] >= quantity:
                self.items[product] -= quantity
                if self.items[product] == 0:
                    del self.items[product]
            else:
                print("Error: Insufficient quantity in cart")

        print("Error: Product not found in cart")


class Client:
    def __init__(self, name):
        self.name = name

    def purchase(self, cart):
        total_price = sum([product.apply_discount() * quantity for product, quantity in cart.items])
        print(f"{self.name} has purchased the following items:")

        for product, quantity in cart.items():
            print(f"{quantity} {product.name} - ${product.apply_discount() * quantity}")

        print(f"Total Price: ${total_price}")


# example of use
# creating products
product1 = Product("Phone", 500)
product2 = Product("Laptop", 1000, discount=10)
product3 = Product("Headphones", 50)

# creating inventory
inventory = Inventory()
inventory.add_product(product1, 10)
inventory.add_product(product2, 5)
inventory.add_product(product3, 20)

# creating a shopping cart
cart = ShoppingCart()
cart.add_to_cart(product1, 2)
cart.add_to_cart(product2, 1)

# creating a client
client = Client("John Doe")

# making a purchase
client.purchase(cart)




