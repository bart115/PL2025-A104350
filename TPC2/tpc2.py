import re
from collections import defaultdict

def parse_obras_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()

    # Regular expression to match the pattern of the CSV fields
    pattern = re.compile(r'(?P<nome>[^\n;]+);(?P<desc>\".*?\"|[^;]+);(?P<anoCriacao>\d+);(?P<periodo>[^;]+);(?P<compositor>[^;]+);(?P<duracao>\d{2}:\d{2}:\d{2});(?P<_id>O\d+)')
    
    # Find all matches in the data
    matches = pattern.finditer(data)
    
    # Parse the matches into a list of dictionaries
    parsed_data = []
    for match in matches:
        entry = match.groupdict()
        # Clean up the 'nome' field to remove unwanted newlines and leading/trailing spaces
        entry['nome'] = entry['nome'].strip()
        parsed_data.append(entry)
    
    return parsed_data

def get_sorted_composers(file_path):
    # Parse the CSV to get the data
    parsed_data = parse_obras_csv(file_path)
    
    # Extract the names of the composers, handling multiple composers per entry
    composers = []
    for entry in parsed_data:
        # Split composers by comma and strip any extra whitespace
        composers.extend([composer.strip() for composer in entry['compositor'].split(',')])
    
    # Remove duplicates and sort the list alphabetically
    sorted_composers = sorted(set(composers))
    
    return sorted_composers

def get_works_distribution_by_period(file_path):
    # Parse the CSV to get the data
    parsed_data = parse_obras_csv(file_path)
    
    # Count the number of works in each period
    period_distribution = defaultdict(int)
    for entry in parsed_data:
        period_distribution[entry['periodo']] += 1
    
    return period_distribution

# Nao funfa 
def get_works_by_period(file_path):
    # Parse the CSV to get the data
    parsed_data = parse_obras_csv(file_path)
    
    # Create a dictionary to store works by period
    works_by_period = defaultdict(list)
    for entry in parsed_data:
        works_by_period[entry['periodo']].append(entry['nome'])
    
    # Sort the lists of works alphabetically for each period
    for period in works_by_period:
        works_by_period[period] = sorted(works_by_period[period])
    
    return works_by_period

# Example usage
file_path = '/home/bart/Desktop/PL2025-A104350/TPC2/obras.csv'
sorted_composers = get_sorted_composers(file_path)
print("Compositores em ordem alfabética:")
print(sorted_composers)

# Get and print works distribution by period
works_distribution = get_works_distribution_by_period(file_path)
print("\nDistribuição das obras por período:")
for period, count in works_distribution.items():
    print(f"{period}: {count} obras")

# Get and print works by period (não funciona)
works_by_period = get_works_by_period(file_path)
print("\nObras por período:")
for period, works in works_by_period.items():
    print(f"{period}:")
    for work in works:
        print(f"  - {work}")