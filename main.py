# Author: Mateusz Godlewski s26524

from lexer import Lexer

with open("input.java", mode="r") as f:
    data = f.read()

lex = Lexer(data)
index = 0

for token in lex.tokens:

    if token.typ == "V_TYPE" and index + 1 < len(lex.tokens):
        v_name = lex.tokens[index + 1]
        l_paren_count = 0
        r_paren_count = 0
        l_paren_m_count = 0
        r_paren_m_count = 0
        m_param = False

        for tok in lex.tokens[index:]:

            if tok.typ == "LPARENM":
                l_paren_m_count += 1

            elif tok.typ == "RPARENM":
                r_paren_m_count += 1

                if r_paren_m_count > l_paren_m_count:
                    m_param = True

            elif tok.typ == "LPARENB":
                l_paren_count += 1

            elif tok.typ == "RPARENB":
                r_paren_count += 1

                if (r_paren_count > l_paren_count and not m_param) or\
                        (r_paren_count == l_paren_count and m_param):
                    print(v_name.to_string() + tok.to_string() + " - -")
                    break

    index += 1
