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
