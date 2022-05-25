from lexer import Lexer

with open("input.java", mode="r") as f:
    data = f.read()

lex = Lexer(data)
results = []
for token in lex.tokens:
    if token.typ == "V_TYPE":
        index = lex.tokens.index(token)
        v_name = lex.tokens[index + 1]
        l_paren_count = 0
        r_paren_count = 0
        for tok in lex.tokens[index:]:
            if tok.typ == "LPAREN":
                l_paren_count += 1
            elif tok.typ == "RPAREN":
                if l_paren_count < r_paren_count:
                    print(v_name.tok, v_name.x, v_name.y, tok.x, tok.y)
                r_paren_count += 1


