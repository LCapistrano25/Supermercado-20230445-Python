from product import Product

class Eletronics(Product):
    def __init__(self, code, name, price, quantity, warranty):
        super().__init__(code, name, price, quantity)
        self._warranty = warranty
    
    def get_warranty(self):
        return self._warranty
    
    def set_warranty(self, warranty):
        self._warranty = warranty

    def __str__(self):
        return f"\nCódigo: {self.get_code()}\nNome: {self.get_name()}\nPreço: R${self.get_price()}\nQuatidade: {self.get_quantity()} unidades\nGarantia: {self.get_warranty()}\n"