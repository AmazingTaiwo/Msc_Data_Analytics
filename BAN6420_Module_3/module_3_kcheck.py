class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
        def calculate_item_total(self):
            return self.price * self.quantity

item1 = ('laptop', 100, 20)
item2 = ('Phone', 1000, 50)


print(item1.calculate_item_total())
print(item2.calculate_item_total())

