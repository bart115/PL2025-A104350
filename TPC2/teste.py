import re
from collections import defaultdict

def parse_obras_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Ignorar o cabeçalho
    if lines and lines[0].startswith('nome;desc;anoCriacao;periodo;compositor;duracao;_id'):
        lines = lines[1:]

    # Pré-processar o CSV para juntar linhas quebradas
    data = []
    current_line = ""
    for line in lines:
        # Contar os campos esperados (7: nome, desc, anoCriacao, periodo, compositor, duracao, _id)
        fields = line.split(';')
        if len(fields) >= 7 and fields[-1].startswith('O'):  # Verificar se termina com _id (O\d+)
            if current_line:
                data.append(current_line.strip())
            current_line = line
        else:
            current_line += " " + line.strip()
    if current_line:
        data.append(current_line.strip())

    # Expressão regular ajustada
    pattern = re.compile(
        r'(?P<nome>[^;\n]+?);'  # Captura até o primeiro ;, evitando quebras de linha
        r'(?P<desc>.*?);'       # Captura tudo até o próximo ; (inclui quebras de linha)
        r'(?P<anoCriacao>\d+);'
        r'(?P<periodo>[^;]+);'
        r'(?P<compositor>[^;]+);'
        r'(?P<duracao>\d{2}:\d{2}:\d{2});'
        r'(?P<_id>O\d+)',
        re.DOTALL
    )
    
    parsed_data = []
    for entry in data:
        match = pattern.match(entry)
        if match:
            entry_dict = match.groupdict()
            entry_dict['nome'] = entry_dict['nome'].strip()
            entry_dict['desc'] = entry_dict['desc'].strip()
            parsed_data.append(entry_dict)
        else:
            print(f"Erro ao parsear: {entry[:100]}...")  # Imprimir parte da linha para depuração

    return parsed_data

def get_works_by_period(file_path):
    # Parsear o CSV para obter os dados
    parsed_data = parse_obras_csv(file_path)
    
    # Criar um dicionário para armazenar obras por período
    works_by_period = defaultdict(list)
    
    # Adicionar apenas os títulos das obras ao dicionário
    for entry in parsed_data:
        title = entry['nome'].strip()
        period = entry['periodo'].strip()
        works_by_period[period].append(title)
    
    # Ordenar alfabeticamente as listas de obras para cada período
    for period in works_by_period:
        works_by_period[period] = sorted(works_by_period[period])
    
    return dict(works_by_period)

# Exemplo de uso
file_path = '/home/bart/Desktop/PL2025-A104350/TPC2/obras.csv'
works_by_period = get_works_by_period(file_path)

# Imprimir as obras por período
print("\nObras por período:")
for period, works in works_by_period.items():
    print(f"{period}:")
    for work in works:
        print(f"  - {work}")