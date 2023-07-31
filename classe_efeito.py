class Efeito:
    def __init__(self,nome,efeitos):
        self.nome = nome
        for efeito in efeitos:
            self.efeitos.append(efeito)

    