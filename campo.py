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
        CJ.jogo.campo[j][k] = CC.Casa(j,k,None,None)

imprimirCampo()
sg.popup(CJ.jogo.modo)


while True:

    if CJ.jogo.modo[0] == "Edição":
        comando("")
        imprimirCampo()

    if CJ.jogo.modo[0] == "Sair":
        break
        
    while CJ.jogo.modo[1] == "Movimentação":
        if CJ.jogo.modo[0] == "Sair":
            break   
        if CJ.jogo.modo[2] == "":
            imprimirCampo()
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
            if CJ.jogo.movimentoJ == None: 
                CJ.jogo.movimentoJ = CM.Movimento(CJ.jogo.jogador)
            if CJ.jogo.movimentoI == None: 
                CJ.jogo.movimentoI = CM.Movimento(CJ.jogo.inimigo)
            if CJ.jogo.movimentoJ.movimentorestante <= 0:
                if CJ.jogo.movimentoI.movimentorestante <= 0:
                    FG.batalha()
                    imprimirCampo()
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
                    imprimirCampo()
                else: 
                    CJ.jogo.movimentoJ.direcionar(event)
                    imprimirCampo()
        elif CJ.jogo.modo[2] == "I":
            if CJ.jogo.movimentoI == None: CJ.jogo.movimentoI = CM.Movimento(CJ.jogo.inimigo)
            if CJ.jogo.movimentoJ == None: CJ.jogo.movimentoJ = CM.Movimento(CJ.jogo.jogador)
            if CJ.jogo.movimentoJ.movimentorestante != None and CJ.jogo.movimentoI.movimentorestante != None: 
                if CJ.jogo.movimentoI.movimentorestante <= 0:
                    if CJ.jogo.movimentoJ.movimentorestante <= 0:
                        FG.batalha()
                        imprimirCampo()
                    else: FG.passarvez()
                else:
                    CJ.jogo.movimentoI.direcionar("?")
        imprimirCampo()
    imprimirCampo()
    
    while CJ.jogo.modo[1] == "Batalha":
        if CJ.jogo.batalha == None:
            CJ.jogo.batalha = CB.Batalha()
            sg.popup("A BATALHA COMEÇOU")
        botoes = FG.definirBotões()
        sg.popup("tamo aqui em cima")
        if CJ.jogo.batalha.estagio == -1:
            if CJ.jogo.batalha.primeirarodada[0] != None and CJ.jogo.batalha.primeirarodada[1] != None:
                CJ.jogo.batalha.estagio = 1
        elif CJ.jogo.batalha.segundarodada[0] != None and CJ.jogo.batalha.segundarodada[1] != None:
            CJ.jogo.batalha.resolverRodadas()


        if CJ.jogo.modo[2] == "I":
            numero = np.random.randint(len(CJ.jogo.inimigo.cartas))+1
            carta = CJ.jogo.inimigo.cartas["Carta "+str(numero)]
            if CJ.jogo.batalha.estagio == -1:
                CJ.jogo.batalha.primeirarodada[1] = carta
                CJ.jogo.inimigo.cartas.pop("Carta "+str(numero))
                CJ.jogo.inimigo.organizarCartas()
            elif CJ.jogo.batalha.estagio == 1:
                CJ.jogo.batalha.segundarodada[1] = carta
                CJ.jogo.inimigo.cartas.pop("Carta "+str(numero))
                CJ.jogo.inimigo.organizarCartas()
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
                    [botoes[1],botoes[2]],
                    [botoes[3],botoes[4]],
                    [botoes[5],botoes[6]],
                    [botoes[7],botoes[8]],
                    [botoes[9],botoes[10]]
                            ]
 
                inimigo = [
                    [sg.Text('Nome:'), sg.T(' '  * 3), sg.Text(CJ.jogo.inimigo.nome)],
                    [sg.Text('Vida'), sg.T(' '  * 3), sg.Text(CJ.jogo.inimigo.vida)],
                    [sg.Text('Mente'), sg.T(' '  * 3), sg.Text(CJ.jogo.inimigo.mente)],
                    [sg.T(' '  * 3)],
                    [botoes[23]],
                    [botoes[24]],
                    [botoes[11],botoes[12]],
                    [botoes[13],botoes[14]],
                    [botoes[15],botoes[16]],
                    [botoes[17],botoes[18]],
                    [botoes[19],botoes[20]]
                      ]

                layout = [[sg.Column(jogador),sg.Text("Turno Atual:"+str(6-int(CJ.jogo.batalha.rodadas))),sg.Column(inimigo)]]


                window = sg.Window('BATALHA', layout)

                
                while True:
                        event, value = window.read()
                        if list(event)[0] == "D":
                            carta = event.replace("DefinirCarta","")
                            window["-nome-"].update(CJ.jogo.jogador.cartas["Carta"+carta].nome)
                            window["-desc-"].update(CJ.jogo.jogador.cartas["Carta"+carta].tipo+"\n"+CJ.jogo.jogador.cartas["Carta"+carta].desc)  
                        elif list(event)[0] == "I":
                            carta = event.replace("InfoCarta","")
                            layout2 = [[sg.Text(CJ.jogo.inimigo.cartas["Carta"+carta].nome)],
                                    [sg.Text(CJ.jogo.inimigo.cartas["Carta"+carta].tipo+"\n"+CJ.jogo.inimigo.cartas["Carta"+carta].desc)],
                                    [sg.Button("OK")]
                                    ]
                            janelinha = sg.Window("Carta",layout2) 
                            event, value = janelinha.read()
                            janelinha.close()
                        else:
                            CJ.jogo.batalha.primeirarodada[0]=CJ.jogo.jogador.cartas["Carta"+carta]
                            CJ.jogo.jogador.cartas.pop("Carta"+carta)
                            CJ.jogo.jogador.organizarCartas()
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
                    [botoes[21]],
                    [sg.Text("",size=(30, 2),background_color="white",text_color="black",key="-nome-" )],
                    [sg.Text("Selecione uma carta abaixo",size=(30, 10),background_color="white",text_color="black",key="-desc-" )],
                    [sg.Checkbox('Ocultar?'), sg.Checkbox('Preservar?'), sg.Button("OK")],
                    [botoes[1],botoes[2]],
                    [botoes[3],botoes[4]],
                    [botoes[5],botoes[6]],
                    [botoes[7],botoes[8]],
                    [botoes[9],botoes[10]]
                    ]

                inimigo = [
                    [sg.Text('Nome:'), sg.T(' '  * 3), sg.Text(CJ.jogo.inimigo.nome)],
                    [sg.Text('Vida'), sg.T(' '  * 3), sg.Text(CJ.jogo.inimigo.vida)],
                    [sg.Text('Mente'), sg.T(' '  * 3), sg.Text(CJ.jogo.inimigo.mente)],
                    [sg.T(' '  * 3)],
                    [botoes[22]],
                    [botoes[25]],
                    [botoes[26]],
                    [botoes[11],botoes[12]],
                    [botoes[13],botoes[14]],
                    [botoes[15],botoes[16]],
                    [botoes[17],botoes[18]],
                    [botoes[19],botoes[20]]
                        ]

                layout = [[sg.Column(jogador),sg.Text("Turno Atual:"+str(6-int(CJ.jogo.batalha.rodadas))),sg.Column(inimigo)]]


                window = sg.Window('BATALHA', layout)

                
                while True:
                        event, value = window.read()
                        if list(event)[0] == "D":
                            carta = event.replace("DefinirCarta","")
                            window["-nome-"].update(CJ.jogo.jogador.cartas["Carta"+carta].nome)
                            window["-desc-"].update(CJ.jogo.jogador.cartas["Carta"+carta].tipo+"\n"+CJ.jogo.jogador.cartas["Carta"+carta].desc)  
                        elif list(event)[0] == "I":
                            carta = event.replace("InfoCarta","")
                            layout2 = [[sg.Text(CJ.jogo.inimigo.cartas["Carta"+carta].nome)],
                                    [sg.Text(CJ.jogo.inimigo.cartas["Carta"+carta].tipo+"\n"+CJ.jogo.inimigo.cartas["Carta"+carta].desc)],
                                    [sg.Button("OK")]
                                    ]
                            janelinha = sg.Window("Carta",layout2) 
                            event, value = janelinha.read()
                            janelinha.close()
                        elif event == "Rever Carta J":
                            layout2 = [[sg.Text(CJ.jogo.batalha.primeirarodada[0].nome)],
                                    [sg.Text(CJ.jogo.batalha.primeirarodada[0].tipo+"\n"+CJ.jogo.batalha.primeirarodada[0].desc)],
                                    [sg.Button("OK")]
                                    ]
                            janelinha = sg.Window("Carta",layout2) 
                            event, value = janelinha.read()
                            janelinha.close()
                        elif event == "Rever Carta I":
                            layout2 = [[sg.Text(CJ.jogo.batalha.primeirarodada[1].nome)],
                                    [sg.Text(CJ.jogo.batalha.primeirarodada[1].tipo+"\n"+CJ.jogo.batalha.primeirarodada[1].desc)],
                                    [sg.Button("OK")]
                                    ]
                            janelinha = sg.Window("Carta",layout2) 
                            event, value = janelinha.read()
                            janelinha.close()
                        else:
                            CJ.jogo.batalha.primeirarodada[0]=CJ.jogo.jogador.cartas["Carta"+carta]
                            CJ.jogo.jogador.cartas.pop("Carta"+carta)
                            CJ.jogo.jogador.organizarCartas()
                            FG.passarvez()
                            window.close()
                            break
                continue