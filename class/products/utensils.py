from products.product import Product

class Utensils(Product):
    def __init__(self, code, name, price, quantity, expiration):
        super().__init__(code, name, price, quantity)
        self._expiration = expiration

    def get_expiration(self):
        return self._expiration
    
    def set_expiration(self, expiration):
        self._expiration = expiration

    def __str__(self):
        return f"\nCódigo: {self.get_code()}\nNome: {self.get_name()}\nPreço: R${self.get_price()}\nQuatidade: {self.get_quantity()} unidades\nValidade: {self.get_expiration()}\n"