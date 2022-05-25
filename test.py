def lex_num(line):
    num = ""
    for c in line:
        if not c.isdigit():
            break
        num += c
    return 'v_value', int(num), len(num)


def lex_str(line):
    delimiter = line[0]
    string = ""
    for c in line:
        string += c
    return 'str', string, len(string)


def lex_id(line):
    keys = ['int', 'float', 'double', 'boolean', 'char', 'short', 'byte', 'long']
    id = ""
    for c in line:
        if not c.isdigit() and not c.isalpha() and c != "_":
            break
        id += c
    if id in keys:
        return 'v_type', id, len(id)
    if id == "true" or id == "false":
        return "v_value", id, len(id)
    elif len(id) == 1:
        return 'v_name', id, 1
    else:
        return 'ID', id, len(id)


def lex(line):
    lexeme_count = 0
    while lexeme_count < len(line):
        lexeme = line[lexeme_count]

        if lexeme.isdigit():
            typ, tok, consumed = lex_num(line[lexeme_count:])
            lexeme_count += consumed
            print(typ, tok, consumed)
        elif lexeme == '"' or lexeme == "'":
            typ, tok, consumed = lex_str(line[lexeme_count:])
            lexeme_count += consumed
            print(typ, tok, consumed)
        elif lexeme == "{":
            typ, tok, consumed = "LPAREN", lexeme, 1
            lexeme_count += consumed
            print(typ, tok, consumed)
        elif lexeme == "}":
            typ, tok, consumed = "RPAREN", lexeme, 1
            lexeme_count += consumed
            print(typ, tok, consumed)
        elif lexeme.isalpha():
            typ, tok, consumed = lex_id(line[lexeme_count:])
            lexeme_count += consumed
            print(typ, tok, consumed)
        else:
            lexeme_count += 1


code = input()
lex(code)
