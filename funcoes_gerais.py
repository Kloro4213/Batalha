import numpy as np
import PySimpleGUI as sg
from colorama import Fore, Back, Style

def batalha():
    sg.popup("A Batalha não existe ainda :)")
    CJ.modo[0] = "Edição"
    CJ.modo[1] = ""
    CJ.modo[2] = ""

def invocarJogador(campo,y,x):
    if jogo.temjogador == True:
        sg.popup("Não podem haver dois jogadores!")
        print(jogo.jogador.x,jogo.jogador.y)
    else:
        Kloro = CJogador(None,None,100)
        campo[y][x].ocupante = Kloro
        Kloro.y = y
        Kloro.x = x
        jogo.temjogador = True
        jogo.jogador = Kloro

def invocarInimigo(campo,y,x):
    if jogo.teminimigo == True:
        sg.popup("Não podem haver dois inimigos!")
    else:
        inimigo = CInimigo(None,None,100)
        campo[y][x].ocupante = inimigo
        inimigo.y = y
        inimigo.x = x
        jogo.teminimigo = True
        jogo.inimigo = inimigo

def passarvez():
    if CJ.modo[2] == "I":
        CJ.modo[2] = "J"
    else:
        CJ.modo[2] = "I"

def obtercasa(y,x):
    if type(y) == str:
        return CAMPO[N(y)][(int(x))-1]
    elif type(y) == int:
        return CAMPO[y][x]

def N(letra):
    match letra:
        case "A":
            return 0
        case "B":
            return 1
        case "C":
            return 2
        case "D":
            return 3
        case "E":
            return 4
        case "F":
            return 5
        case "G":
            return 6

def buscaritem(item):
    return item
