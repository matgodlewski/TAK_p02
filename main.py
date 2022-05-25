from lexer import Lexer

with open("input.java", mode="r") as f:
    data = f.read()

lex = Lexer(data)

for token in lex.tokens:
    token.to_string()