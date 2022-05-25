from pprint import pprint

from lexer import Lexer

with open("input.java", mode="r") as f:
    data = f.read()

lex = Lexer(data)
results = []
for token in lex.tokens:
    if token.typ == "V_TYPE":
        index = lex.tokens.index(token)
        v_name = lex.tokens[index + 1]
        if v_name.typ == "V_NAME":
            l_paren_count = 0
            r_paren_count = 0
            for tok in lex.tokens[index:]:
                if tok.typ == "LPAREN":
                    l_paren_count += 1
                elif tok.typ == "RPAREN":
                    r_paren_count += 1
                    if l_paren_count < r_paren_count:
                        print(v_name.tok, v_name.y, v_name.x, tok.y, tok.x)
                        break
