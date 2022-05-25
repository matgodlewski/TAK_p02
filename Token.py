from pprint import pprint

V_TYPES = ['int', 'float', 'double', 'boolean', 'char', 'short', 'byte', 'long']
IGNORE = [r'\n', r'\t', ' ']
LITERALS = ['=', ';']


class Token:
    def __init__(self, data):
        self.data = data.split("\n")
        self.tokens = []
        self.lexeme_lineno = 0
        self.lex()

    def lex_num(self, line):
        num = ""
        for c in line:
            if not c.isdigit():
                break
            num += c
        self.tokens.append(['v_value', num, len(num), self.lexeme_lineno + 1])

    def lex_id(self, line):
        id = ""
        for c in line:
            if not c.isdigit() and not c.isalpha() and c != "_":
                break
            id += c
        if id in KEYWORDS:
            self.tokens.append(['v_type', id, len(id), self.lexeme_lineno + 1])
        elif id == "true" or id == "false":
            self.tokens.append(['v_value', id, len(id), self.lexeme_lineno + 1])
        elif len(id) == 1:
            self.tokens.append(['v_name', id, 1, self.lexeme_lineno + 1])
        else:
            pass

    def lex(self):
        for line in self.data:
            lexeme_count = 0
            self.lexeme_lineno = self.data.index(line)
            while lexeme_count < len(line):
                lexeme = line[lexeme_count]

                if lexeme.isdigit():
                    self.lex_num(line[lexeme_count:])
                    lexeme_count += self.tokens[self.lexeme_lineno][2]
                elif lexeme == "{":
                    self.tokens.append(["LPAREN", lexeme, 1, self.lexeme_lineno])
                    lexeme_count += 1
                elif lexeme == "}":
                    self.tokens.append(["RPAREN", lexeme, 1, self.lexeme_lineno])
                    lexeme_count += 1
                elif lexeme.isalpha():
                    self.lex_id(line[lexeme_count:])
                    lexeme_count += self.tokens[self.lexeme_lineno][2]
                else:
                    lexeme_count += 1


lexer = Token(
    """
    {
    int x = 12;
    }
    """
)
pprint(lexer.tokens)
