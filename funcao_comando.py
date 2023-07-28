import numpy as np
import PySimpleGUI as sg
from colorama import Fore, Back, Style
import classe_jogo as CJ
import funcoes_gerais as FG


def comando(entrada):
    if entrada is "":
        comando = sg.popup_get_text('Entrada', 'O que fazer?')
    else: comando = entrada
    if comando == "":
        op = ""
    else:
        op = "".join([list(comando)[0],list(comando)[1]])
    item = comando.replace(op,"")
    match op:
        case "XX":
            CJ.jogo.modo[0] = "Sair"
        case "IT":
            local = ""
            local = local + str(np.random.randint(7))
            local = local + str(np.random.randint(7))
            local = list(local)
            y = int(local[0])
            x = int(local[1])
            FG.invocarJogador(CJ.jogo.campo,y,x,"Kloro")
            local = ""
            local = local + str(np.random.randint(7))
            local = local + str(np.random.randint(7))
            local = list(local)
            y = int(local[0])
            x = int(local[1])
            FG.invocarInimigo(CJ.jogo.campo,y,x,"Lutécio")
        case "CC":
            local = sg.popup_get_text('Localização da checagem', 'Qual casa você quer checar?')
            local = list(local)
            y = FG.N(local[0])
            xmesmo = local[0]
            x = int(local[1])-1
            ymesmo = str(x+1)
            if CJ.jogo.campo[y][x].ocupante == None:
                ocupante = "Ninguém"
            else: ocupante = CJ.jogo.campo[y][x].ocupante.nome
            if CJ.jogo.campo[y][x].carta == None:
                carta = "Nada"
            else: carta = CJ.jogo.campo[y][x].carta.nome
            layout = [                   
                    [sg.Text("Ocupante da Casa "+xmesmo+ymesmo+": "+ocupante)],
                    [sg.Text("Carta na Casa "+xmesmo+ymesmo+": "+carta)],
                    ]
            window = sg.Window("Movimentação",layout)
            event, values = window.read()
            print(event)
            print(values)
            window.close()
        case "??":
            return FG.buscarItem(item)
        case "IJ":
            local = sg.popup_get_text('Localização da invocação', 'Em qual casa o jogador será invocado?')
            local = list(local)
            y = FG.N(local[0])
            x = int(local[1])-1
            FG.invocarJogador(CJ.jogo.campo,y,x)
        case "II":
            local = sg.popup_get_text('Localização da invocação', 'Em qual casa o inimigo será invocado?')
            local = list(local)
            y = FG.N(local[0])
            x = int(local[1])-1
            FG.invocarInimigo(CJ.jogo.campo,y,x)
        case "CJ":
            if CJ.jogo.teminimigo == False:
                sg.popup("Primeiro invoque um inimigo!")
            elif CJ.jogo.temjogador == False:
                sg.popup("Primeiro invoque um jogador!")
            else:
                CJ.jogo.definirbaralhos()
                FG.ReporCampo()
                sg.popup("O CJ.jogo realmente começou")
                CJ.jogo.modo[1] = "Movimentação"
                CJ.jogo.modo[0] = "Jogo"
        case "IN":
            for carta in CJ.jogo.jogador.cartas:
                sg.popup(carta+" do jogador: "+CJ.jogo.jogador.cartas[carta].nome)
            for carta in CJ.jogo.inimigo.cartas:
                sg.popup(carta+" do inimigo: "+CJ.jogo.inimigo.cartas[carta].nome)