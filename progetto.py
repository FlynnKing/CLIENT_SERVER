# How to create a class:
from email import message


class Item:
    name= ""
    price = 0
    quantity = 0
    def __init__(self, name:str, price:float, quantity=0):
        self.price = 2374
        self.quantity = 10
        if quantity>0 or price>0:
            print("la quantità e il prezzo sono maggiori di zero!!")
        
    def calculate_total_price(x, y):
        return x * y

item1 = Item
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
print("il totale del Phone prezzo è: ")
print(item1.calculate_total_price(item1.price, item1.quantity))
item2 = Item
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3
print("il totale del Laptop prezzo è: ")
print(item2.calculate_total_price(item2.price, item2.quantity))