class Inimigo:
    def __init__(self,y=None,x=None,vida=None,cartas = {},nome=""):
        self.vida=vida
        self.cartas=cartas
        self.y=y
        self.x=x
        self.nome=nome
        self.mente = None
