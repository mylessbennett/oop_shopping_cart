from product import Product


class ShoppingCart:

    """ Keeps track of and totals cost of products """

    def __init__(self):
        self.cart = []

    def add_product(self, product):
        self.cart.append(product)

    def remove_product(self, product):
        self.cart.remove(product)

    def total_before_tax(self):
        subtotal = 0
        for item in self.cart:
            subtotal += item.base_price
        return subtotal

    def total_after_tax(self):
        total = 0
        for item in self.cart:
            total += Product.total_price(item)
        return total


apple = Product('apple', 2, 13)
shirt = Product('shirt', 25, 13)
beer = Product('banana', 15, 15)

my_cart = ShoppingCart()
my_cart.add_product(apple)
my_cart.add_product(shirt)
my_cart.add_product(beer)
print(my_cart.cart)
print(my_cart.total_before_tax())
my_cart.remove_product(apple)
print(my_cart.cart)
print(my_cart.total_after_tax())
