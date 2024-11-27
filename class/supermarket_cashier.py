from stock import Stock
from terminal import Terminal
from colors import BOLD_WHITE, BOLD_CYAN, BOLD_GREEN, RESET

class SupermarketCashier:
    """ 
    Classe para simular o funcionamento do caixa do supermercado
    """
    def __init__(self):
        self._stock = Stock()
        self._terminal = Terminal()
        self._previus_balance = 0
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

    def get_previus_balance(self):
        """
        Método para retornar o saldo do caixa anterior
        """
        return self._previus_balance
    
    def set_previus_balance(self, previus_balance):
        """
        Método para setar o saldo anterior
        """
        self._previus_balance = previus_balance

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
               self._generate_report()
            elif option == 8:
                print(f'\nSeu caixa iniciou com {BOLD_GREEN}R$ {self.get_previus_balance()}{RESET}.')
                print(f'Seu caixa finalizou com {BOLD_GREEN}R$ {self.get_balance()}{RESET}.')
                self.set_previus_balance(self.get_balance())
                return

            else:
                print('Opção Inválida')

    def close_supermarket_cashier(self, opening_balance):
        """
        Método para fechar o caixa do supermercado
        """
        self.get_terminal().show_final_message(opening_balance, self.get_balance())

    def _get_product_by_search(self):
        """
        Método responsável por buscar e retornar o produto
        """
        code, quantity = self.get_terminal().show_make_sale()

        product = self.get_stock().search_product(code, name=None)

        return product, code, quantity

    def _validate_quantity_product(self, product, quantity):
        """
        Método responsável por validar a quantidade de produtos no estoque
        """
        return True if product.get_quantity() >= quantity else False
    
    def _add_product_to_cart (self, products, product, quantity):
        """
        Método responsável por adicionar o produto a lista de produtos a comprar
        """
        products[product] = quantity

    def _cancel_product(self, products):
        """
        Método responsável pelo cancelamento de um produto na venda
        """
        while True:
            # Cancelar Produto
            print('Para cancelar um produto digite os dados abaixo:\n')
            code, quantity = self.get_terminal().show_cancel_product()
            product = self.get_stock().search_product(code, name=None)
    
            if products[product] == quantity:
                del products[product]
                print('Produto removido com sucesso!\n')
                return

            elif products[product] > quantity:
                products[product] =  products[product] - quantity
                print(f'Foram cancelados {quantity} de {product.get_name()}.\n')
                return
            
            elif products[product] < quantity:
                print('Quantidade inválida!\n')
                continue

            else:
                print('Algo deu errado!\n')
                continue
        
    def _finalize_sale(self, products):
        """
        Método responsável por finalizar uma compra
        """
        self.get_terminal().show_finish_selling()
        self._remove_stock(products)
        total = self.tax_coupon(products)
        self.set_balance(self.get_balance()+total)

        print(f'{BOLD_CYAN}Compra finalizada!{RESET}')
        print(f'{BOLD_GREEN}Obrigado por comprar no SuperCLT!{RESET}\n')

    def _generate_report(self):
        """
        Método responsável por escolher o tipo de relatório
        """
        option = self.get_terminal().show_options_report()

        if option == 1:
            value = self.get_terminal().validate_input(f'\nA quantidade de produtos será (menor ou igual a):', int)
            produts = self.get_stock().search_products(quantity=value)
            self.get_terminal().show_report(produts)
        elif option == 2:
            value = self.get_terminal().validate_input(f'\nA validade do produtos será (menor ou igual a) em dias:', int)
            produts = self.get_stock().search_products(expiration=value)
            self.get_terminal().show_report(produts)
        elif option == 3:
            value = self.get_terminal().validate_input(f'\nA validade do produtos será (menor ou igual a) em anos:', int)
            produts = self.get_stock().search_products(warranty=value)
            self.get_terminal().show_report(produts, type_product=3)
        else:
            return

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
            self.tax_coupon(products)

            product, code, quantity = self._get_product_by_search()

            if not product:
                print('\nProduto não encontrado!\n')
                continue
            
            if  self._validate_quantity_product(product, quantity):
                self._add_product_to_cart (products, product, quantity)
                
                option = self.get_terminal().show_menu_selling()

                if option == 1:
                    # Adicionar mais
                    continue
                elif option == 2:
                    # Cancelar Produto
                    self._cancel_product(products)
                elif option == 3:
                    self._finalize_sale(products)
                    return
                elif option == 4:
                    # Cancelar compra
                    print('\nSua compra foi cancelada com sucesso!')
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
        print(f"\n{BOLD_WHITE}{'-' * 18} CUPOM FISCAL {'-' * 18}{RESET}")
        print(f"{BOLD_WHITE}{'Produto':<30} {'Qtd':<5} {'Preço Total':>10}{RESET}")
        print(f"{BOLD_WHITE}-{RESET}" * 50)

        # Processando os produtos
        for key, value in products.items():
            # Mostra cada produto no cupom
            self.get_terminal().show_tax_coupon(value, key.get_name(), key)
            # Adiciona o total por produto na lista
            values.append(self._calculate_total_by_product(value, key.get_price()))

        # Totalizador do cupom
        total = self._calculate_total(values)
        print(f"{BOLD_WHITE}-{RESET}" * 50)
        print(f"{BOLD_WHITE}{'TOTAL':<30} {'':<5} {RESET}{BOLD_GREEN}R${total:>10.2f}{RESET}\n")
        
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

    def _remove_stock(self, products):
        """
        Método responsável por remover as unidades do estoque
        """
        for product, quantity in products.items():
            remaining_quantity = product.get_quantity() - quantity
            self.get_stock().update_product({'quantity': remaining_quantity}, product)
    
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
            confirm = self.get_terminal().validate_option(f'Deseja confirmar a exclusão de {product.get_name()}? Digite S(Sim) ou N(Não)', str, ['S', 'N'])

            if confirm == 'S':
                self.get_stock().remove_product(product)
                print('\nProduto removido com sucesso!')
            else:
                print(f'\nOperação de deleção cancelada!')
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
