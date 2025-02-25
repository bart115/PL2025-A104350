# TPC3: Conversor de Markdown para HTML

**Data:** 23/02/2025

## Autor
<img src="../bart.png" alt="bart" width="100" height="100">

- **Nome:** Gonçalo Freitas
- **Número:** a104350   

## Descrição da Tarefa

A tarefa consistiu em desenvolver um programa em Python que convertesse texto Markdown para HTML, suportando elementos da "Basic Syntax": cabeçalhos, negrito, itálico, listas numeradas, links e imagens.

## Processo de Desenvolvimento

### 1. Análise do Problema
Analisei os requisitos e identifiquei os elementos Markdown a converter: #, **, *, listas numeradas, [texto](url) e ![texto](url).

### 2. Implementação
Desenvolvi utilizando expressões regulares para parsing mais robusto e conciso dos padrões Markdown.

### 4. Testes 
Testei com um texto em md diretamente no ficheiro tpc3.py

## Solução Final

A solução oferece:
- Função que converte Markdown para HTML
- Suporte a cabeçalhos, formatação, listas, links e imagens
- Processamento eficiente de texto multilinha

## Lista de Resultados
- [Resolução com regex](tpc3.py)
- [Exemplo de entrada](tpc3.py)