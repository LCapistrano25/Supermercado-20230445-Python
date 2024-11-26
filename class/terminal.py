import time
from colors import RESET, BOLD_RED, BOLD_WHITE, BOLD_GREEN, BOLD_BLUE, WHITE, BOLD_YELLOW
from products.factory_product import FactoryProduct

class Terminal:
    """
    Classe para armazenar saidas de texto do terminal
    """
    def validate_input(self, text, type, is_nullable=False):
        """
        Método para validar a entrada do usuário
        """
        while True:
            try:
                value = input(f"{BOLD_WHITE}{text}{RESET} ")
                if is_nullable and value == "":
                    return None
                return type(value)
            except ValueError:
                print(f"{BOLD_RED}Valor inválido. Tente novamente.{RESET}")

    def validate_option(self, text, type, options):
        """
        Método para validar a opção do usuário
        """
        while True:
            try:
                value = type(input(f"{BOLD_WHITE}{text}{RESET} "))
                if value in options:
                    return value
                else:
                    print(f"{BOLD_RED}Valor inválido. Tente novamente.{RESET}")
            except ValueError:
                print(f"{BOLD_RED}Valor inválido. Tente novamente.{RESET}")

    def show_initial_message(self):
        """
        Método para exibir a mensagem inicial
        """
        print(f'\n{BOLD_WHITE}Olá, seja bem vindo ao{RESET} {BOLD_BLUE}SUPERCLT!{RESET}\n')

        print(f'{BOLD_GREEN}1 - Abrir caixa{RESET}')
        print(f'{WHITE}2 - Finalizar{RESET}')

        return self.validate_option('\nPor favor, escolha uma das opções acima: ', int, [1,2])
    
    def show_menu(self, balance):
        """
        Método para exibir o menu do caixa
        """
        print(f'\n{BOLD_WHITE}Você está iniciando seu caixa com{RESET} {BOLD_GREEN}R$ {balance}{RESET}.\n')

        print('1 - Cadastrar Produto')
        print('2 - Pesquisar Produto')
        print('3 - Remover Produto')
        print('4 - Atualizar Produto')
        print('5 - Realizar venda')
        print('6 - Mostrar Estoque')
        print('7 - Fechar Caixa')

        return self.validate_option('\nPor favor, escolha uma das opções acima: ', int, [1,2,3,4,5,6,7])

    def show_final_message(self, opening_balance, ending_balance):
        """
        Método para exibir a mensagem final
        """
        print('Seu caixa está sendo fechado....')
        time.sleep(5)

        print(f'Você iniciou seu caixa com R${opening_balance}.')
        print(f'Você está fechando o caixa com R${ending_balance}.')

    def show_search_options(self):
        """
        Método para exibir as opções de pesquisa
        """
        print(f'\n{BOLD_BLUE}Opções:{RESET}\n')

        print(f'{WHITE}1 - Código')
        print(f'2 - Nome{RESET}')
        print(f'{BOLD_RED}3 - Voltar{RESET}')

        return self.validate_option('\nVocê deseja pesquisar por?', int, [1,2,3])

    def show_product_type(self):
        """
        Método para exibir o tipo de produto
        """
        print(f'\n{BOLD_BLUE}Tipo do Produto:{RESET}\n')

        print(f'{WHITE}1 - Eletrônico')
        print(f'2 - Alimentos')
        print(f'3 - Utensílios{RESET}')
        print(f'{BOLD_RED}4 - Voltar{RESET}')

        return self.validate_option('\nPor favor, escolha o tipo do produto: ', int, [1,2,3,4])
    
    def show_create_product(self):
        """
        Método para exibir os campos para cadastro de produto
        """
        print(f'\n{BOLD_BLUE}Cadastro de Produto:{RESET}\n')

        show_product_type = self.show_product_type()

        if show_product_type == 4:
            return None
        
        code = self.validate_input('Código: ', int)
        name = self.validate_input('Nome: ', str)
        price = self.validate_input('Preço: ', float)
        quantity = self.validate_input('Quantidade: ', int)

        if show_product_type in [2, 3]:
            expiration = self.validate_input('Data de Validade (em dias): ', int)
            
            return FactoryProduct.createProduct(code, name, price, quantity, show_product_type, expiration=expiration)
        
        if show_product_type == 1:
            warranty = self.validate_input('Garantia (em anos): ', int)

            return FactoryProduct.createProduct(code, name, price, quantity, show_product_type, warranty=warranty)
        
    def show_update_product(self, product):
        """
        Método para exibir os campos para atualização de produto
        """
        print(f'\n{BOLD_BLUE}Atualização de Produto:{RESET}\n')

        print(f'{BOLD_WHITE}Produto selecionado:{RESET}')
        print(f'\n{BOLD_YELLOW}Código:{RESET} {product.get_code()}')
        print(f'{BOLD_YELLOW}Nome:{RESET} {product.get_name()}')
        print(f'{BOLD_YELLOW}Preço:{RESET} {product.get_price()}')
        print(f'{BOLD_YELLOW}Quantidade:{RESET} {product.get_quantity()}')

        if hasattr(product, 'get_expiration'):
            print(f'{BOLD_YELLOW}Validade:{RESET} {product.get_expiration()} dias\n')

        if hasattr(product, 'get_warranty'):
            print(f'{BOLD_YELLOW}Garantia:{RESET} {product.get_warranty()} anos\n')

        updates = {}

        fields = [
            ('code', 'Código', int),
            ('name', 'Nome', str),
            ('price', 'Preço', float),
            ('quantity', 'Quantidade', int),
        ]

        if hasattr(product, 'get_expiration'):
            fields.append(('expiration', 'Validade', int))

        if hasattr(product, 'get_warranty'):
            fields.append(('warranty', 'Garantia', int))

        for field, label, field_type in fields:
            current_value = getattr(product, f'get_{field}')()
            value = self.validate_input(
                f'{BOLD_WHITE}{label} ({current_value}){RESET} (deixe em branco para manter o mesmo): ',
                field_type,
                is_nullable=True
            )
            if value is not None:
                updates[field] = value

        return updates

    def show_make_sale(self):
        """
        Método para exibir os campos para realizar a venda
        """
        code = self.validate_input(f'{BOLD_BLUE}Digite o código do produto: {RESET}', int)
        quantity = self.validate_input(f'{BOLD_BLUE}Digite a quantidade de produto: {RESET}', int)

        return code, quantity
    
    def show_cancel_product(self):
        """
        Método para exibir os campos para cancelar produto
        """
        code = self.validate_input(f'{BOLD_YELLOW}Digite o código do produto que deseja cancelar: {RESET}', int)
        quantity = self.validate_input(f'{BOLD_YELLOW}Digite a quantidade de produto que deseja remover: {RESET}', int)

        return code, quantity
    
    def show_tax_coupon(self, value, name, key):
        """
        Exibe um item do cupom fiscal no formato correto.

        :param value: Quantidade comprada do produto.
        :param name: Nome do produto.
        :param key: Objeto do produto contendo o método get_price().
        """
        price_total = key.get_price() * value
        # Exibe o produto formatado no cupom
        print(f"{name:<30} {value:<5} R${price_total:>10.2f}")

    def show_menu_selling(self):
        """
        Método para exibir o menu de venda
        """
        print(f'{WHITE}1 - Adicionar mais')
        print(f'2 - Cancelar produto')
        print(f'3 - Finalizar compra{RESET}')
        print(f'{BOLD_RED}4 - Cancelar compra{RESET}')

        return self.validate_option('\nPor favor, escolha o tipo do produto: ', int, [1,2,3,4])
