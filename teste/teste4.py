import re
from sympy import sympify

def SEPARAR(texto):
    pilha=[""]
    saída = []
    texto = list(texto)
    i = 0
    while i<len(texto):
        if pilha[len(pilha)-1] != "(" and pilha[len(pilha)-1] != "[":
            if texto[i] != "(" and texto[i] != "[":
                i = i+1
            elif texto[i] == "(":
                saída.append("")
                pilha.append("(")
                saída[len(saída)-1] = saída[len(saída)-1]+texto[i]
                i = i+1
            elif texto[i] == "[":
                saída.append("")
                pilha.append("[")
                saída[len(saída)-1] = saída[len(saída)-1]+texto[i]
                i = i+1
        else:
            if texto[i] != ")" and texto[i] != "]":
                saída[len(saída)-1] = saída[len(saída)-1]+texto[i]
                i = i+1
            elif texto[i] == ")" and pilha[len(pilha)-1] == "(":
                saída[len(saída)-1] = saída[len(saída)-1]+texto[i]
                i = i+1
                del pilha[len(pilha)-1]
            elif texto[i] == "]" and pilha[len(pilha)-1] == "[":
                saída[len(saída)-1] = saída[len(saída)-1]+texto[i]
                i = i+1
                del pilha[len(pilha)-1]
            else:
                saída[len(saída)-1] = saída[len(saída)-1]+texto[i]
                i = i+1
    return saída

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
    
    def encontrarEu(self):
        return self

    def receberVida(self,valor):
        self.vida += int(int(valor))
        if self.vida > self.vidamax: self.vida = self.vidamax

    def perderVida(self,valor):
        self.vida -= int(int(valor))

    def condicao(self,criterio,sim,nao):
        print("O critério é:",criterio)
        print("O critério é:",sim)
        print("O critério é:",nao)
        if sympify(criterio):
            sim = sim.replace("[","").replace("]","")
            sim = sim.split("+")
            for comando in sim:
                resolver(self,comando)
        else:
            nao = nao.replace("[","").replace("]","")
            nao = nao.split("+")
            for comando in nao:
                resolver(self,comando)
    def nada(self):
        return None

    def definirAlvo(self,alvo):
        if alvo == "op":
            return self.oponente
        elif alvo == "si":
            return self.oponente

    def causarDano(self,alvo,dano):
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
    temp = re.findall(r'[(].*[)]',negocio)[0]
    efeitoreal = negocio.replace(temp,"")
    temp = list(temp)
    temp[0]=""
    temp[-1]=""
    temp = "".join(temp)
    coisa = SEPARAR(temp)
    dicreal = {}
    for item in coisa:
        dicreal.update({"blob"+str(coisa.index(item)):item})
        temp = temp.replace(item,"blob"+str(coisa.index(item)))
    temp = temp.split(",")
    i=0
    while i <len(temp):
        correspondencia = re.findall(r'blob\d',temp[i])
        for j in range(len(correspondencia)):        
            temp[i] = temp[i].replace(correspondencia[j],dicreal[correspondencia[j]])
        i = i+1
    funcao = getattr(fonte, efeitoreal)
    if len(temp)== 1:
        funcao(temp[0])
    elif len(temp) == 2:
        funcao(temp[0],temp[1])
    elif len(temp) == 3:
        funcao(temp[0],temp[1],temp[2])
    elif len(temp) == 4:
        funcao(temp[0],temp[1],temp[2],temp[3])
    elif len(temp) == 5:
        funcao(temp[0],temp[1],temp[2],temp[3],temp[4])
    elif len(temp) == 6:
        funcao(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5])
    elif len(temp) == 7:
        funcao(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6])
    elif len(temp) == 8:
        funcao(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7])
    elif len(temp) == 9:
        funcao(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7],temp[8])
    elif len(temp) == 10:
        funcao(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7],temp[8],temp[9])
    elif len(temp) == 11:
        funcao(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7],temp[8],temp[9],temp[10])

    


magic = "condicao(self.vida<40,perderVida(99),[receberVida(23)+causarDano(op,45)])"


print("A vida do jogador é:",jogador.vida)
print("A vida do inimigo é:",inimigo.vida)

print("Iremos causar 45 de dano ao inimigo!")

resolver(jogador,dano)

print("A vida do jogador é:",jogador.vida)
print("A vida do inimigo é:",inimigo.vida)

print("Se a vida do jogador foir menor que 40, ele perderá 99 de vida. Do contrário, receberá 23 e causará 45 de dano ao oponente")
resolver(jogador,magic)

print("A vida do jogador é:",jogador.vida)
print("A vida do inimigo é:",inimigo.vida)

print("Se a vida do jogador foir menor que 40, ele perderá 99 de vida. Do contrário, receberá 23 e causará 45 de dano ao oponente")
resolver(jogador,magic)

print("A vida do jogador é:",jogador.vida)
print("A vida do inimigo é:",inimigo.vida)