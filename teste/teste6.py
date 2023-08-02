from sympy import sympify
 
string = '2/3 + 5/2'
print(sympify(string, evaluate=True))
print(sympify(string, evaluate=False))


def maracuja(self):
    print("maracujá")


expressao = "12<45"

print(sympify(expressao))


expressao = "maracuja()"

sympify(expressao)