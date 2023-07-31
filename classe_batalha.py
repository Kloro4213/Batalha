import numpy as np
import PySimpleGUI as sg
from colorama import Fore, Back, Style
import funcoes_gerais as FG
import classe_jogo as CJ

class Batalha:
    def __init__(self):
        self.jogador = CJ.jogo.jogador
        self.inimigo = CJ.jogo.inimigo
        self.rodadas = 5
        self.primeirarodada = [None,None]
        self.segundarodada = [None,None]
        self.estagio = -1
        self.pilha = {}

    def resolverRodadas(self):
        cartaJogador = self.primeirarodada[0]
        cartaInimigo = self.primeirarodada[0]
        ordem = cartaJogador.tipo+" vs "+cartaInimigo.tipo
        match ordem:
            case "Manobra vs Manobra":
            case "Manobra vs Ataque":
            case "Manobra vs Talento":
            case "Ataque vs Manobra":