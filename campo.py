import numpy as np
import PySimpleGUI as sg
from colorama import Fore, Back, Style
import classe_casa as CC
import classe_movimento as CM
import classe_carta as CA
from funcao_imprimir_campo import imprimirCampo
from funcao_comando import comando
import funcoes_gerais as FG


class CJogo:
    def __init__(self):
        self.temjogador = False
        self.teminimigo = False
        self.jogador = None
        self.inimigo = None
        self.movimentoJ = CM.Movimento(None)
        self.movimentoI = CM.Movimento(None)

class CJogador:
    def __init__(self,y=None,x=None,vida=None,cartas=None,nome="Kloro"):
        self.vida=vida
        self.cartas=cartas
        self.y=y
        self.x=x
        self.nome=nome
    
class CInimigo:
    def __init__(self,y=None,x=None,vida=None,cartas=None,nome="Inimigo"):
        self.vida=vida
        self.cartas=cartas
        self.y=y
        self.x=x
        self.nome=nome

jogo = CJogo()
letras = ['A','B','C','D','E','F','G']

CAMPO = np.empty([7, 7], dtype = CC.Casa)


for j in range(7):
    for k in range(7):
        CAMPO[j][k] = CC.Casa(j,k,CA.Carta(letras[j]+str(k+1)))

modo = ["Edição","Nada","","","",""]

imprimirCampo(CAMPO)
while modo[0] == "Edição":
    comando("")
    imprimirCampo(CAMPO)

while modo[0] == "Sair":
    break

while modo[0] == "Jogo":
    if modo[2] == "":
        sg.popup("O Jogo realmente começou")
        sg.popup("Veremos quem se move primeiro")
        al = np.random.randint(2)
        if al == 1:
            modo[2]="J"
            sg.popup("O Jogador começa!")
        else:
            modo[2]="I"
            sg.popup("O Inimigo começa!")
    modo[1] = "Movimentação"
    
    if modo[1] == "Movimentação":
        if modo[2] == "J":
            if jogo.movimentoJ.dono == None:
                jogo.movimentoJ = CM.Movimento(jogo.jogador)
                sg.popup("o movimento do jogador começou")
            if jogo.movimentoJ.movimentorestante <= 0:
                if jogo.movimentoJ.movimentorestante != None and jogo.movimentoI.movimentorestante != None:  
                    if jogo.movimentoJ.movimentorestante <= 0:
                        if jogo.movimentoI.movimentorestante <= 0:
                            FG.batalha()
                        else: FG.passarvez()
            layout =[
                    [sg.T(' '  * 10), sg.Button("W")],
                    [sg.Button("A"), sg.T(' ' * 15), sg.Button("D")],
                    [sg.T(' '  * 10), sg.Button("S")],
                    [sg.T(" " * 10)],
                    [sg.Text("Deseja fazer algo antes de se mover?"),sg.InputText(""),sg.Button("OK")]
                    ]
            window = sg.Window("Movimentação",layout)
            event, values = window.read()
            window.close()
            if event == "OK":
                comando(event[0])
                imprimirCampo(CAMPO)
            else: 
                jogo.movimentoJ.direcionar(event)
                imprimirCampo(CAMPO)
        elif modo[2] == "I":
            if jogo.movimentoI.dono == None:
                jogo.movimentoI = CM.Movimento(jogo.inimigo)
                sg.popup("o movimento do inimigo começou")
            if jogo.movimentoJ.movimentorestante != None and jogo.movimentoI.movimentorestante != None:  
                if jogo.movimentoJ.movimentorestante <= 0:
                    if jogo.movimentoI.movimentorestante <= 0:
                        FG.batalha()
                    else: FG.passarvez()
            jogo.movimentoI.direcionar("?")
        imprimirCampo(CAMPO)
            
