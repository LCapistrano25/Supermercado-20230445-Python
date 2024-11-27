import pandas as pd
from products.eletronics import Eletronics
from products.foods import Food
from products.utensils import Utensils

class Stock:
    """
    Classe para representar o estoque
    """
    def __init__(self):
        self._products={
            1: Eletronics(1, 'Smartphone', 1000.00, 10, 1),
            2: Food(2, 'Arroz', 10.00, 100, 90),
            3: Utensils(3, 'Panela', 50.00, 50, 365),
            4: Eletronics(4, 'Notebook', 2000.00, 5, 2),
            5: Food(5, 'Feijão', 5.00, 100, 180),
        }

    def get_products(self):
        """
        Método de retorno do estoque.
        """
        return self._products
    
    def add_product(self, product):
        """
        Método para adicionar produto ao estoque.
        """
        self._products[product.get_code()]=product

    def remove_product(self, product):
        """
        Método de remover produto do estoque.
        """
        if product:
            del self.get_products()[product.get_code()] 
            return
        print('Não encontramos o produto informado!')
        return None

    def update_product(self, updates, product):
        """
        Método de atualizar um produto
        """
        if not updates:
            return None
        
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
        table = []
        print('\nEstoque atual:\n')
        for key, values in self.get_products().items():
            table.append(
                {
                    "Código": values.get_code(),
                    "Nome": values.get_name(),
                    "Preço": values.get_price(),
                    "Quantidade": values.get_quantity()
                }
            )

            if isinstance(values, Eletronics):
                table[-1]["Garantia"] = values.get_warranty()

            if isinstance(values, Food) or isinstance(values, Utensils):
                table[-1]["Validade"] = values.get_expiration()

        print( pd.DataFrame(table))

    def _search_product_code(self, code):
        """
        Método auxiliar de consulta por meio do código do produto
        """
        for key, values in self.get_products().items():
            if int(key) == int(code):
                print(30*'-')
                print('\nProduto encontrado!\n')
                return values
        print(f'\nProduto de código {code} não encontrado no estoque!')
        return None

    def _search_product_name(self, name):
        """
        Método auxiliar de consulta por meio do nome do produto
        """
        for key, values in self.get_products().items():
            if name == values.get_name():
                print(30*'-')
                print('\nProduto encontrado!\n')
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
    
    def search_products(self, quantity=None, expiration=None, warranty=None):
        products_found = []

        for key, product in self.get_products().items():
            if quantity:
                if product.get_quantity() <= quantity:
                    products_found.append(product)

            if hasattr(product, 'get_expiration') and expiration:
                if product.get_expiration() <= expiration:
                    products_found.append(product)

            if hasattr(product, 'get_warranty') and warranty:
                if product.get_warranty() <= warranty:
                    products_found.append(product)

        return products_found
