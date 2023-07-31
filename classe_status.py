class Status:
    def __init__(self,nome,efeitos,acumulavel=True):
        self.nome = nome
        self.duracao = None
        self.valor1 = None
        self.valor2 = None
        for efeito in efeitos:
            self.efeitos.append(efeito)
        self.acumulavel = acumulavel

    