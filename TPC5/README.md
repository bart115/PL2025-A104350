# TPC5: Máquina de Vending

**Data:** 2025-03-10

## Autor
<img src="../bart.png" alt="bart" width="100" height="100">

- **Nome:** Gonçalo Freitas
- **Número:** a104350

## Descrição da Tarefa
Desenvolver um programa em Python que simula uma máquina de vending, permitindo listar produtos, inserir moedas, selecionar produtos, adicionar produtos ao stock e sair.

## Processo de Desenvolvimento

### 1. Análise do Problema
Foi identificada a necessidade de gerir um stock de produtos num ficheiro JSON, processar comandos do utilizador e manter o estado da máquina entre execuções.

### 2. Implementação
Implementei funções para:
- Carregar e salvar o stock a partir de `stock.json`.
- Listar produtos disponíveis.
- Processar a inserção de moedas e calcular troco.
- Selecionar produtos e atualizar o stock.
- Adicionar novos produtos ao stock.

### 3. Tutorial de Utilização

Este tutorial explica como usar cada comando da máquina de vending de forma simples e prática.

#### Comando `LISTAR`
- **O que faz**: Mostra uma tabela com os produtos disponíveis, incluindo o código, nome, quantidade e preço de cada um.

#### Comando `MOEDA`
- **O que faz**: Permite adicionar moedas para acumular saldo. As moedas aceites são: `1e`, `50c`, `20c`, `10c`, `5c`, `2c`, `1c`.
- **Como usar**:
- Digite `MOEDA` seguido das moedas que quer inserir, separadas por vírgulas.
- **Exemplo**: `MOEDA 1e, 20c, 5c`
- Aqui estará a ser inserido 1 euro, 20 cêntimos e 5 cêntimos.


#### Comando `SELECIONAR`
- **O que faz**: Escolhe um produto pelo código. Se houver stock e saldo suficiente, a máquina entrega o produto e atualiza o saldo.
- **Como usar**:
- Digite `SELECIONAR` seguido do código do produto.
- **Exemplo**: `SELECIONAR A23`
- A máquina verifica:
  - Se "A23" existe (neste caso, é "água 0.5L").
  - Se há stock (por exemplo, 8 unidades).
  - Se o saldo (ex.: 1e25c) cobre o preço (0.70).
- Se tudo estiver certo, você verá: "Pode retirar o produto dispensado 'água 0.5L'" e o saldo será ajustado (ex.: `Saldo = 0e55c`).
- Se faltar saldo ou stock, aparecerá uma mensagem de erro.

#### Comando `ADICIONAR`
- **O que faz**: Adiciona um novo produto ao stock ou atualiza a quantidade e preço de um já existente.
- **Como usar**:
- Digite `ADICIONAR` seguido do código, nome, quantidade e preço.
- **Exemplo**: `ADICIONAR D56 batatas_fritas 10 1.0`
- Isso adiciona "batatas_fritas" com código "D56", 10 unidades, ao preço de 1 euro.
- A máquina confirma a adição ou atualização com uma mensagem.

#### Comando `SAIR`
- **O que faz**: Termina a interação, devolve o troco (se houver) e guarda o stock atualizado no ficheiro `stock.json`.
- **Como usar**:
- Digite `SAIR` e pressione Enter.
- **Exemplo de resposta**: Se o saldo for 0e55c, a máquina dirá: "Pode retirar o troco: 50c, 5c." e depois "Até à próxima!".

## Solução
A solução final possui as seguintes funcionalidades:
- Gestão persistente do stock através de um ficheiro JSON.
- Interface interativa com suporte aos comandos `LISTAR`, `MOEDA`, `SELECIONAR`, `ADICIONAR` e `SAIR`.

## Lista de Resultados
- [Máquina de vending](tpc5.py)
- [Ficheiro de stock (json)](stock.json)