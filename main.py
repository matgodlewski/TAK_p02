# Author: Mateusz Godlewski s26524

from lexer import Lexer

with open("input.java", mode="r") as f:
    data = f.read()

lex = Lexer(data)

for token_id, token in enumerate(lex.tokens):

    if token.typ == "V_TYPE" and token_id + 1 < len(lex.tokens):
        v_name = lex.tokens[token_id + 1]
        l_paren_count = 0
        r_paren_count = 0
        l_paren_m_count = 0
        r_paren_m_count = 0
        m_param = False
        last_used = ""
        collision = False
        tok_id = 0

        for tok in lex.tokens[token_id + 2:]:
            if tok.tok == v_name.tok:
                if lex.tokens[token_id + tok_id + 1].typ == "V_TYPE":
                    collision = True
                else:
                    if not collision:
                        last_used = f"{tok.y} {tok.x}"
            elif tok.typ == "LPARENM":
                l_paren_m_count += 1

            elif tok.typ == "RPARENM":
                r_paren_m_count += 1

                if r_paren_m_count > l_paren_m_count:
                    m_param = True

            elif tok.typ == "LPARENB":
                l_paren_count += 1

            elif tok.typ == "RPARENB":
                r_paren_count += 1
                collision = False

                if (r_paren_count > l_paren_count and not m_param) or \
                        (r_paren_count == l_paren_count and m_param):
                    print(v_name.to_string() + tok.to_string() + " " + (last_used if last_used != "" else "- -"))
                    break

            tok_id += 1
