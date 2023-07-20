import classe_movimento as CM
import numpy as np
import classe_casa as CC

class Jogo:
    def __init__(self):
        self.temjogador = False
        self.teminimigo = False
        self.jogador = None
        self.inimigo = None
        self.movimentoJ = CM.Movimento(None)
        self.movimentoI = CM.Movimento(None)
        self.campo = None
        self.modo = "Edição"


jogo = Jogo()

jogo.campo = np.empty([7, 7], dtype = CC.Casa)

