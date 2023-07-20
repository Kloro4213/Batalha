import numpy as np
import PySimpleGUI as sg
from colorama import Fore, Back, Style
import classe_jogo as CJ
import classe_jogador as CJD
import classe_inimigo as CI
from funcao_imprimir_campo import imprimirCampo

def limparmovimento():
    for fileira in CJ.jogo.campo:
        for casa in fileira:    
            casa.visitado = None
            casa.ocupante = None
    CJ.jogo.movimentoI = None
    CJ.jogo.movimentoJ = None
    CJ.jogo.teminimigo = False
    CJ.jogo.temjogador = False

def batalha():
    sg.popup("A Batalha não existe ainda :)")
    CJ.jogo.modo[0] = "Edição"
    CJ.jogo.modo[1] = ""
    CJ.jogo.modo[2] = ""
    limparmovimento()

def invocarJogador(campo,y,x,nome):
    if CJ.jogo.temjogador == True:
        sg.popup("Não podem haver dois jogadores!")
        sg.popup(CJ.jogo.jogador.x,CJ.jogo.jogador.y)
    else:
        vida = 100
        cartas = None
        if CJ.jogo.jogador != None:
            x = CJ.jogo.jogador.x
            y = CJ.jogo.jogador.y
            vida = CJ.jogo.jogador.vida
            cartas = CJ.jogo.jogador.cartas
            nome = CJ.jogo.jogador.nome
        Kloro = CJD.Jogador(None,None,vida,cartas,nome)
        campo[y][x].ocupante = Kloro
        Kloro.y = y
        Kloro.x = x
        CJ.jogo.temjogador = True
        CJ.jogo.jogador = Kloro

def invocarInimigo(campo,y,x,nome):
    if CJ.jogo.teminimigo == True:
        sg.popup("Não podem haver dois inimigos!")
        sg.popup(CJ.jogo.inimigo.x,CJ.jogo.inimigo.y)
    else:
        vida = 100
        cartas = None
        if CJ.jogo.inimigo != None:
            x = CJ.jogo.inimigo.x
            y = CJ.jogo.inimigo.y
            vida = CJ.jogo.inimigo.vida
            cartas = CJ.jogo.inimigo.cartas
            nome = CJ.jogo.inimigo.nome
        Lutécio = CJD.Jogador(None,None,vida,cartas,nome)
        campo[y][x].ocupante = Lutécio
        Lutécio.y = y
        Lutécio.x = x
        CJ.jogo.teminimigo = True
        CJ.jogo.inimigo = Lutécio

def passarvez():
    if CJ.jogo.modo[2] == "I":
        CJ.jogo.modo[2] = "J"
    else:
        CJ.jogo.modo[2] = "I"

def obtercasa(y,x):
    if type(y) == str:
        return CJ.jogo.campo[N(y)][(int(x))-1]
    elif type(y) == int:
        return CJ.jogo.campo[y][x]

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
