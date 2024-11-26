from abc import ABC

class Product(ABC):
    """
    Classe abstrata para representar um produto
    """
    def __init__(self, code, name, price, quantity):
        self._code = code
        self._name = name
        self._price = price
        self._quantity = quantity
    
    def get_code(self):
        """
        Método para retornar o código do produto
        """
        return self._code
    
    def get_name(self):
        """
        Método para retornar o nome do produto
        """
        return self._name
    
    def get_price(self):
        """
        Método para retornar o preço do produto
        """
        return self._price
    
    def get_quantity(self):
        """
        Método para retornar a quantidade do produto
        """
        return self._quantity
    
    def set_code(self, code):
        """
        Método para alterar o código do produto 
        """
        self._code = code
    
    def set_name(self, name):
        """
        Método para alterar o nome do produto
        """
        self._name = name

    def set_price(self, price):
        """
        Método para alterar o preço do produto
        """
        self._price = price

    def set_quantity(self, quantity):
        """
        Método para alterar a quantidade do produto
        """
        self._quantity = quantity

    def __str__(self):
        return f"\nCódigo: {self._code}\nNome: {self._name}\nPreço: R${self._price}\nQuatidade: {self._quantity} unidades\n"
    