import numpy as np
import PySimpleGUI as sg
import classe_status as CE
from colorama import Fore, Back, Style
import math

class Carta:
    def __init__(self,id,nome,tipo,efeito={},desc=None):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.desc = desc
        self.efeito = efeito
        self.dono = None
        self.log = {}


    def resolver(self):
        for efeito in self.efeito:
            efeito()
        
    def causarDano(self,alvo,dano):
        danofinal = dano
        if "Fraqueza" in self.dono.acessarStatus():
            danofinal = math.floor(danofinal*0.75)
        if "Fragilidade" in alvo.acessarStatus():
            danofinal = math.floor(danofinal*1.25)
        if alvo.acessarBloqueio() > 0:
            temp = danofinal
            danofinal -= alvo.acessarBloqueio()
            if danofinal < 0: danofinal = 0
            alvo.perderBloqueio(danofinal)
        if alvo.acessarDesvio() >= danofinal:
            alvo.definirDesvio = math.floor(alvo.acessarDesvio()/2)
            danofinal = 0
        alvo.perderVida(danofinal)

    def bloquear(self,quantidade):
        self.dono.bloqueio += quantidade
        
    def desviar(self,quantidade):
        self.dono.desvio += quantidade
        
    def causarStatus(alvo,status):
        alvo.receberStatus(status)

    def ganharStatus(self,status):
        self.dono.receberStatus(status)



#cartabranca = Carta()

	
					

					
					
					

					