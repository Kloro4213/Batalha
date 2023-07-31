class Efeito:
    def __init__(self,nome,efeitos,acumulavel=True):
        self.nome = nome
        for efeito in efeitos:
            self.efeitos.append(efeito)
        self.acumulavel = acumulavel

    