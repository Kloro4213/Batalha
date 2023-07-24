
class Jogador:
    def __init__(self,y=None,x=None,vida=None, cartas = {},nome=""):
        self.vida=vida
        self.cartas=cartas
        self.y=y
        self.x=x
        self.nome=nome
        self.mente = None
        
    
    def coletarCarta(self,carta):
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
    