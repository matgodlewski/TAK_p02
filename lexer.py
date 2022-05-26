from token_ import Token

V_TYPES = ['int', 'float', 'double', 'boolean', 'char', 'short', 'byte', 'long']


class Lexer:
    def __init__(self, data: str):
        self.data = data
        self.tokens = []
        self.lexeme_count = 0
        self.lexeme_lineno = 0
        self.consumed = 0
        self.lex()

    def add_token(self, typ: str, tok: str = ""):
        self.tokens.append(
            Token(
                typ,
                tok,
                self.lexeme_count,
                self.lexeme_lineno
            )
        )

    def lex_alpha(self):
        alpha = ""
        for c in self.data[self.consumed:]:
            if not c.isalpha():
                break
            alpha += c
        if len(alpha) == 1:
            self.add_token("V_NAME", alpha)
        elif alpha in V_TYPES:
            self.add_token("V_TYPE")
        self.lexeme_count += len(alpha)
        self.consumed += len(alpha)

    def next_c(self):
        self.lexeme_count += 1
        self.consumed += 1

    def lex(self):
        for lexeme in self.data:
            if self.data[self.consumed] == '\n':
                self.lexeme_lineno += 1
                self.consumed += 1
                self.lexeme_count = 0
            elif lexeme == "{":
                self.add_token("LPARENB")
                self.next_c()
            elif lexeme == "}":
                self.add_token("RPARENB")
                self.next_c()
            elif lexeme == "(":
                self.add_token("LPARENM")
                self.next_c()
            elif lexeme == ")":
                self.add_token("RPARENM")
                self.next_c()
            elif lexeme.isalpha():
                self.lex_alpha()
            else:
                self.lexeme_count += 1
                self.consumed += 1
