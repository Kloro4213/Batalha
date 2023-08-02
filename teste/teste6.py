from sympy import sympify
 
string = '2/3 + 5/2'
print(sympify(string, evaluate=True))
print(sympify(string, evaluate=False))


expressao = "12<45"

print(exec(expressao))