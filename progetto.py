# How to create a class:
from email import message


class Item:
    name= ""
    price = 0
    quantity = 0
    def __init__(self, name:str, price:float, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        assert price >=0, f"il prezzo {price} è minore di zero!"
        assert quantity >=0, f"la quantità {price} è minore di zero!"
    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("Phone", 100, 5)
item2 = Item("laptop", 1000, 3)
print("il totale del Phone prezzo è: ")
print(item1.calculate_total_price())
print("il totale del Laptop prezzo è: ")
print(item2.calculate_total_price())
