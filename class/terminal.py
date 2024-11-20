import time
from colors import RESET, BOLD_RED, BOLD_WHITE, BOLD_GREEN, BOLD_BLUE, WHITE

class Terminal:

    def validate_input(self, text, type):
        while True:
            try:
                value = type(input(text))
                return value
            except ValueError:
                print(f"{BOLD_RED}Valor inválido. Tente novamente.{RESET}")

    def validate_option(self, text, type, options):
        while True:
            try:
                value = type(input(text))
                if value in options:
                    return value
                else:
                    print(f"{BOLD_RED}Valor inválido. Tente novamente.{RESET}")
            except ValueError:
                print(f"{BOLD_RED}Valor inválido. Tente novamente.{RESET}")

    def show_initial_message(self):
        print(f'\n{BOLD_WHITE}Olá, seja bem vindo ao{RESET} {BOLD_BLUE}SUPERCLT!{RESET}\n')

        print(f'{BOLD_GREEN}1 - Abrir caixa{RESET}')
        print(f'{WHITE}2 - Finalizar{RESET}')

        return self.validate_option('\nPor favor, escolha uma das opções acima: ', int, [1,2])
    
    def show_menu(self, balance):
        print(f'\n{BOLD_WHITE}Você está iniciando seu caixa com{RESET} {BOLD_GREEN}R$ {balance}{RESET}.\n')

        print('1 - Cadastrar Produto')
        print('2 - Pesquisar Produto')
        print('3 - Remover Produto')
        print('4 - Atualizar Produto')
        print('5 - Realizar venda')
        print('6 - Fechar Caixa')

        return self.validate_option('\nPor favor, escolha uma das opções acima: ', int, [1,2,3,4,6])

    def show_final_message(self, opening_balance, ending_balance):
        print('Seu caixa está sendo fechado....')
        time.sleep(5)

        print(f'Você iniciou seu caixa com R${opening_balance}.')
        print(f'Você está fechando o caixa com R${ending_balance}.')

    