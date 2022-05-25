# wyjscie nazwa_zmiennej | wiersz_deklaracji | kolumna_deklaracji | koniec zasiegu wiersz | ... kolumna

import ply.lex as lex

tokens = [
    'LPAREN',
    'RPAREN'
]

t_LPAREN = r'\{'
t_RPAREN = r'\}'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_error(t):
    # print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

data = open("input.java", mode="r").read()

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
