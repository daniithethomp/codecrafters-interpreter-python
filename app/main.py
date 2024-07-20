import sys

class Token:
    def __init__(self, type, lexeme, literal, line):
        self.type = type
        self.lexeme = lexeme
        self.literaly = literal
        self.line = line
    
    def __str__(self):
        literal_str = "null" if self.literal is None else str(self.literal)
        return f"{self.type} {self.lexeme} {literal_str}"
    

class Scanner:
    def __init__(self, source):
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1
        self.errors = []

    def is_at_end(self):
        return self.current >= len(self.source)

    def scan_tokens(self):
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()
        self.tokens.append(Token("EOF", "", None, self.line))
        return self.tokens, self.errors
    
    def scan_token(self):
        c = self.advance()
        match c:
            case "(":
                self.add_token("LEFT_PAREN")
            case ")":
                self.add_token("RIGHT_PAREN")
            case "{":
                self.add_token("LEFT_BRACE")
            case "}":
                self.add_token("RIGHT_BRACE")
            case "*":
                self.add_token("STAR")
            case ".":
                self.add_token("DOT")
            case ",":
                self.add_token("COMMA")
            case "+":
                self.add_token("PLUS")
            case "-":
                self.add_token("MINUS")
            case ";":
                self.add_token("SEMICOLON")
            case "=":
                if self.match("="):
                    self.add_token("EQUAL_EQUAl")
                else:
                    self.add_token("EQUAL")
            case _:
                self.error(f"Unexpected character: {c}")

    def match(self, expected):
        if self.current >= len(self.source):
            return False
        if self.source[self.current] != expected:
            return False
        
        self.current += 1
        return True
    
    def add_token(self, type, literal=None):
        token = self.source[self.start : self.current]
        self.tokens.append(Token(type, token, literal, self.line))
    
    def error(self, message):
        self.errors.append(f"[line {self.line}] Error: {message}")
    
    def advance(self):
        self.current += 1
        return self.source[self.current - 1]

def main():
    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    with open(filename) as file:
        file_contents = file.read()

    scanner = Scanner(file_contents)
    tokens, errors = scanner.scan_tokens()

    for token in tokens:
        print(token)

    for error in errors:
        print(error, file=sys.stderr)

    if errors:
        exit(65)

if __name__ == "__main__":
    main()