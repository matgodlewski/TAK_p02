V_TYPES = ['int', 'float', 'double', 'boolean', 'char', 'short', 'byte', 'long']
LITERALS = ['=']


class Lexer:
    def __init__(self, data: str):
        self.data = data.split("\n")
        self.tokens = []
        self.consumed = 0
        self.lex()

    def lex_num(self, line):
        num = ""
        for c in line:
            if not c.isdigit() and c != ".":
                break
            num += c
        self.consumed += len(num)
        print(num)

    def lex_lparen(self):
        # Token l_paren
        pass

    def lex_rparen(self):
        # Token r_paren
        pass

    def lex_alpha(self, line):
        alpha = ""
        if len(line) == 1:
            print(alpha)
            self.consumed += 1
            pass
        for c in line:
            if not c.isalpha():
                break
            alpha += c
        if alpha == "true" or alpha == "false":
            print(alpha)
        elif alpha in V_TYPES:
            print(alpha)
        self.consumed = len(alpha)

    def lex(self):
        for line in self.data:
            lexeme_count = 0
            while lexeme_count < len(line):
                lexeme = line[lexeme_count]
                if lexeme.isdigit():
                    self.lex_num(line)
                    lexeme_count += self.consumed
                elif lexeme == "{":
                    self.lex_lparen()
                    lexeme_count += 1
                elif lexeme == "}":
                    self.lex_rparen()
                    lexeme_count += 1
                elif lexeme.isalpha():
                    self.lex_alpha(line)
                    lexeme_count += self.consumed
                else:
                    lexeme_count += 1


lex = Lexer("int x = 12;")
