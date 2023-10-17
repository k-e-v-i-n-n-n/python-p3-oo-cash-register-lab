#!/usr/bin/env python3

class CashRegister:

    def __init__(self, discount = 0, total = 0.0, items = None):
        self.discount = discount
        self.total = total
        if items == None:
          self.items = []
        else:
            self.items = items

    def add_item(self, title, price, quantity = 1):
        self.title = title
        self.price = price
        self.quantity = quantity
        self.total += (price * quantity)
    
    def apply_discount(self):
        disc_per = float(self.discount) / 100
        self.total = self.total - (self.total * disc_per)
        print(f"After the discount, the total comes to ${int(self.total)}.\n")
        
        
