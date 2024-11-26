from products.eletronics import Eletronics 
from products.foods import Food
from products.utensils import Utensils

class FactoryProduct:
    """
    Classe para representar uma fábrica de produtos
    """
    @staticmethod
    def createProduct(code, name, price, quantity, param, **args):
        """
        Método para criar um produto
        """
        try:
            if param == 1:
                return Eletronics(code, name, price, quantity, args['warranty'])
            elif param == 2:
                return Food(code, name, price, quantity, args['expiration'])
            elif param == 3:
                return Utensils(code, name, price, quantity, args['expiration'])
            else:
                return F"Invalid param: {param}"
        except KeyError:
            return F"Invalid param: {param}"