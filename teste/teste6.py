from sympy import sympify
 
string = '2/3 + 5/2'
print(sympify(string, evaluate=True))
print(sympify(string, evaluate=False))


def maracuja(self):
    print("maracujá")


expressao = "macaco.banana"

print(expressao.split("."))

expressao = "macacosozinho"

print(expressao.split("."))




class Jogador:
    def __init__(self,y=None,x=None,vida=None, cartas = {},nome=""):
        self.vida=vida
        self.vidamax = vida
        self.cartas=cartas
        self.y=y
        self.x=x
        self.nome=nome
        self.mente = None
        self.baralho = []
        self.cartasbasicas = []
        self.oponente = None


kloro = Jogador(2,3,12,None,"Kloro")


coisa = "vida"

valor = getattr(kloro,coisa)

print(valor)





