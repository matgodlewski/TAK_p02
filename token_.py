class Token:
    def __init__(self, typ: str, tok: str, x: int, y: int):
        self.typ = typ
        self.tok = tok
        self.x = x + 1
        self.y = y + 1

    def to_string(self):
        return "{} {} {}".format(self.tok, self.y, self.x)
