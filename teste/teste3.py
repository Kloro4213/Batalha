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


kloro = Jogador(0,0,100,None,"Kloro")

jogador = kloro

jogador.vida -=24

print(jogador.vida)
print(kloro.vida)