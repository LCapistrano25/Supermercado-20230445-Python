from abc import ABC

class Product(ABC):
    def __init__(self, code, name, price, quantity):
        self._code = code
        self._name = name
        self._price = price
        self._quantity = quantity
    
    def get_code(self):
        return self._code
    
    def get_name(self):
        return self._name
    
    def get_price(self):
        return self._price
    
    def get_quantity(self):
        return self._quantity
    
    def set_code(self, code):
        self._code = code
    
    def set_name(self, name):
        self._name = name

    def set_price(self, price):
        self._price = price

    def set_quantity(self, quantity):
        self._quantity = quantity

    def __str__(self):
        return f"\nCódigo: {self._code}\nNome: {self._name}\nPreço: R${self._price}\nQuatidade: {self._quantity} unidades\n"
    