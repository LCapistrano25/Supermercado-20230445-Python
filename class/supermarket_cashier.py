from stock import Stock
from terminal import Terminal
from colors import BOLD_WHITE, RESET

class SupermarketCashier:
    """ 
    Classe para simular o funcionamento do caixa do supermercado
    """
    def __init__(self):
        self._stock = Stock()
        self._terminal = Terminal()
        self._balance = 0

    def get_balance(self):
        """
        Método para retornar o saldo do caixa
        """
        return self._balance
    
    def set_balance(self, balance):
        """
        Método para setar o saldo do caixa
        """
        self._balance = balance

    def get_terminal(self):
        """
        Método para retornar o terminal
        """
        return self._terminal
    
    def get_stock(self):
        """
        Método para retornar o estoque
        """
        return self._stock
    
    def open_supermarket_cashier(self):
        """
        Método para abrir o caixa do supermercado
        """
        while True:
            option = self.get_terminal().show_menu(self.get_balance())

            if option == 1:
                self.create_product()
            elif option == 2:
                self.choose_search_option()
            elif option == 3:
                self.delete_product()
            elif option == 4:
                self.update_product()
            elif option == 5:
                self.make_sale()
            elif option == 6:
                self.get_stock().show_stock()
            elif option == 7:
                pass
            else:
                print('Opção Inválida')

    def close_supermarket_cashier(self, opening_balance):
        """
        Método para fechar o caixa do supermercado
        """
        self.get_terminal().show_final_message(opening_balance, self.get_balance())

    def make_sale(self):
        """
        Método para realizar uma venda
        """
        # Calcular valor dos produtos com quantidade - imput
        # Realizar registro como se fosse uma NFC - 4x produto
        # Calcular total
        # Abater as unidades do estoque

        products = {}

        while True:
            subtotal = self.tax_coupon(products)

            code, quantity = self.get_terminal().show_make_sale()

            product = self.get_stock().search_product(code, name=None)

            if product:
                if  product.get_quantity() >= quantity:
                    products[product] = quantity
                    
                    option = self.get_terminal().show_menu_selling()

                    if option == 1:
                        continue
                    elif option == 2:
                        print('Para cancelar um produto digite os dados abaixo:\n')
                        code, quantity = self.get_terminal().show_cancel_product()
                        product = self.get_stock().search_product(code, name=None)

                        if products[product] == quantity:
                            del products[product]
                            print('Produto removido com sucesso!')

                        elif products[product] > quantity:
                            products[product] =  products[product] - quantity
                            print(f'Foram cancelados {quantity} de {product.get_name()}.')

                        elif products[product] < quantity:
                            print('Quantidade inválida!')
                            continue
                    elif option == 3:
                        pass
                    elif option == 4:
                        print('Sua compra foi cancelada com sucesso!')
                        return
                    else:
                        print('Opção inválida!!!')
                else:
                    print(f'Infelizmente não temos a quantidade {quantity} no estoque.\n')

    def tax_coupon(self, products):
        """
        Gera e exibe o cupom fiscal completo.

        :param products: Dicionário com objetos de produtos como chave e quantidades como valores.
        """
        values = []

        # Cabeçalho do cupom
        print(f"{'-' * 18} CUPOM FISCAL {'-' * 18}")
        print(f"{'Produto':<30} {'Qtd':<5} {'Preço Total':>10}")
        print("-" * 50)

        # Processando os produtos
        for key, value in products.items():
            # Mostra cada produto no cupom
            self.get_terminal().show_tax_coupon(value, key.get_name(), key)
            # Adiciona o total por produto na lista
            values.append(self._calculate_total_by_product(value, key.get_price()))

        # Totalizador do cupom
        total = self._calculate_total(values)
        print("-" * 50)
        print(f"{'TOTAL':<30} {'':<5} R${total:>10.2f}\n")
        
        return total
    
    def _calculate_total_by_product(self, quantity, value):
        """
        Método para calcular total de um produto
        """
        return quantity * value
    
    def _calculate_total(self, values):
        """
        Método para somar o total dos produtos
        """
        return sum(values)

    def _remove_stock_unit(self, product):
        # Receber o objeto do produto
        # Abater a quantidade
        pass
    
    def choose_search_option(self): 
        """
        Método para escolher a opção de busca de produto
        """
        while True:
            option = self.get_terminal().show_search_options()

            if option == 1:
                code = self.get_terminal().validate_input(f'\nInsira o código do produto: ', str)
                product = self.get_stock().search_product(code, name=None)   
                if product:
                    print(product)
                    return product
                return
            
            elif option == 2:
                name = self.get_terminal().validate_input(f'\nInsira o nome do produto: ', str)
                product = self.get_stock().search_product(code=None, name=name)   

                if product:
                    print(product)
                    return product
                return
            
            elif option == 3:
                return
            
    def create_product(self):
        """
        Método para criar um produto
        """
        product = self.get_terminal().show_create_product()
        
        if product:
            self.get_stock().add_product(product)
            print(self.get_stock().get_products())
            print('Produto cadastrado com sucesso!')
        else:
            print('Cadastro cancelado!')
            

    def delete_product(self):
        """
        Método para deletar um produto
        """
        product = self.choose_search_option()

        if product:
            self.get_stock().remove_product(product)
            print('Produto removido com sucesso!')
        else:
            print('Produto não encontrado!')

    def update_product(self):
        """
        Método para atualizar um produto
        """
        product = self.choose_search_option()
        
        if product:
            new_product = self.get_terminal().show_update_product(product)
            self.get_stock().update_product(new_product, product)
            print('Produto atualizado com sucesso!')
        else:
            print('Produto não encontrado!')
