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
        self.oponente = None
    
    def receberVida(self,valor):
        self.vida += int(int(valor))
        if self.vida > self.vidamax: self.vida = self.vidamax

    def perderVida(self,valor):
        self.vida -= int(int(valor))

    def condicao(self,criterio,sim,nao,sim2=None,nao2=None,sim3=None,nao3=None,sim4=None,nao4=None,sim5=None,nao5=None):
        if criterio: 
            resolver(jogador,sim)
            if sim2 != None: resolver(jogador,sim2)
            if sim3 != None: resolver(jogador,sim3)
            if sim4 != None: resolver(jogador,sim4)
            if sim5 != None: resolver(jogador,sim5)
        if not criterio: 
            resolver(jogador,nao)
            if nao2 != None: resolver(jogador,nao2)
            if nao3 != None: resolver(jogador,nao3)
            if nao4 != None: resolver(jogador,nao4)
            if nao5 != None: resolver(jogador,nao5)

    def nada(self):
        return None

    def definirAlvo(self,alvo):
        if alvo == "op":
            return self.oponente
        elif alvo == "si":
            return self.oponente

    def causarDano(self,alvo,dano):
        print(alvo)
        alvo = self.definirAlvo(alvo)
        danofinal = dano
        alvo.perderVida(danofinal)


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
        self.oponente = None

    def receberVida(self,valor):
        self.vida += int(valor)
        if self.vida > self.vidamax: self.vida = self.vidamax
    def perderVida(self,valor):
        self.vida -= int(valor)
    def acessarVida(self):
        return self.vida
    def definirVida(self,valor):
        self.vida = int(valor)


    def nada(self):
        return None


kloro = Jogador(0,0,100,None,"Kloro")
lutecio = Inimigo(0,0,100,None,"Lutécio")

jogador = kloro
inimigo = lutecio

jogador.oponente = lutecio
inimigo.oponente = kloro

dano = "causarDano(op,45)"

def resolver(fonte,negocio):
    coisa = re.findall(r'\(.*\)',negocio)[0]
    efeitoreal = negocio.replace(coisa,"")
    coisa = list(coisa)
    coisa[0]=""
    coisa[-1]=""
    coisa = "".join(coisa)
    coisa = coisa.split(",")
    print(coisa)
    i = 0
    for item in coisa:
        coisa[i] = coisa[i].replace("#",",")
        i = i+1
    print(coisa)
    funcao = getattr(fonte, efeitoreal)
    if len(coisa)== 1:
        funcao(coisa[0])
    elif len(coisa) == 2:
        funcao(coisa[0],coisa[1])
    elif len(coisa) == 3:
        funcao(coisa[0],coisa[1],coisa[2])
    elif len(coisa) == 4:
        funcao(coisa[0],coisa[1],coisa[2],coisa[3])
    elif len(coisa) == 5:
        funcao(coisa[0],coisa[1],coisa[2],coisa[3],coisa[4])
    elif len(coisa) == 6:
        funcao(coisa[0],coisa[1],coisa[2],coisa[3],coisa[4],coisa[5])
    elif len(coisa) == 7:
        funcao(coisa[0],coisa[1],coisa[2],coisa[3],coisa[4],coisa[5],coisa[6])
    elif len(coisa) == 8:
        funcao(coisa[0],coisa[1],coisa[2],coisa[3],coisa[4],coisa[5],coisa[6],coisa[7])
    elif len(coisa) == 9:
        funcao(coisa[0],coisa[1],coisa[2],coisa[3],coisa[4],coisa[5],coisa[6],coisa[7],coisa[8])
    elif len(coisa) == 10:
        funcao(coisa[0],coisa[1],coisa[2],coisa[3],coisa[4],coisa[5],coisa[6],coisa[7],coisa[8],coisa[9])
    elif len(coisa) == 11:
        funcao(coisa[0],coisa[1],coisa[2],coisa[3],coisa[4],coisa[5],coisa[6],coisa[7],coisa[8],coisa[9],coisa[10])

    


trick = "condicao(jogador.vida<40,receberVida(23),jogador.nada(),causarDano(op#45))"


print(jogador.vida)
print(inimigo.vida)

resolver(jogador,dano)

print(jogador.vida)
print(inimigo.vida)


resolver(jogador,trick)

print(jogador.vida)
print(inimigo.vida)