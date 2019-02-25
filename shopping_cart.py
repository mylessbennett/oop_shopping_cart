from product import Product


class ShoppingCart:

    """ Keeps track of and totals cost of products """

    def __init__(self):
        self.cart = []

    # method to add a product to the cart
    def add_product(self, product):
        self.cart.append(product)

    # method to remove a product to the cart
    def remove_product(self, product):
        self.cart.remove(product)

    # calculates the total price of products in cart before tax
    def total_before_tax(self):
        subtotal = 0
        for item in self.cart:
            subtotal += item.base_price
        return subtotal

    # calculates the total price of items in the cart using the total price
    # method from Product class
    def total_after_tax(self):
        total = 0
        for item in self.cart:
            total += Product.total_price(item)
        return total


# Testing
apple = Product('apple', 2, 13)
shirt = Product('shirt', 25, 13)
beer = Product('banana', 15, 15)

my_cart = ShoppingCart()
my_cart.add_product(apple)
my_cart.add_product(shirt)
my_cart.add_product(beer)
my_cart.remove_product(apple)
print('------------------')
for item in my_cart.cart:
    print("{}: ${:.2f}".format(item.name, item.base_price))

print('------------------')
print("Subtotal: ${:.2f}".format(my_cart.total_before_tax()))
print('------------------')
print("Total: ${:.2f}".format(my_cart.total_after_tax()))
print('------------------')
