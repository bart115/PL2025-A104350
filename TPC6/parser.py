from lexer import Lexer

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class ArithmeticParser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.next_token()

    def error(self, msg):
        raise Exception(f"Erro de parsing: {msg}")

    def eat(self, token_type):
        """Consome o token atual se for do tipo esperado."""
        if self.current_token.type == token_type:
            self.current_token = self.lexer.next_token()
        else:
            self.error(f"Esperado {token_type}, encontrado {self.current_token.type}")

    def parse_E(self):
        """E → T E'"""
        result = self.parse_T()
        result = self.parse_E_prime(result)
        return result

    def parse_E_prime(self, inherited_value):
        """E' → + T E' | - T E' | ε"""
        if self.current_token.type == 'PLUS':
            self.eat('PLUS')
            temp = self.parse_T()
            result = inherited_value + temp
            return self.parse_E_prime(result)
        elif self.current_token.type == 'MINUS':
            self.eat('MINUS')
            temp = self.parse_T()
            result = inherited_value - temp
            return self.parse_E_prime(result)
        else:
            return inherited_value  # Produção ε

    def parse_T(self):
        """T → F T'"""
        result = self.parse_F()
        result = self.parse_T_prime(result)
        return result

    def parse_T_prime(self, inherited_value):
        """T' → * F T' | ε"""
        if self.current_token.type == 'TIMES':
            self.eat('TIMES')
            temp = self.parse_F()
            result = inherited_value * temp
            return self.parse_T_prime(result)
        else:
            return inherited_value  # Produção ε

    def parse_F(self):
        """F → ( E ) | num"""
        if self.current_token.type == 'NUM':
            value = int(self.current_token.value)
            self.eat('NUM')
            return value
        elif self.current_token.type == 'LPAREN':
            self.eat('LPAREN')
            result = self.parse_E()
            self.eat('RPAREN')
            return result
        else:
            self.error("Esperado número ou '('")

    def parse(self):
        """Inicia o parsing pela produção inicial E."""
        result = self.parse_E()
        if self.current_token.type != 'EOF':
            self.error("Expressão incompleta")
        return result
    
def main():
    expressao = input("Introduza uma expressão aritmética: ")
    lexer = Lexer(expressao)
    parser = ArithmeticParser(lexer)
    try:
        resultado = parser.parse()
        print(f"Resultado: {resultado}")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()