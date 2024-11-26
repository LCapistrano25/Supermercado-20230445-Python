import pandas as pd
from products.product import Product

class Eletronics(Product):
    """
    Classe para representar um produto eletrônico
    """
    def __init__(self, code, name, price, quantity, warranty):
        super().__init__(code, name, price, quantity)
        self._warranty = warranty
    
    def get_warranty(self):
        """
        Método para retornar a garantia do produto eletrônico
        """
        return self._warranty
    
    def set_warranty(self, warranty):
        """
        Método para alterar a garantia do produto eletrônico
        """
        self._warranty = warranty

    def __str__(self):
        return "\n" + pd.DataFrame(
            {
                "Código": [self.get_code()],
                "Nome": [self.get_name()],
                "Preço": [self.get_price()],
                "Quantidade": [self.get_quantity()],
                "Garantia": [self.get_warranty()]
            }
        ).to_string(index=False) + "\n"