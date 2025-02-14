def somador_on_off(texto):
    linhas = texto.split('\n')
    saida = []
    soma = 0
    somando = True
    linha_atual = ""
    
    for linha in linhas:
        i = 0
        while i < len(linha):
            # Verificar "Off" em qualquer combinação de maiúsculas e minúsculas
            if i <= len(linha) - 3 and linha[i:i+3].lower() == "off":
                linha_atual += linha[i:i+3]
                somando = False
                i += 3
                continue
            
            # Verificar "On" em qualquer combinação de maiúsculas e minúsculas
            if i <= len(linha) - 2 and linha[i:i+2].lower() == "on":
                linha_atual += linha[i:i+2]
                somando = True
                i += 2
                continue
            
            # Se estiver somando, verificar se encontrou uma sequência de dígitos
            if somando and linha[i].isdigit():
                numero = ""
                while i < len(linha) and linha[i].isdigit():
                    numero += linha[i]
                    i += 1
                linha_atual += numero
                soma += int(numero)
                continue
            
            # Verificar o caractere "="
            if linha[i] == "=":
                linha_atual += "="
                saida.append(linha_atual)
                saida.append(f">> {soma}")
                linha_atual = ""
                i += 1
                continue
            
            linha_atual += linha[i]
            i += 1
        
        # Adiciona quebra de linha, exceto na última linha
        if linha != linhas[-1]:
            linha_atual += "\n"
    
    # Adiciona o restante do texto, se houver
    if linha_atual:
        saida.append(linha_atual)
    
    # Adiciona o resultado final
    saida.append(f">> {soma}")
    
    return "\n".join(saida)

if __name__ == "__main__":
    import sys
    
    # Lê todo o input de uma vez
    entrada = sys.stdin.read()
    
    # Remove o último \n se existir
    if entrada.endswith("\n"):
        entrada = entrada[:-1]
    
    # Processa o texto e imprime o resultado
    saida = somador_on_off(entrada)
    print(saida)