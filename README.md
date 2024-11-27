# 💻 SUPERCLT

- 🛠️ Products
- 🥗 Alimentos
- 🍴 Utensílios
- 📺 Eletrônicos
- 🏪 Supermarket Cashier
- 🏬 Stock
- 🖥️ Terminal

# 🛠️ Products
A classe Product é uma classe abstrata que serve como base para todas as outras entidades de produtos no sistema.
Ela define os atributos e métodos essenciais para qualquer produto.

🔑 Métodos Base
- Getters:
    - get_name(): Retorna o nome do produto.
    - get_code(): Retorna o código do produto.
    - get_price(): Retorna o preço do produto.
    - get_quantity(): Retorna a quantidade disponível do produto.

- Setters:
    - set_name(name): Define o nome do produto.
    - set_code(code): Define o código do produto.
    - set_price(price): Define o preço do produto.
    - set_quantity(quantity): Define a quantidade disponível do produto.

# 🥗 Foods
A classe Food representa produtos alimentícios, adicionando o atributo de validade.

- 📌 Métodos Adicionais
    - get_expiration(): Retorna a validade do produto.
    - set_expiration(expiration): Define a validade do produto.

# 🍴 Utensils
A classe Utensils é destinada a utensílios gerais, também incluindo o atributo validade.

- 📌 Métodos Adicionais
    - get_expiration(): Retorna a validade do produto.
    - set_expiration(expiration): Define a validade do produto.

# 📺 Electronics
A classe Electronics representa dispositivos eletrônicos, adicionando o atributo de garantia.

- 📌 Métodos Adicionais
    - get_warranty(): Retorna a garantia do produto.
    - set_warranty(warranty): Define a garantia do produto.

# 🏪 Supermarket Cashier

A classe `SupermarketCashier` simula o funcionamento do caixa do supermercado.

🔑 Métodos Base
- get_balance(): Retorna o saldo atual do caixa.
- set_balance(balance): Define o saldo do caixa.
- get_previus_balance(): Retorna o saldo anterior.
- set_previus_balance(previus_balance): Define o saldo anterior.
- get_terminal(): Retorna o terminal para interação com o usuário.
- get_stock(): Retorna o estoque de produtos.

📌 Métodos Adicionais
- open_supermarket_cashier(): Abre o caixa do supermercado e permite interação.
- close_supermarket_cashier(): Fecha o caixa e exibe o saldo.
- make_sale(): Realiza uma venda e atualiza o estoque.
- choose_search_option(): Escolhe uma opção para buscar produtos.
- create_product(): Cria um novo produto.
- delete_product(): Deleta um produto do estoque.
- update_product(): Atualiza as informações de um produto no estoque.

# 🏬 Stock

A classe `Stock` gerencia o estoque de produtos no supermercado.

🔑 Métodos Base
- get_products(): Retorna todos os produtos do estoque.
- add_product(product): Adiciona um novo produto ao estoque.
- remove_product(product): Remove um produto do estoque.
- update_product(updates, product): Atualiza as informações de um produto no estoque.

📌 Métodos Adicionais
- search_product(code=None, name=None): Busca um produto no estoque por código ou nome.
- show_stock(): Exibe o estoque atual de produtos.
- search_products(quantity=None, expiration=None, warranty=None): Busca produtos com base em parâmetros adicionais.
  
# 🖥️ Terminal

A classe `Terminal` é responsável pela interface de interação com o usuário no processo de vendas e gestão de estoque.

📌 Métodos
- show_initial_message(): Exibe a mensagem inicial de opções para o usuário.
- show_menu(balance): Exibe o menu principal do caixa, com opções de gerenciamento de produtos e vendas.
- show_make_sale(): Exibe a interface para fazer uma venda.
- show_search_options(): Exibe as opções de busca de produtos.
- show_create_product(): Exibe a interface para criar um novo produto.
- show_update_product(product): Exibe a interface para atualizar um produto existente.
- show_report(products): Exibe o relatório de produtos encontrados conforme a busca.
- show_tax_coupon(quantity, name, product): Exibe o cupom fiscal para um produto.
- validate_input(message, type): Valida a entrada de dados do usuário.
- validate_option(message, type, options): Valida uma opção de escolha entre um conjunto de opções.

# 🧾 Simulator
A classe `Simulator` simula o funcionamento do caixa do supermercado, interagindo com a classe `SupermarketCashier`.

🔑 Métodos Base
- get_supermarket_cashier(): Retorna o objeto do caixa do supermercado.

📌 Métodos Adicionais
- main(): Método principal que simula o funcionamento do caixa do supermercado. Exibe o menu inicial e permite ao usuário abrir o caixa ou finalizar a operação.
- Exibir a mensagem inicial e opções ao usuário.
- Abrir o caixa do supermercado ou finalizar a operação dependendo da escolha.

# 🌈 Cores

Este arquivo define as cores usadas no terminal para estilizar a saída do sistema. As cores são representadas por códigos ANSI, que são interpretados pelos terminais para alterar a cor do texto.

### Cores Normais
- `BLACK`: Cor preta.
- `RED`: Cor vermelha.
- `GREEN`: Cor verde.
- `YELLOW`: Cor amarela.
- `BLUE`: Cor azul.
- `MAGENTA`: Cor magenta.
- `CYAN`: Cor ciano.
- `WHITE`: Cor branca.
- `RESET`: Restaura a cor padrão do terminal.

### Cores em Negrito
- `BOLD_BLACK`: Preto em negrito.
- `BOLD_RED`: Vermelho em negrito.
- `BOLD_GREEN`: Verde em negrito.
- `BOLD_YELLOW`: Amarelo em negrito.
- `BOLD_BLUE`: Azul em negrito.
- `BOLD_MAGENTA`: Magenta em negrito.
- `BOLD_CYAN`: Ciano em negrito.
- `BOLD_WHITE`: Branco em negrito.

