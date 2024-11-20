from stock import Stock
from terminal import Terminal

class SupermarketCashier:
    def __init__(self):
        self._stock = Stock()
        self._terminal = Terminal()
        self._balance = 0

    def get_balance(self):
        return self._balance
    
    def set_balance(self, balance):
        self._balance = balance

    def get_terminal(self):
        return self._terminal
    
    def open_supermarket_cashier(self):
        while True:
            option = self.get_terminal().show_menu(self.get_balance())

            if option == 1:
                pass
            elif option == 2:
                pass
            elif option == 3:
                pass
            elif option == 4:
                pass
            elif option == 5:
                pass
            elif option == 6:
                pass
            else:
                print('Opção Inválida')

    def close_supermarket_cashier(self, opening_balance):
        self.get_terminal().show_final_message(opening_balance, self.get_balance())

    def make_sale(self):
        # Calcular valor dos produtos com quantidade - imput
        # Realizar registro como se fosse uma NFC - 4x produto
        # Calcular total
        # Abater as unidades do estoque
        pass

    def tax_coupon(self, products):
        # Vai receber uma lista com a quantidade comprada e o objeto
        # Mostrar o cupom
        pass

    def _calculate_total_by_product(self, quantity, value):
        # Calcular o total por produto
        # Retornar o valor
        pass

    def _calculate_total(self, values):
        # Recebe uma lista e calcular o total
        # retorna o total
        pass

    def _remove_stock_unit(self, product):
        # Receber o objeto do produto
        # Abater a quantidade
        pass
    