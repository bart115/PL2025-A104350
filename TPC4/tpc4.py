import re

class Token:
    def __init__(self, type, value, line):
        self.type = type
        self.value = value
        self.line = line

    def __str__(self):
        return f'Token({self.type}, {self.value}, line={self.line})'

class Lexer:
    def __init__(self):
        # Definição dos tipos de tokens e suas expressões regulares
        self.token_specs = [
            ('COMMENT', r'#.*$'),              # Comentários (# texto)
            ('KEYWORD', r'select|where|LIMIT'), # Palavras-chave
            ('VAR', r'\?[a-zA-Z]+'),           # Variáveis (?nome)
            ('STRING', r'"[^"]*"@[a-z]{2}'),  # Strings com idioma ("texto"@en)
            ('STRING_SIMPLE', r'"[^"]*"'),     # Strings simples ("texto")
            ('URI', r'[a-z]+:[a-zA-Z]+'),      # URIs (dbo:artist)
            ('NUMBER', r'\d+'),                # Números (1000)
            ('SYMBOL', r'[{}.,]'),             # Símbolos ({ } . ,)
            ('WHITESPACE', r'\s+'),            # Espaços em branco
            ('WORD', r'[a-zA-Z]+'),            # Palavras genéricas
        ]
        # Compilar padrões regex
        self.token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in self.token_specs)

    def tokenize(self, text):
        tokens = []
        line_num = 1
        
        # Processar texto linha por linha
        for line in text.split('\n'):
            for match in re.finditer(self.token_regex, line):
                for token_type, pattern in self.token_specs:
                    value = match.group(token_type)
                    if value is not None:
                        # Ignorar whitespace
                        if token_type != 'WHITESPACE':
                            tokens.append(Token(token_type, value, line_num))
                        break
            line_num += 1
            
        return tokens

# Teste do analisador léxico
def main():
    query = """
    # DBPedia: obras de Chuck Berry
    select 
     ?nome ?desc 
    where {
     ?s a dbo:MusicalArtist .
     ?s foaf:name "Chuck Berry"@en .
     ?w dbo:artist ?s .
     ?w foaf:name ?nome .
     ?w dbo:abstract ?desc
    } LIMIT 1000
    """
    
    lexer = Lexer()
    tokens = lexer.tokenize(query)
    
    # Exibir os tokens encontrados
    for token in tokens:
        print(token)

if __name__ == "__main__":
    main()