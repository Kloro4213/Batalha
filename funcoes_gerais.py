import numpy as np
import PySimpleGUI as sg
from colorama import Fore, Back, Style
import classe_jogo as CJ
import classe_jogador as CJD
import classe_inimigo as CI
import classe_carta as CC
from funcao_imprimir_campo import imprimirCampo
from dic_cartas import DCC


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
    sg.popup("Iniciando batalha")
    CJ.jogo.modo[1] = "Batalha"
    limparmovimento()
    passarvez()

def invocarJogador(campo,y,x,nome):
    if CJ.jogo.temjogador == True:
        sg.popup("Não podem haver dois jogadores!")
        sg.popup(CJ.jogo.jogador.x,CJ.jogo.jogador.y)
    else:
        vida = 100
        cartas = {}
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
        cartas = {}
        if CJ.jogo.inimigo != None:
            x = CJ.jogo.inimigo.x
            y = CJ.jogo.inimigo.y
            vida = CJ.jogo.inimigo.vida
            cartas = CJ.jogo.inimigo.cartas
            nome = CJ.jogo.inimigo.nome
        Lutécio = CJD.Jogador(None,None,vida, cartas,nome)
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

def ReporCampo():
    for j in range(7):
        for k in range(7):
            if CJ.jogo.campo[j][k].carta != None:
                continue
            numero = np.random.randint(3)
            if numero == 0:
                carta = np.random.randint(len(CJ.jogo.jogador.baralho))
                carta = CJ.jogo.jogador.baralho[carta]
                carta = DCC[carta]
            elif numero == 1:
                carta = np.random.randint(len(CJ.jogo.inimigo.baralho))
                carta = CJ.jogo.inimigo.baralho[carta]
                carta = DCC[carta]
            elif numero == 2:
                carta = np.random.randint(len(CJ.jogo.baralhoregional))
                carta = CJ.jogo.baralhoregional[carta]
                carta = DCC[carta]
            CJ.jogo.campo[j][k].carta = carta

def definirBotões():
    if len(CJ.jogo.jogador.cartas)>=1:
        botaoJ1 = sg.Button(CJ.jogo.jogador.cartas[list(CJ.jogo.jogador.cartas.keys())[0]].nome, key="Definir"+list(CJ.jogo.jogador.cartas.keys())[0])
    else:
        botaoJ1 = sg.Text("")
    if len(CJ.jogo.jogador.cartas)>=2:
        botaoJ2 = sg.Button(CJ.jogo.jogador.cartas[list(CJ.jogo.jogador.cartas.keys())[1]].nome, key="Definir"+list(CJ.jogo.jogador.cartas.keys())[1])
    else:
        botaoJ2 = sg.Text("")

    if len(CJ.jogo.jogador.cartas)>=3:
        botaoJ3 = sg.Button(CJ.jogo.jogador.cartas[list(CJ.jogo.jogador.cartas.keys())[2]].nome, key="Definir"+list(CJ.jogo.jogador.cartas.keys())[2])
    else:
        botaoJ3 = sg.Text("")

    if len(CJ.jogo.jogador.cartas)>=4:
        botaoJ4 = sg.Button(CJ.jogo.jogador.cartas[list(CJ.jogo.jogador.cartas.keys())[3]].nome, key="Definir"+list(CJ.jogo.jogador.cartas.keys())[3])
    else:
        botaoJ4 = sg.Text("")

    if len(CJ.jogo.jogador.cartas)>=5:
        botaoJ5 = sg.Button(CJ.jogo.jogador.cartas[list(CJ.jogo.jogador.cartas.keys())[4]].nome, key="Definir"+list(CJ.jogo.jogador.cartas.keys())[4])
    else:
        botaoJ5 = sg.Text("")

    if len(CJ.jogo.jogador.cartas)>=6:
        botaoJ6 = sg.Button(CJ.jogo.jogador.cartas[list(CJ.jogo.jogador.cartas.keys())[5]].nome, key="Definir"+list(CJ.jogo.jogador.cartas.keys())[5])
    else:
        botaoJ6 = sg.Text("")

    if len(CJ.jogo.jogador.cartas)>=7:
        botaoJ7 = sg.Button(CJ.jogo.jogador.cartas[list(CJ.jogo.jogador.cartas.keys())[6]].nome, key="Definir"+list(CJ.jogo.jogador.cartas.keys())[6])
    else:
        botaoJ7 = sg.Text("")

    if len(CJ.jogo.jogador.cartas)>=8:
        botaoJ8 = sg.Button(CJ.jogo.jogador.cartas[list(CJ.jogo.jogador.cartas.keys())[7]].nome, key="Definir"+list(CJ.jogo.jogador.cartas.keys())[7])
    else:
        botaoJ8 = sg.Text("")

    if len(CJ.jogo.jogador.cartas)>=9:
        botaoJ9 = sg.Button(CJ.jogo.jogador.cartas[list(CJ.jogo.jogador.cartas.keys())[8]].nome, key="Definir"+list(CJ.jogo.jogador.cartas.keys())[8])
    else:
        botaoJ9 = sg.Text("")

    if len(CJ.jogo.jogador.cartas)==10:
        botaoJ10 = sg.Button(CJ.jogo.jogador.cartas[list(CJ.jogo.jogador.cartas.keys())[9]].nome, key="Definir"+list(CJ.jogo.jogador.cartas.keys())[9])
    else:
        botaoJ10 = sg.Text("")
    if len(CJ.jogo.jogador.cartas)>=1:
        botaoI1 = sg.Button(CJ.jogo.jogador.cartas[list(CJ.jogo.jogador.cartas.keys())[0]].nome, key="Info"+list(CJ.jogo.jogador.cartas.keys())[0])
    else:
        botaoI1 = sg.Text("")

    if len(CJ.jogo.jogador.cartas)>=2:
        botaoI2 = sg.Button(CJ.jogo.jogador.cartas[list(CJ.jogo.jogador.cartas.keys())[1]].nome, key="Info"+list(CJ.jogo.jogador.cartas.keys())[1])
    else:
        botaoI2 = sg.Text("")

    if len(CJ.jogo.jogador.cartas)>=3:
        botaoI3 = sg.Button(CJ.jogo.jogador.cartas[list(CJ.jogo.jogador.cartas.keys())[2]].nome, key="Info"+list(CJ.jogo.jogador.cartas.keys())[2])
    else:
        botaoI3 = sg.Text("")

    if len(CJ.jogo.jogador.cartas)>=4:
        botaoI4 = sg.Button(CJ.jogo.jogador.cartas[list(CJ.jogo.jogador.cartas.keys())[3]].nome, key="Info"+list(CJ.jogo.jogador.cartas.keys())[3])
    else:
        botaoI4 = sg.Text("")

    if len(CJ.jogo.jogador.cartas)>=5:
        botaoI5 = sg.Button(CJ.jogo.jogador.cartas[list(CJ.jogo.jogador.cartas.keys())[4]].nome, key="Info"+list(CJ.jogo.jogador.cartas.keys())[4])
    else:
        botaoI5 = sg.Text("")

    if len(CJ.jogo.jogador.cartas)>=6:
        botaoI6 = sg.Button(CJ.jogo.jogador.cartas[list(CJ.jogo.jogador.cartas.keys())[5]].nome, key="Info"+list(CJ.jogo.jogador.cartas.keys())[5])
    else:
        botaoI6 = sg.Text("")

    if len(CJ.jogo.jogador.cartas)>=7:
        botaoI7 = sg.Button(CJ.jogo.jogador.cartas[list(CJ.jogo.jogador.cartas.keys())[6]].nome, key="Info"+list(CJ.jogo.jogador.cartas.keys())[6])
    else:
        botaoI7 = sg.Text("")

    if len(CJ.jogo.jogador.cartas)>=8:
        botaoI8 = sg.Button(CJ.jogo.jogador.cartas[list(CJ.jogo.jogador.cartas.keys())[7]].nome, key="Info"+list(CJ.jogo.jogador.cartas.keys())[7])
    else:
        botaoI8 = sg.Text("")

    if len(CJ.jogo.jogador.cartas)>=9:
        botaoI9 = sg.Button(CJ.jogo.jogador.cartas[list(CJ.jogo.jogador.cartas.keys())[8]].nome, key="Info"+list(CJ.jogo.jogador.cartas.keys())[8])
    else:
        botaoI9 = sg.Text("")

    if len(CJ.jogo.jogador.cartas)==10:
        botaoI10 = sg.Button(CJ.jogo.jogador.cartas[list(CJ.jogo.jogador.cartas.keys())[9]].nome, key="Info"+list(CJ.jogo.jogador.cartas.keys())[9])
    else:
        botaoI10 = sg.Text("")
    
    if CJ.jogo.batalha.primeirarodada[0] != None:
        botaoJR = sg.Button(CJ.jogo.batalha.primeirarodada[0].nome, key="Rever Carta J")
    else:
        botaoJR = sg.Text("")

    if CJ.jogo.batalha.primeirarodada[1] != None:
        botaoIR = sg.Button(CJ.jogo.batalha.primeirarodada[1].nome, key="Rever Carta I")
    else:
        botaoIR = sg.Text("")



    return ["",botaoJ1,botaoJ2,botaoJ3,botaoJ4,botaoJ5,botaoJ6,botaoJ7,botaoJ8,botaoJ9,botaoJ10,botaoI1,botaoI2,botaoI3,botaoI4,botaoI5,botaoI6,botaoI7,botaoI8,botaoI9,botaoI10,botaoJR,botaoIR]