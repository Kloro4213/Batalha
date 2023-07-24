import numpy as np
import PySimpleGUI as sg
from colorama import Fore, Back, Style
import classe_casa as CC
import classe_movimento as CM
import classe_carta as CA
import classe_jogo as CJ
import classe_jogador as CJD
import classe_inimigo as CI
import classe_batalha as CB
from funcao_imprimir_campo import imprimirCampo
from funcao_comando import comando
from dic_cartas import DCC
import funcoes_gerais as FG



letras = ['A','B','C','D','E','F','G']
numeros = [0,1,2,3,4,5,6,7,8,9]
snumeros = ['0','1','2','3','4','5','6','7','8','9']
lcartas = ["Bola de Fogo","Soco potente","Cuspe Ácido","3 Oitão"]


CJ.jogo.campo = np.empty([7, 7], dtype = CC.Casa)


for j in range(7):
    for k in range(7):
        CJ.jogo.campo[j][k] = CC.Casa(j,k,DCC[lcartas[np.random.randint(4)]],None,None)

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
                    comando(values[0])
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
    
    while CJ.jogo.modo[1] == "Batalha":
        if CJ.jogo.batalha == None:
            CJ.jogo.batalha = CB.Batalha()
            sg.popup("A BATALHA COMEÇOU")

        if CJ.jogo.batalha.estagio == -1:
            if CJ.jogo.batalha.primeirarodada[0] != None and CJ.jogo.batalha.primeirarodada[1] != None:
                CJ.jogo.batalha.estagio = 1

        if CJ.jogo.modo[2] == "I":
            numero = np.random.randint(len(CJ.jogo.inimigo.cartas))+1
            carta = CJ.jogo.inimigo.cartas["Carta "+str(numero)]
            if CJ.jogo.batalha.estagio == -1:
                CJ.jogo.batalha.primeirarodada[1] = carta
                CJ.jogo.inimigo.cartas.pop("Carta "+str(numero))
            elif CJ.jogo.batalha.estagio == 1:
                CJ.jogo.batalha.segundarodada[1] = carta
                CJ.jogo.inimigo.cartas.pop("Carta "+str(numero))
            FG.passarvez()
            continue

        if CJ.jogo.modo[2] == "J":

            if CJ.jogo.batalha.estagio == -1:
                jogador = [
                    [sg.Text('Nome:'), sg.T(' '  * 3), sg.Text(CJ.jogo.jogador.nome)],
                    [sg.Text('Vida'), sg.T(' '  * 3), sg.Text(CJ.jogo.jogador.vida)],
                    [sg.Text('Mente'), sg.T(' '  * 3), sg.Text(CJ.jogo.jogador.mente)],
                    [sg.T(' '  * 3)],
                    [sg.Text("",size=(30, 2),background_color="white",text_color="black",key="-nome-" )],
                    [sg.Text("Selecione uma carta abaixo",size=(30, 10),background_color="white",text_color="black",key="-desc-" )],
                    [sg.Checkbox('Ocultar?'), sg.Checkbox('Preservar?'), sg.Button("OK")],
                    [sg.Button(CJ.jogo.jogador.cartas["Carta 1"].nome, key="DefinirCarta1"+CJ.jogo.jogador.cartas["Carta 1"].nome),sg.Button(CJ.jogo.jogador.cartas["Carta 2"].nome, key="DefinirCarta2"+CJ.jogo.jogador.cartas["Carta 2"].nome)],
                    [sg.Button(CJ.jogo.jogador.cartas["Carta 3"].nome, key="DefinirCarta3"+CJ.jogo.jogador.cartas["Carta 3"].nome),sg.Button(CJ.jogo.jogador.cartas["Carta 4"].nome, key="DefinirCarta4"+CJ.jogo.jogador.cartas["Carta 4"].nome)]
                    ]

                inimigo = [
                    [sg.Text('Nome:'), sg.T(' '  * 3), sg.Text(CJ.jogo.inimigo.nome)],
                    [sg.Text('Vida'), sg.T(' '  * 3), sg.Text(CJ.jogo.inimigo.vida)],
                    [sg.Text('Mente'), sg.T(' '  * 3), sg.Text(CJ.jogo.inimigo.mente)],
                    [sg.T(' '  * 3)],
                    [sg.Text("",size=(30, 2),background_color="white",text_color="black",key="-nome-" )],
                    [sg.Text("",size=(30, 10),background_color="white",text_color="black",key="-desc-" )],
                    [sg.Button(CJ.jogo.inimigo.cartas["Carta 1"].nome, key="Info1"+CJ.jogo.inimigo.cartas["Carta 1"].nome),sg.Button(CJ.jogo.inimigo.cartas["Carta 2"].nome, key="Info2"+CJ.jogo.inimigo.cartas["Carta 2"].nome)],
                    [sg.Button(CJ.jogo.inimigo.cartas["Carta 3"].nome, key="Info3"+CJ.jogo.inimigo.cartas["Carta 3"].nome),sg.Button(CJ.jogo.inimigo.cartas["Carta 4"].nome, key="Info4"+CJ.jogo.inimigo.cartas["Carta 4"].nome)]
                        ]

                layout = [[sg.Column(jogador),sg.Text("Turno Atual:"+str(6-int(CJ.jogo.batalha.rodadas))),sg.Column(inimigo)]]


                window = sg.Window('BATALHA', layout)

                
                while True:
                        event, value = window.read()
                        if list(event)[0] == "D":
                            carta = event.replace("DefinirCarta","")
                            carta = list(carta)
                            if carta[0] in snumeros:
                                ordem = carta[0]
                                del carta[0]
                            carta = "".join(carta) 
                            window["-nome-"].update(DCC[carta].nome)
                            window["-desc-"].update(DCC[carta].desc)  
                        elif list(event)[0] == "I":
                            carta = event.replace("Info","")
                            carta = list(carta)
                            if carta[0] in snumeros:
                                del carta[0]
                            carta = "".join(carta)
                            layout2 = [[sg.Text(DCC[carta].nome)],
                                    [sg.Text(DCC[carta].desc)],
                                    [sg.Button("OK")]
                                    ]
                            janelinha = sg.Window("Carta",layout2) 
                            event, value = janelinha.read()
                            janelinha.close()
                        else:
                            CJ.jogo.batalha.primeirarodada[0]=carta
                            CJ.jogo.jogador.cartas.pop("Carta "+ordem)
                            FG.passarvez()
                            window.close()
                            break
                continue
            elif CJ.jogo.batalha.estagio == 1:
                jogador = [
                    [sg.Text('Nome:'), sg.T(' '  * 3), sg.Text(CJ.jogo.jogador.nome)],
                    [sg.Text('Vida'), sg.T(' '  * 3), sg.Text(CJ.jogo.jogador.vida)],
                    [sg.Text('Mente'), sg.T(' '  * 3), sg.Text(CJ.jogo.jogador.mente)],
                    [sg.T(' '  * 3)],
                    [sg.Button(CJ.jogo.batalha.primeirarodada[0], key="InfoCarta5"+CJ.jogo.batalha.primeirarodada[0])],
                    [sg.Text("",size=(30, 2),background_color="white",text_color="black",key="-nome-" )],
                    [sg.Text("Selecione uma carta abaixo",size=(30, 10),background_color="white",text_color="black",key="-desc-" )],
                    [sg.Checkbox('Ocultar?'), sg.Checkbox('Preservar?'), sg.Button("OK")],
                    [sg.Button(CJ.jogo.jogador.cartas["Carta 1"].nome, key="DefinirCarta1"+CJ.jogo.jogador.cartas["Carta 1"].nome),sg.Button(CJ.jogo.jogador.cartas["Carta 2"].nome, key="DefinirCarta2"+CJ.jogo.jogador.cartas["Carta 2"].nome)],
                    [sg.Button(CJ.jogo.jogador.cartas["Carta 3"].nome, key="DefinirCarta3"+CJ.jogo.jogador.cartas["Carta 3"].nome),sg.Button(CJ.jogo.jogador.cartas["Carta 4"].nome, key="DefinirCarta4"+CJ.jogo.jogador.cartas["Carta 4"].nome)]
                    ]

                inimigo = [
                    [sg.Text('Nome:'), sg.T(' '  * 3), sg.Text(CJ.jogo.inimigo.nome)],
                    [sg.Text('Vida'), sg.T(' '  * 3), sg.Text(CJ.jogo.inimigo.vida)],
                    [sg.Text('Mente'), sg.T(' '  * 3), sg.Text(CJ.jogo.inimigo.mente)],
                    [sg.T(' '  * 3)],
                    [sg.Button(CJ.jogo.batalha.primeirarodada[1], key="InfoCarta6"+CJ.jogo.batalha.primeirarodada[1])],
                    [sg.Text("",size=(30, 2),background_color="white",text_color="black",key="-nome-" )],
                    [sg.Text("",size=(30, 10),background_color="white",text_color="black",key="-desc-" )],
                    [sg.Button(CJ.jogo.inimigo.cartas["Carta 1"].nome, key="Info1"+CJ.jogo.inimigo.cartas["Carta 1"].nome),sg.Button(CJ.jogo.inimigo.cartas["Carta 2"].nome, key="Info2"+CJ.jogo.inimigo.cartas["Carta 2"].nome)],
                    [sg.Button(CJ.jogo.inimigo.cartas["Carta 3"].nome, key="Info3"+CJ.jogo.inimigo.cartas["Carta 3"].nome),sg.Button(CJ.jogo.inimigo.cartas["Carta 4"].nome, key="Info4"+CJ.jogo.inimigo.cartas["Carta 4"].nome)]
                        ]

                layout = [[sg.Column(jogador),sg.Text("Turno Atual:"+str(6-int(CJ.jogo.batalha.rodadas))),sg.Column(inimigo)]]


                window = sg.Window('BATALHA', layout)

                
                while True:
                        event, value = window.read()
                        if list(event)[0] == "D":
                            carta = event.replace("DefinirCarta","")
                            carta = list(carta)
                            ordem = carta[0]
                            del carta[0]
                            carta = "".join(carta) 
                            window["-nome-"].update(DCC[carta].nome)
                            window["-desc-"].update(DCC[carta].desc)  
                        elif list(event)[0] == "I":
                            carta = event.replace("Info","")
                            carta = list(carta)
                            if carta[0] in snumeros:
                                del carta[0]
                            carta = "".join(carta)
                            layout2 = [[sg.Text(DCC[carta].nome)],
                                    [sg.Text(DCC[carta].desc)],
                                    [sg.Button("OK")]
                                    ]
                            janelinha = sg.Window("Carta",layout2) 
                            event, value = janelinha.read()
                            janelinha.close()
                        else:
                            CJ.jogo.batalha.segundarodada[0] = carta
                            CJ.jogo.jogador.cartas.pop("Carta "+ordem)
                            FG.passarvez()
                            window.close()
                            break
                continue