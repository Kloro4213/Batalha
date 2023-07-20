import numpy as np
import PySimpleGUI as sg
from colorama import Fore, Back, Style
import classe_casa as CC
import classe_movimento as CM
import classe_carta as CA
import classe_jogo as CJ
import classe_jogador as CJD
import classe_inimigo as CI
from funcao_imprimir_campo import imprimirCampo
from funcao_comando import comando
import funcoes_gerais as FG



letras = ['A','B','C','D','E','F','G']

CJ.jogo.campo = np.empty([7, 7], dtype = CC.Casa)


for j in range(7):
    for k in range(7):
        CJ.jogo.campo[j][k] = CC.Casa(j,k,CA.Carta(letras[j]+str(k+1)))

imprimirCampo(CJ.jogo.campo)
sg.popup(CJ.jogo.modo)


while True:

    if CJ.jogo.modo[0] == "Edição":
        comando("")

    if CJ.jogo.modo[0] == "Sair":
        break
        
    while CJ.jogo.modo[1] == "Movimentação":
        if CJ.jogo.modo[2] == "":
            sg.popup("Veremos quem se move primeiro")
            al = np.random.randint(2)
            if al == 1:
                CJ.jogo.modo[2]="J"
                sg.popup("O Jogador começa!")
            else:
                CJ.jogo.modo[2]="I"
                sg.popup("O Inimigo começa!")
        CJ.jogo.modo[1] = "Movimentação"
        if CJ.jogo.modo[2] == "J":
            if CJ.jogo.movimentoJ == None: CJ.jogo.movimentoJ = CM.Movimento(CJ.jogo.jogador)
            if CJ.jogo.movimentoI == None: CJ.jogo.movimentoI = CM.Movimento(CJ.jogo.inimigo)
            if CJ.jogo.movimentoJ.movimentorestante <= 0:
                if CJ.jogo.movimentoI.movimentorestante <= 0:
                    FG.batalha()
                    imprimirCampo(CJ.jogo.campo)
                else: FG.passarvez()
            else:
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
                    imprimirCampo(CJ.jogo.campo)
                else: 
                    CJ.jogo.movimentoJ.direcionar(event)
                    imprimirCampo(CJ.jogo.campo)
        elif CJ.jogo.modo[2] == "I":
            if CJ.jogo.movimentoI == None: CJ.jogo.movimentoI = CM.Movimento(CJ.jogo.inimigo)
            if CJ.jogo.movimentoJ == None: CJ.jogo.movimentoJ = CM.Movimento(CJ.jogo.jogador)
            if CJ.jogo.movimentoJ.movimentorestante != None and CJ.jogo.movimentoI.movimentorestante != None: 
                if CJ.jogo.movimentoI.movimentorestante <= 0:
                    if CJ.jogo.movimentoJ.movimentorestante <= 0:
                        FG.batalha()
                        imprimirCampo(CJ.jogo.campo)
                    else: FG.passarvez()
                else:
                    CJ.jogo.movimentoI.direcionar("?")
        imprimirCampo(CJ.jogo.campo)
    imprimirCampo(CJ.jogo.campo)
