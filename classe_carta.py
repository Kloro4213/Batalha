import numpy as np
import PySimpleGUI as sg
import classe_status as CE
from colorama import Fore, Back, Style
import math
import classe_jogo as CJ

class Carta:
    def __init__(self,id,nome,tipo,rotulo=None,desc=None,efeito=None):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.desc = desc
        self.dono = None
        self.log = {}
        self.efeito = efeito
        self.rotulo = rotulo

    def condicao(self,criterio,sim,nao):
        if criterio: eval(sim)
        if not criterio: eval(nao)

    def definirAlvo(self,alvo):
        if alvo == "si":
            alvo = self.dono
        elif alvo == "op":
            if self.dono == CJ.jogo.inimigo:
                alvo = CJ.jogo.jogador
            else:
                alvo = CJ.jogo.inimigo
        return alvo

    def encontrarOutro(self):
        if self.dono == CJ.jogo.jogador:
            return CJ.jogo.batalha.cartaInimigo
        elif self.dono == CJ.jogo.inimigo:
            return CJ.jogo.batalha.cartaJogador

    def encontrarEu(self):
        if self.dono == CJ.jogo.jogador:
            return CJ.jogo.batalha.cartaJogador
        elif self.dono == CJ.jogo.inimigo:
            return CJ.jogo.batalha.cartaInimigo
        
    def clash(self):
        return self.encontrarEu.tipo == self.encontrarOutro.tipo
            

    def causarDano(self,alvo,dano):
        alvo = self.definirAlvo(alvo)
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
        
    def causarStatus(self,alvo,status):
        alvo = self.definirAlvo(alvo)
        alvo.receberStatus(status)

    def ganharStatus(self,status):
        self.dono.receberStatus(status)

    def causarDanoMental(self,alvo,dano):
        alvo = self.definirAlvo(alvo)
        alvo.perderMente(dano)

    def suspender(self,carta):
        if carta in CJ.jogo.batalha.primeirarodada:
            temp = carta
            CJ.jogo.batalha.primeirarodada[CJ.jogo.batalha.primeirarodada.index(carta)] = None
            CJ.jogo.batalha.pilhasuspensa.append(temp)
        elif carta in CJ.jogo.batalha.segundarodada:
            temp = carta
            CJ.jogo.batalha.segundarodada[CJ.jogo.batalha.segundarodada.index(carta)] = None
            CJ.jogo.batalha.pilhasuspensa.append(temp)

    def pioneiro(self):
        return self.encontrarEu() in CJ.jogo.batalha.primeirarodada

    def nada(self):
        return None
#cartabranca = Carta()