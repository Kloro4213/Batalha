import numpy as np
import PySimpleGUI as sg
import classe_efeito as CE
from colorama import Fore, Back, Style
import math

class Carta:
    def __init__(self,id,nome,tipo,efeito=None,desc=None):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.desc = desc
        self.efeito = efeito
        self.dono = None
        self.log = {
        }






    def resolver(self):
        for efeito in self.efeito:
            efeito()
        
    def causarDano(alvo,dano):
        danofinal = dano
        if alvo.bloqueio > 0:
            temp = danofinal
            danofinal -= alvo.bloqueio
            alvo.bloqueio -= temp
            if alvo.bloqueio < 0: alvo.bloqueio = 0
            if danofinal < 0: danofinal = 0
        if alvo.desvio >= danofinal:
            alvo.desvio = math.floor(alvo.desvio/2)
            danofinal = 0
        alvo.vida -= danofinal

    def bloquear(self,quantidade):
        self.dono.bloqueio += quantidade
        
    def desviar(self,quantidade):
        self.dono.desvio += quantidade
        
    def causarStatus(alvo,status):
        alvo.status.update({status.nome:status})

    def ganharStatus(self,status):
        self.status.update({status.nome:status})




#cartabranca = Carta()

	
					

					
					
					

					