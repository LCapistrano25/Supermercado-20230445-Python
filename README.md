# 💻 SUPERCLT

. 🥗 Alimentos
. 🍴 Utensílios
. 📺 Eletrônicos

# 📂 Estrutura do Projeto

# 🛠️ Products
A classe Product é uma classe abstrata que serve como base para todas as outras entidades de produtos no sistema.
Ela define os atributos e métodos essenciais para qualquer produto.

🔑 Métodos Base
- Getters:
. get_name(): Retorna o nome do produto.
. get_code(): Retorna o código do produto.
. get_price(): Retorna o preço do produto.
. get_quantity(): Retorna a quantidade disponível do produto.

- Setters:
. set_name(name): Define o nome do produto.
. set_code(code): Define o código do produto.
. set_price(price): Define o preço do produto.
. set_quantity(quantity): Define a quantidade disponível do produto.

# 🥗 Foods
A classe Food representa produtos alimentícios, adicionando o atributo de validade.

- 📌 Métodos Adicionais
. get_expiration(): Retorna a validade do produto.
. set_expiration(expiration): Define a validade do produto.

# 🍴 Utensils
A classe Utensils é destinada a utensílios gerais, também incluindo o atributo validade.

- 📌 Métodos Adicionais
. get_expiration(): Retorna a validade do produto.
. set_expiration(expiration): Define a validade do produto.

# 📺 Electronics
A classe Electronics representa dispositivos eletrônicos, adicionando o atributo de garantia.

- 📌 Métodos Adicionais
. get_warranty(): Retorna a garantia do produto.
. set_warranty(warranty): Define a garantia do produto.
