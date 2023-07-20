import numpy as np
import PySimpleGUI as sg
from colorama import Fore, Back, Style

class Carta:
    def __init__(self,nome=None,efeito=None,dono=None):
        self.nome = nome
        self.efeito = efeito
        self.dono = dono
