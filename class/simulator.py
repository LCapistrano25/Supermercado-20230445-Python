from supermarket_cashier import SupermarketCashier
from colors import BOLD_RED, RESET

class Simulator:
    def __init__(self):
        self._supermarket_cashier = SupermarketCashier()

    def get_supermarket_cashier(self):
        return self._supermarket_cashier
    
    def main(self):
        while True:
            option = self.get_supermarket_cashier().get_terminal().show_initial_message()

            if option == 1:
                self.get_supermarket_cashier().open_supermarket_cashier()
            elif option == 2:
                print(f'\n{BOLD_RED}Operação finalizada!{RESET}\n')
                break


if __name__ == "__main__":
    Simulator().main()
