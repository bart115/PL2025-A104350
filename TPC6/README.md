# TPC6: Recursivo Descendente para Expressões Aritméticas

**Data:** 21/03/2025

## Autor
<img src="../bart.png" alt="bart" width="100" height="100">

- **Nome:** Gonçalo Freitas
- **Número:** a104350

## Descrição da Tarefa
A tarefa consistiu em desenvolver um parser LL(1) recursivo descendente em Python que reconheça expressões aritméticas e calcule o respetivo valor. As expressões podem incluir operadores de adição (`+`), subtração (`-`), multiplicação (`*`), parênteses e números inteiros.

## Processo de Desenvolvimento

### 1. Análise do Problema
Analisei os requisitos da tarefa, identificando a necessidade de uma gramática que suportasse expressões aritméticas com a correta precedência de operadores.

### 2. Implementação
Desenvolvi o parser utilizando funções recursivas para cada não-terminal da gramática:
- `E → T E'`
- `E' → + T E' | - T E' | ε`
- `T → F T'`
- `T' → * F T' | ε`
- `F → ( E ) | num`

Integrei o parser com um lexer que reconhece tokens como `NUM`, `PLUS`, `MINUS`, `TIMES`, `LPAREN`, `RPAREN` e `EOF`. O parser calcula o valor da expressão e detecta erros em entradas inválidas.

### 3. Tutorial de Utilização
Testei o parser com exemplos de expressões aritméticas.

#### Exemplo de Uso
- **Expressão**: `2 + 3`
  - **Resultado**: `5`
- **Expressão**: `67 - (2 + 3 * 4)`
  - **Resultado**: `55`
- **Expressão**: `(9 - 2) * (13 - 4)`
  - **Resultado**: `63`

#### Como Rodar o Código

1. Execute o programa com o comando:
   ```bash
   python3 parser.py
2. Introduza uma expressão aritmética quando solicitado

## Lista de Resultados
- [Parser da expressão aritmética](parser.py)
- [Lexer](lexer.py)