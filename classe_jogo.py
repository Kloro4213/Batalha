import numpy as np

class Jogo:
    def __init__(self):
        self.temjogador = False
        self.teminimigo = False
        self.jogador = None
        self.inimigo = None
        self.movimentoJ = None
        self.movimentoI = None
        self.batalha = None
        self.campo = None
        self.modo = ["Edição",'','','','','','']
        self.baralhoregional = []
    
    def definirbaralhos(self):
        self.jogador.cartasbasicas = [1,2,3]
        self.inimigo.cartasbasicas = [21,22,23]
        self.jogador.baralho = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        self.inimigo.baralho = [24,25,26,27,28,29,30,31]
        self.baralhoregional = [31,32,33,34,35,36]


jogo = Jogo()


