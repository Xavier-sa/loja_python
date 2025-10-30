## 📦 Projeto Loja Python: Sistema de E-commerce CLI

Este repositório contém o código-fonte de um sistema de loja virtual, desenvolvido em Python, que simula o fluxo de compra e gestão de estoque via *Command Line Interface* (CLI). O projeto é modular e utiliza estruturas de dados nativas da linguagem para a lógica de negócio.

### 💻 Tecnologias

* **Linguagem:** Python.
* **Persistência:** Arquivos **JSON** são utilizados para armazenar dados do catálogo de produtos e credenciais.

### ⚙️ Estrutura e Módulos

O projeto é organizado modularmente, com responsabilidades bem definidas:

* **`main.py`:** Ponto de entrada e orquestrador do Menu Principal.
* **`funcoes.py`:** Biblioteca de utilitários que contém funções de validação de entradas, manipulação de arquivos JSON e lógica de edição do carrinho.
* **`loja_online.py` / `loja_online_logado.py`:** Módulos que gerenciam o fluxo de navegação do cliente, visualização do catálogo, adição ao carrinho e checkout.
* **`login_cliente.py`:** Módulo dedicado à simulação do processo de login e cadastro de clientes.
* **`estoque_gerente.py`:** Módulo que implementa o painel gerencial, incluindo a lógica CRUD (Criar, Ler, Atualizar, Deletar) para produtos e relatórios de vendas.

### ✨ Funcionalidades

O sistema contém as seguintes funcionalidades operacionais:

* **Catálogo de Produtos:** Exibe uma lista de produtos disponíveis com nome, valor e quantidade em estoque.
* **Carrinho de Compras:** Permite ao usuário adicionar produtos, visualizar o resumo, editar a quantidade de itens e excluir produtos antes de finalizar o pedido.
* **Autenticação de Cliente:** Funcionalidades de Login e Cadastro para clientes, com verificação de credenciais em arquivos JSON.
* **Checkout Simulado:** Apresenta opções de pagamento (PIX, Cartão e Boleto) e simula a conclusão da transação.
* **Gerenciamento de Estoque:** Painel administrativo com autenticação, que permite:
    * Cadastrar novos produtos.
    * Editar nome, valor ou quantidade de produtos existentes.
    * Excluir produtos.
    * Gerar relatórios de vendas (Dia, Semana, Mês).