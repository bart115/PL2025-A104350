# TPC2: Análise de um dataset de obras musicais

**Data:** 20/02/2025

## Autor
<img src="../bart.png" alt="bart" width="100" height="100">

- **Nome:** Gonçalo Freitas  
- **Número:** a104350  

## Descrição da Tarefa

A tarefa consistia em desenvolver um programa em Python que processasse um catálogo de obras musicais e fornecesse as seguintes funcionalidades:

1. Lista ordenada alfabeticamente dos compositores musicais
2. Distribuição das obras por período: quantas obras catalogadas em cada período
3. Dicionário em que a cada período está associada uma lista alfabética dos títulos das obras desse período

O programa precisava ler os dados de entrada a partir de um ficheiro e gerar os resultados conforme especificado.

## Processo de Desenvolvimento

### 1. Análise do Problema
Comecei por analisar o problema e os requisitos fornecidos. Identifiquei as principais funcionalidades necessárias: ordenação de compositores, contagem de obras por período, e criação de um dicionário de obras por período.

### 2. Primeira Implementação
Desenvolvi uma primeira versão do programa que lia os dados do ficheiro, processava as informações e gerava as listas e dicionários necessários.

### 3. Correções
Após testar a primeira versão, identifiquei problemas na lógica de processamento dos dados e na manipulação das listas. Refinei o algoritmo para garantir que todas as regras fossem seguidas corretamente.

### 4. Otimização da Leitura de Dados
Observei um problema com a leitura dos dados do ficheiro: o programa não estava lidando corretamente com diferentes formatos de entrada. Ajustei a implementação para garantir a correta leitura e processamento dos dados.

### 5. Testes Finais
Testei o programa com o ficheiro obras.csv e verifiquei que a saída correspondia exatamente ao esperado. As seguintes funcionalidades foram realizadas com sucesso:
- Lista ordenada alfabeticamente dos compositores musicais
- Distribuição das obras por período
- Dicionário de obras por período

## Solução Final

A solução consiste em:
- Uma função principal que processa os dados do ficheiro e gera as listas e dicionários necessários
- Lógica para ordenação de compositores
- Contagem de obras por período
- Criação de um dicionário de obras por período
- Método eficiente de leitura dos dados de entrada

## Lista de Resultados
- [Resolução](tpc2.py)
- [Dados de teste](obras.csv)
