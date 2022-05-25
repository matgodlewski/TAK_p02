from token import Token

V_TYPES = ['int', 'float', 'double', 'boolean', 'char', 'short', 'byte', 'long']
LITERALS = ['=']


class Lexer:
    def __init__(self, data: str):
        self.data = data.split("\n")
        self.tokens = []
        self.lexeme_count = 0
        self.lexeme_lineno = 0
        self.lex()

    def lex_num(self, line):
        num = ""
        for c in line:
            if not c.isdigit() and c != ".":
                break
            num += c
        self.lexeme_count += len(num)
        self.tokens.append(Token("V_VALUE", num, self.lexeme_count, self.lexeme_lineno))

    def lex_lparen(self):
        self.tokens.append(Token("LPAREN", "{", self.lexeme_count, self.lexeme_lineno))
        self.lexeme_count += 1

    def lex_rparen(self):
        self.tokens.append(Token("RPAREN", "}", self.lexeme_count, self.lexeme_lineno))
        self.lexeme_count += 1

    def lex_alpha(self, line):
        alpha = ""
        for c in line:
            if not c.isalpha():
                break
            alpha += c
        if len(alpha) == 1:
            self.tokens.append(Token("V_NAME", alpha, self.lexeme_count, self.lexeme_lineno))
        elif alpha == "true" or alpha == "false":
            self.tokens.append(Token("V_VALUE", alpha, self.lexeme_count, self.lexeme_lineno))
        elif alpha in V_TYPES:
            self.tokens.append(Token("V_TYPE", alpha, self.lexeme_count, self.lexeme_lineno))
        else:
            pass
        self.lexeme_count += len(alpha)

    def lex(self):
        for line in self.data:
            self.lexeme_count = 0
            self.lexeme_lineno = self.data.index(line)
            while self.lexeme_count < len(line):
                lexeme = line[self.lexeme_count]
                if lexeme.isdigit():
                    self.lex_num(line[self.lexeme_count:])
                elif lexeme == "{":
                    self.lex_lparen()
                elif lexeme == "}":
                    self.lex_rparen()
                elif lexeme.isalpha():
                    self.lex_alpha(line[self.lexeme_count:])
                else:
                    self.lexeme_count += 1
