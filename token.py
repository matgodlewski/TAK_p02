class Token:
    def __init__(self, typ, tok, x, y):
        self.typ = typ
        self.tok = tok
        self.x = x + 1
        self.y = y + 1

    def to_string(self):
        print(f"Token[ {self.typ} , {self.tok} , {self.x} , {self.y} ]")
