# TPC4: Analisador Léxico para linguagem query

**Data:** 02/03/2025

## Autor
<img src="../bart.png" alt="bart" width="100" height="100">

- **Nome:** Gonçalo Freitas
- **Número:** a104350   

## Descrição da Tarefa

A tarefa consistiu em desenvolver um analisador léxico em Python para uma linguagem query, identificando e categorizando diferentes tipos de tokens presentes nas consultas.

## Processo de Desenvolvimento

### 1. Análise do Problema
Analisei os requisitos e identifiquei os diferentes tipos de tokens a serem reconhecidos: comentários, palavras-chave, variáveis, strings, URIs, números, símbolos, espaços em branco e palavras genéricas.

### 2. Implementação
Desenvolvi a classe `Lexer` utilizando expressões regulares para definir e reconhecer os padrões de cada tipo de token. A classe `Token` foi criada para representar os tokens identificados.

### 3. Testes 
Testei o analisador léxico com o exemplo dado no TPC4 diretamente no ficheiro `tpc4.py`.

## Solução Final

A solução oferece:
- Classe `Lexer` que tokeniza a linguagem
- Suporte a múltiplos tipos de tokens, incluindo comentários, palavras-chave, variáveis, strings, URIs, números, símbolos, espaços em branco e palavras genéricas


## Lista de Resultados
- [Código do analisador léxico](tpc4.py)
- [Exemplo](tpc4.py)