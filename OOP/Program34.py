class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    def __gt__(self, Order2):
        return self.price > Order2.price
Order1 = Order("Cup", 200)
Order2 = Order("Toy", 50)
print(Order1 > Order2)
        