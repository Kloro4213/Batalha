from dic_cartas import DCC

class Jogador:
    def __init__(self,y=None,x=None,vida=None, cartas = {},nome=""):
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

    def receberMente(self,valor):
        self.mente += valor
        if self.mente > 10: self.mente = 10
    def perderMente(self,valor):
        self.mente -= valor
        if self.mente < 0: self.mente = 0
    def acessarMente(self):
        return self.mente
    def definirMente(self,valor):
        self.mente = valor

    def receberDesvio(self,valor):
        self.desvio += valor
        if self.desvio > 999: self.desvio = 999
    def perderDesvio(self,valor):
        self.desvio -= valor
        if self.desvio < 0: self.desvio = 0
    def acessarDesvio(self):
        return self.desvio
    def definirDesvio(self,valor):
        self.desvio = valor

    def receberBloqueio(self,valor):
        self.bloqueio += valor
        if self.bloqueio > 999: self.bloqueio = 999
    def perderBloqueio(self,valor):
        self.bloqueio -= valor
        if self.bloqueio < 0: self.bloqueio = 0
    def acessarBloqueio(self):
        return self.bloqueio
    def definirBloqueio(self,valor):
        self.bloqueio = valor

    def receberStatus(self,valor):
        if valor.nome in self.status:
            if valor.acumulavel:
                self.status.update({valor.nome:self.status[valor.nome].valor+valor.valor})
            else:
                self.status.update({valor.nome:valor})    
        else:
            self.status.update({valor.nome:valor})
    def perderStatus(self,valor):
        self.status.pop(valor.nome)
    def acessarStatus(self):
        return self.status



    def coletarCarta(self,carta):
            carta.dono = self
            if carta.id not in self.baralho:
                if carta.tipo == "Ataque":
                    carta = DCC[self.cartasbasicas[0]]
                if carta.tipo == "Manobra":
                    carta = DCC[self.cartasbasicas[1]]
                if carta.tipo == "Talento":
                    carta = DCC[self.cartasbasicas[2]]
            if "Carta 1" not in self.cartas:
                self.cartas.update({"Carta 1":carta})
            elif "Carta 2" not in self.cartas:
                self.cartas.update({"Carta 2":carta})
            elif "Carta 3" not in self.cartas:
                self.cartas.update({"Carta 3":carta})
            elif "Carta 4" not in self.cartas:
                self.cartas.update({"Carta 4":carta})
            elif "Carta 5" not in self.cartas:
                self.cartas.update({"Carta 5":carta})
            elif "Carta 6" not in self.cartas:
                self.cartas.update({"Carta 6":carta})
            elif "Carta 7" not in self.cartas:
                self.cartas.update({"Carta 7":carta})
            elif "Carta 8" not in self.cartas:
                self.cartas.update({"Carta 8":carta})
            elif "Carta 9" not in self.cartas:
                self.cartas.update({"Carta 9":carta})
            elif "Carta 10" not in self.cartas:
                self.cartas.update({"Carta 10":carta})
            
    def organizarCartas(self):
        lcartas = list(self.cartas.values())
        self.cartas = {}
        for carta in lcartas:
            self.coletarCarta(carta)