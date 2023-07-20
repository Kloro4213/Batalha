import numpy as np
import PySimpleGUI as sg
from colorama import Fore, Back, Style

class Casa:
    def __init__(self,y,x,carta=None,ocupante=None,visitado=None):
        self.y = y
        self.x = x
        self.carta = carta
        self.ocupante=ocupante
        self.visitado=visitado

    def definirOcupante(self,ocupante):
        self.ocupante = ocupante
    
    def definirCarta(self,carta):
        self.carta = carta

    def obterVizinhos(self):
        vizinhos = []
        if self.y > 0:
            vizinho = CAMPO[self.y-1][self.x]
            vizinhos.append(vizinho)
            #print(vizinho.carta.nome+" é adjacente a mim, "+self.carta.nome)

        if self.y < 6:
            vizinho = CAMPO[self.y+1][self.x]
            vizinhos.append(vizinho)
            #print(vizinho.carta.nome+" é adjacente a mim, "+self.carta.nome)
        if self.x > 0:
            vizinho = CAMPO[self.y][self.x-1]
            vizinhos.append(vizinho)
            #print(vizinho.carta.nome+" é adjacente a mim, "+self.carta.nome)
        if self.x < 6:
            vizinho = CAMPO[self.y][self.x+1]
            vizinhos.append(vizinho)
            #print(vizinho.carta.nome+" é adjacente a mim, "+self.carta.nome)
        return vizinhos
    