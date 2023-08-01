import re

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
    
    def receberVida(self,valor):
        self.vida += valor
        if self.vida > self.vidamax: self.vida = self.vidamax

    def perderVida(self,valor):
        self.vida -= valor

    def condicao(self,criterio,sim,nao):
        if criterio: eval(sim)
        if not criterio: eval(nao)


class Inimigo:
    def __init__(self,y=None,x=None,vida=None,cartas = {},nome=""):
        self.vidamax = vida
        self.vida=vida
        self.cartas=cartas
        self.y=y
        self.x=x
        self.nome=nome
        self.mente = None
        self.baralho = []
        self.cartasbasicas = []
        self.desvio = 0
        self.bloqueio = 0
        self.status = {}

    def receberVida(self,valor):
        self.vida += valor
        if self.vida > self.vidamax: self.vida = self.vidamax
    def perderVida(self,valor):
        self.vida -= valor
    def acessarVida(self):
        return self.vida
    def definirVida(self,valor):
        self.vida = valor
    def condicao(self,criterio,sim,nao):
        if criterio: eval(sim)
        if not criterio: eval(nao)


kloro = Jogador(0,0,100,None,"Kloro")
lutecio = Inimigo(0,0,100,None,"Lutécio")

jogador = kloro
inimigo = lutecio


ganhar = "receberVida(23)"
perder = "perderVida(69)"
trick = "condicao()"


def resolver(coisa,negocio):
    valor = re.findall(r'\(\d*\)',negocio)[0]
    efeitoreal = negocio.replace(valor,"")
    valor = valor.replace("(","").replace(")","")
    valor = int(valor)
    funcao = getattr(coisa, efeitoreal)
    funcao(valor)
    
    

print(jogador.vida)


resolver(jogador,perder)



print(jogador.vida)

resolver(jogador,ganhar)



print(jogador.vida)

resolver(jogador,perder)

print(jogador.vida)

jogador.condicao(jogador.vida<40,"jogador.receberVida(90)","jogador.perderVida(90)")

print(jogador.vida)
