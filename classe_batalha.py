import numpy as np
import PySimpleGUI as sg
from colorama import Fore, Back, Style
import funcoes_gerais as FG
import classe_jogo as CJ
import re

class Batalha:
    def __init__(self):
        self.jogador = CJ.jogo.jogador
        self.inimigo = CJ.jogo.inimigo
        self.rodadas = 5
        self.primeirarodada = [None,None]
        self.segundarodada = [None,None]
        self.estagio = -1
        self.pilhasuspensa = []
        self.cartaJogador = None
        self.cartaInimigo = None
        self.proxcartaJogador = None
        self.proxcartaInimigo = None


    def passarRodada(self):
        self.rodadas -= 1
        for carta in self.pilhasuspensa:
            self.resolver(carta)
        if self.rodadas == 0:
            FG.terminarBatalha()
        FG.passarvez

    def acontecer(coisa,negocio):
        valor = re.findall(r'\(\d*\)',negocio)[0]
        efeitoreal = negocio.replace(valor,"")
        valor = valor.replace("(","").replace(")","")
        valor = int(valor)
        funcao = getattr(coisa, efeitoreal)
        funcao(valor)

    def resolver(self,carta):
        for efeito in carta.efeito:
            self.acontecer(carta,efeito)

    def resolverRodadas(self):
        self.cartaJogador = self.primeirarodada[0]
        self.cartaInimigo = self.primeirarodada[1]
        etapas = ["Manobra","Ataque","Talento"]
        primeiro = CJ.jogo.modo[2]
        if primeiro == "J": segundo = "I"
        else: segundo = "J"
        contador = 0
        while CJ.jogo.modo[1] == "Batalha" >0:
            if self.cartaJogador.tipo == self.cartaInimigo.tipo:
                if primeiro == "J":
                    self.resolver(self.cartaJogador)
                    if self.cartaJogador == self.primeirarodada[0]:
                        self.cartaJogador == self.segundarodada[0]
                    else:
                        self.cartaJogador = None
                    self.resolver(self.cartaInimigo)
                    if self.cartaInimigo == self.primeirarodada[1]:
                        self.cartaInimigo == self.segundarodada[1]
                    else:
                        self.cartaInimigo = None
                else:
                    self.resolver(self.cartaInimigo)
                    if self.cartaInimigo == self.primeirarodada[1]:
                        self.cartaInimigo == self.segundarodada[1]
                    else:
                        self.cartaInimigo = None
                    self.resolver(self.cartaJogador)
                    if self.cartaJogador == self.primeirarodada[0]:
                        self.cartaJogador == self.segundarodada[0]
                    else:
                        self.cartaJogador = None
            elif self.cartaJogador.tipo == etapas[contador]:
                self.resolver(self.cartaJogador)
                if self.cartaJogador == self.primeirarodada[0]:
                    self.cartaJogador == self.segundarodada[0]
                else:
                    self.cartaJogador = None
            elif self.cartaInimigo.tipo == etapas[contador]:
                self.resolver(self.cartaInimigo)
                if self.cartaInimigo == self.primeirarodada[1]:
                    self.cartaInimigo == self.segundarodada[1]
                else:
                    self.cartaInimigo = None
            elif self.cartaInimigo == None and self.cartaJogador == None:
                contador +=1
                if contador == 4: self.passarRodada()
            elif self.cartaInimigo != etapas[contador] and self.cartaJogador != etapas[contador]:
                contador +=1
                if contador == 4: self.passarRodada()
                
                    
            




