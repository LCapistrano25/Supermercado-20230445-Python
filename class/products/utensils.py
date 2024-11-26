import pandas as pd
from products.product import Product

class Utensils(Product):
    """
    Classe para representar um produto de utensílios
    """
    def __init__(self, code, name, price, quantity, expiration):
        super().__init__(code, name, price, quantity)
        self._expiration = expiration

    def get_expiration(self):
        """
        Método para retornar a validade do produto  
        """
        return self._expiration
    
    def set_expiration(self, expiration):
        """
        Método para alterar a validade do produto
        """
        self._expiration = expiration

    def __str__(self):
        return pd.DataFrame(
            {
                "Código": [self.get_code()],
                "Nome": [self.get_name()],
                "Preço": [self.get_price()],
                "Quantidade": [self.get_quantity()],
                "Validade": [self.get_expiration()]
            }
        ).to_string(index=False) + "\n"