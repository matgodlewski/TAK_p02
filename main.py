# wyjscie nazwa_zmiennej | wiersz_deklaracji | kolumna_deklaracji | koniec zasiegu wiersz | ... kolumna

import ply.lex as lex

tokens = [
    'LPAREN',
    'RPAREN',
    'INT'
]

t_LPAREN = r'\{'
t_RPAREN = r'\}'


def t_int(t):



def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_error(t):
    # print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

data = """
    public class MyClass {

    public void printThree() {

           int i = 3;
           System.out.println(i);
    }

    void printFirstTenSquares() {

         int i = 0;
         while (i <= 10) {
             int y = 3;
             printNumber(i * i, 0);
             i = i + 1;
         }
    }

     void printNumber(int x, int y) {

         System.out.println(x);
     }
}

"""

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)