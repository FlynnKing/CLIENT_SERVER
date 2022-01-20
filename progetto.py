# How to create a class:
from email import message


class Item:
    pay_rate = 0
    all_items = [] #lista delle istanze
    def __init__(self, name:str, price:float, quantity=0, ):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all_items.append()
        assert price >=0, f"il prezzo {price} è minore di zero!"
        assert quantity >=0, f"la quantità {price} è minore di zero!"
    def calculate_total_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.pay_rate = input("inserisci lo sconto tra 0 e 1(float): ") 

        return self.price 
    def __repr__(self) -> str:
        pass

item1 = Item("Phone", 100, 5)
item2 = Item("laptop", 1000, 3)
print("il totale del Phone prezzo è: ")
print(item1.calculate_total_price())
print("il totale del Laptop prezzo è: ")
print(item2.calculate_total_price())

+