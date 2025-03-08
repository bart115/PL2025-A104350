import json
import os
from datetime import datetime

# Nome do ficheiro de stock
STOCK_FILE = 'stock.json'

# Valores das moedas em cêntimos
MOEDAS = {
    '1e': 100,
    '50c': 50,
    '20c': 20,
    '10c': 10,
    '5c': 5,
    '2c': 2,
    '1c': 1
}

def carregar_stock():
    """Carrega o stock do ficheiro JSON."""
    if os.path.exists(STOCK_FILE):
        with open(STOCK_FILE, 'r') as f:
            return json.load(f)
    return []  # Retorna lista vazia se o ficheiro não existir

def salvar_stock(stock):
    """Salva o stock no ficheiro JSON."""
    with open(STOCK_FILE, 'w') as f:
        json.dump(stock, f, indent=4)

def listar_produtos(stock):
    """Lista os produtos disponíveis."""
    print("cod | nome | quantidade | preço")
    for produto in stock:
        print(f"{produto['cod']} | {produto['nome']} | {produto['quant']} | {produto['preco']:.2f}")

def adicionar_moedas(saldo, moedas_str):
    """Adiciona moedas ao saldo."""
    moedas = moedas_str.split(',')
    for moeda in moedas:
        moeda = moeda.strip().lower()
        if moeda in MOEDAS:
            saldo += MOEDAS[moeda]
        else:
            print(f"Moeda inválida: {moeda}")
    return saldo

def selecionar_produto(stock, saldo, cod):
    """Seleciona um produto e dispensa se possível."""
    for produto in stock:
        if produto['cod'] == cod:
            if produto['quant'] > 0:
                preco_centimos = int(produto['preco'] * 100)  # Converte preço para cêntimos
                if saldo >= preco_centimos:
                    produto['quant'] -= 1
                    saldo -= preco_centimos
                    print(f"maq: Pode retirar o produto dispensado \"{produto['nome']}\"")
                    return saldo
                else:
                    print("maq: Saldo insuficiente para satisfazer o seu pedido")
                    print(f"maq: Saldo = {saldo // 100}e{saldo % 100}c; Pedido = {produto['preco']:.2f}e")
                    return saldo
            else:
                print(f"maq: Produto \"{produto['nome']}\" esgotado")
                return saldo
    print(f"maq: Produto com código {cod} não encontrado")
    return saldo

def calcular_troco(saldo):
    """Calcula o troco a devolver."""
    if saldo == 0:
        return "maq: Sem troco a devolver."
    troco = []
    for nome, valor in sorted(MOEDAS.items(), key=lambda x: x[1], reverse=True):
        while saldo >= valor:
            troco.append(nome)
            saldo -= valor
    return f"maq: Pode retirar o troco: {', '.join(troco)}."

def adicionar_produto(stock, cod, nome, quant, preco):
    """Adiciona ou atualiza um produto no stock."""
    for produto in stock:
        if produto['cod'] == cod:
            produto['quant'] += quant
            produto['preco'] = preco
            print(f"maq: Produto {cod} atualizado: +{quant} unidades, novo preço {preco:.2f}e")
            return
    stock.append({"cod": cod, "nome": nome, "quant": quant, "preco": preco})
    print(f"maq: Produto {cod} adicionado: {nome}, {quant} unidades, {preco:.2f}e")

def main():
    stock = carregar_stock()
    print(f"maq: {datetime.now().strftime('%Y-%m-%d')}, Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")
    
    saldo = 0
    while True:
        comando = input(">> ").strip().upper()
        if comando == "LISTAR":
            listar_produtos(stock)
        elif comando.startswith("MOEDA"):
            moedas_str = comando[6:].strip()
            saldo = adicionar_moedas(saldo, moedas_str)
            print(f"maq: Saldo = {saldo // 100}e{saldo % 100}c")
        elif comando.startswith("SELECIONAR"):
            cod = comando[11:].strip()
            saldo = selecionar_produto(stock, saldo, cod)
            print(f"maq: Saldo = {saldo // 100}e{saldo % 100}c")
        elif comando == "SAIR":
            print(calcular_troco(saldo))
            print("maq: Até à próxima")
            salvar_stock(stock)
            break
        elif comando.startswith("ADICIONAR"):
            partes = comando.split()
            if len(partes) == 5:
                cod = partes[1]
                nome = partes[2]
                quant = int(partes[3])
                preco = float(partes[4])
                adicionar_produto(stock, cod, nome, quant, preco)
            else:
                print("maq: Uso: ADICIONAR <cod> <nome> <quant> <preco>")
        else:
            print("maq: Comando inválido. Use LISTAR, MOEDA, SELECIONAR, ADICIONAR ou SAIR.")

if __name__ == "__main__":
    main()