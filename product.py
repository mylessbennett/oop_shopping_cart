class Product:
    """ Calculates product total price based on base price and tax rate """

    # initializes a product with name, price, and tax rate
    def __init__(self, name, base_price, tax_rate):
        self.name = name
        self.base_price = base_price
        self.tax_rate = tax_rate

    # calculates the total price of a product including tax
    def total_price(self):
        total = self.base_price + (self.base_price * (self.tax_rate / 100))
        return total
