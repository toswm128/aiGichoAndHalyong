class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_discount_price(self, sale):
        return self.price - (self.price * sale)


keyboard = Product('키보드', 50000)
print(keyboard.name, keyboard.price)
price1 = keyboard.get_discount_price(0.1)
print(price1)
