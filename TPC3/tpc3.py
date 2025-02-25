import re

def markdown_to_html_regex(markdown_text):
    # Lista para armazenar as linhas HTML processadas
    html_lines = []
    in_ordered_list = False
    
    # Processar o texto linha por linha
    lines = markdown_text.split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Cabeçalhos (#)
        header_match = re.match(r'^#\s+(.+)$', line)
        if header_match:
            html_lines.append(f'<h1>{header_match.group(1)}</h1>')
            continue
            
        # Lista numerada
        list_match = re.match(r'^\d+\.\s+(.+)$', line)
        if list_match:
            if not in_ordered_list:
                html_lines.append('<ol>')
                in_ordered_list = True
            html_lines.append(f'    <li>{list_match.group(1)}</li>')
            continue
        elif in_ordered_list:
            html_lines.append('</ol>')
            in_ordered_list = False
            
        # Processar elementos inline
        processed_line = line
        
        # Links [texto](url)
        processed_line = re.sub(
            r'\[([^]]+)\]\((https?://[^)]+)\)',
            r'<a href="\2">\1</a>',
            processed_line
        )
        
        # Imagens ![texto](url)
        processed_line = re.sub(
            r'!\[([^]]+)\]\((https?://[^)]+)\)',
            r'<img src="\2" alt="\1" />',
            processed_line
        )
        
        # Negrito (**texto**)
        processed_line = re.sub(
            r'\*\*([^*]+)\*\*',
            r'<b>\1</b>',
            processed_line
        )
        
        # Itálico (*texto*)
        processed_line = re.sub(
            r'\*([^*]+)\*',
            r'<i>\1</i>',
            processed_line
        )
        
        if processed_line and not in_ordered_list:
            html_lines.append(processed_line)
    
    # Fechar lista ordenada se ainda estiver aberta
    if in_ordered_list:
        html_lines.append('</ol>')
        
    return '\n'.join(html_lines)

# Exemplo de uso
markdown = """
# Exemplo
Este é um *exemplo* com **negrito**...
1. Primeiro item
2. Segundo item
3. Terceiro item
Como pode ser consultado em [página da UC](http://www.uc.pt)
Como se vê na imagem: ![imagem dum coelho](http://www.coelho.com)
"""

html_output = markdown_to_html_regex(markdown)
print(html_output)  # Deve imprimir o texto em HTML correspondente