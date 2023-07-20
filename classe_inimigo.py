class Inimigo:
    def __init__(self,y=None,x=None,vida=None,cartas=None,nome="Inimigo"):
        self.vida=vida
        self.cartas=cartas
        self.y=y
        self.x=x
        self.nome=nome