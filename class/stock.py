from products.eletronics import Eletronics
from products.foods import Food

class Stock:
    def __init__(self):
        self._product={}

    def get_products(self):
        """
        Método de retorno do estoque.
        """
        return self._product
    
    def add_product(self, product):
        """
        Método para adicionar produto ao estoque.
        """
        self._product[product.get_code()]=product

    def remove_product(self, code=None, name=None):
        """
        Método de remover produto do estoque.
        """
        if not self._error_or_empty(code, name):
            return None
        product = self.search_product(code, name)
        if product:
            del self.get_products()[product.get_code()] 
            print(product)
            return
        print('Não encontramos o produto informado!')
        return None

    def update_product(self, updates, code=None, name=None):
        """
        Método de atualizar um produto
        """
        if not self._error_or_empty(code, name):
            return None
        if not updates:
            return None
        
        product = self.search_product(code, name)
        if product:
            self._update_product(product, updates)
            return 
        print('Não foi possível atualizar o produto!')
        return
    
    def _update_product(self, product, updates):
        """
        Método de atualização dinâmica do produto

            - O método itera sobre casa item dentro do dicionário de atualização.
            - Ao iterar ele captura os possíveis métodos get e set de cada classe
            - O método verifica se existe os métodos dentro da classe
            - Se existir ele atualiza por meio do método gettattr
        """
        for attribute, new_value in updates.items():
            getter_method = f"get_{attribute}"
            setter_method = f"set_{attribute}"
            
            if hasattr(product, setter_method) and hasattr(product, getter_method):
                getattr(product, setter_method)(new_value)
                print(f"Atributo '{attribute}' atualizado para '{new_value}'.")
            else:
                print(f"Atributo '{attribute}' não encontrado ou não pode ser atualizado no produto.")
        return None

    def search_product(self, code=None, name=None):
        """
        Método de consulta
        """
        if not self._error_or_empty(code, name):
            return None
        
        if code:
            product = self._search_product_code(code)
            return product
        if name:
            product = self._search_product_name(name)
            return product
        return None
    
    def show_stock(self):
        """
        Método de exibição do estoque
        """
        print('\nEstoque atual:')
        for key, values in self.get_products().items():
            print(values)
        return None

    def _search_product_code(self, code):
        """
        Método auxiliar de consulta por meio do código do produto
        """
        for key, values in self.get_products().items():
            if key == code:
                print(values)
                return values
        print(f'\nProduto de código {code} não encontrado no estoque!')
        return None

    def _search_product_name(self, name):
        """
        Método auxiliar de consulta por meio do nome do produto
        """
        for key, values in self.get_products().items():
            if name == values.get_name():
                print(values)
                return values
        print(f'\nProduto {name} não encontrado no estoque!')
        return None
    
    def _error_or_empty(self, code=None, name=None):
        """
        Método para retornar erros ou variáveis vazias
        """
        if not code and not name:
            print('Consulta inválida, insira os parâmentros solicitados!')
            return False
        return True