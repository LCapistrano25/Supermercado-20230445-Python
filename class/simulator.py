from supermarket_cashier import SupermarketCashier
from colors import BOLD_RED, RESET

class Simulator:
    """
    Classe para simular o funcionamento do caixa do supermercado
    """
    def __init__(self):
        self._supermarket_cashier = SupermarketCashier()
        
    def get_supermarket_cashier(self):
        """
        Método para retornar o caixa do supermercado
        """
        return self._supermarket_cashier
    
    def main(self):
        """
        Método principal para simular o funcionamento do caixa do supermercado
        """
        while True:
            option = self.get_supermarket_cashier().get_terminal().show_initial_message()

            if option == 1:
                self.get_supermarket_cashier().open_supermarket_cashier()
            elif option == 2:
                print(f'\n{BOLD_RED}Operação finalizada!{RESET}\n')
                break


if __name__ == "__main__":
    Simulator().main()
