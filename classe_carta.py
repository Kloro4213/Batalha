import numpy as np
import PySimpleGUI as sg
import classe_efeito as CE
from colorama import Fore, Back, Style


class Carta:
    def __init__(self,id,nome,tipo,efeito=None,desc=None):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.desc = desc
        self.efeito = efeito
        self.dono = None







    def resolver(self):
        for efeito in self.efeito:
            efeito()
        
    def causarDano(alvo,dano):
        if alvo.desvio > dano:
            




        alvo.vida -= dano

    def bloquear(self,quantidade):
        self.dono.bloqueio += quantidade
        
    def desviar(self,quantidade):
        self.dono.desvio += quantidade
        
    def causarStatus(alvo,status):
        alvo.status.update({status.nome:status})

    def ganharStatus(self,status):
        self.status.update({status.nome:status})




#cartabranca = Carta()

	
					

					
					
					

					