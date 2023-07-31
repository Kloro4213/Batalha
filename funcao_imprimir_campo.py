import numpy as np
import PySimpleGUI as sg
from colorama import Fore, Back, Style
import classe_casa as CC
import classe_movimento as CM
import classe_carta as CA
import classe_jogo as CJ 

def imprimirCampo():
    textoE = "{:<9}"
    textoC = "{:^29}"
    textoD = "{:>9}"
    print("__________________________________________________________________________________________________________________________________________________________________________________________________________________________")
    for fileira in CJ.jogo.campo:
        for casa in fileira:
            formatacao = Fore.WHITE
            final = Fore.WHITE
            corsim = Back.BLACK
            cornao = Back.BLACK
            if CJ.jogo.movimentoJ != None:
                if CJ.jogo.movimentoJ.caminho != None:
                    if casa in CJ.jogo.movimentoJ.caminho:
                        corsim = Back.LIGHTGREEN_EX
            if CJ.jogo.movimentoI != None:
                if CJ.jogo.movimentoI.caminho != None:
                    if casa in CJ.jogo.movimentoI.caminho:
                        corsim = Back.LIGHTRED_EX
            ocupante = casa.ocupante
            if ocupante == None:
                ocupantenome = ""
            else:
                ocupantenome = ocupante.nome
                if ocupante == CJ.jogo.jogador:
                    formatacao = Fore.GREEN
                elif ocupante == CJ.jogo.inimigo:
                    formatacao = Fore.RED
                else: formatacao = ""
            print("|"+formatacao+corsim+textoC.format(ocupantenome)+final+cornao,end="")
        print("|")
        for casa in fileira:
            formatacao = Fore.WHITE
            final = Fore.WHITE
            corsim = Back.BLACK
            cornao = Back.BLACK
            if CJ.jogo.movimentoJ != None:
                if CJ.jogo.movimentoJ.caminho != None:
                    if casa in CJ.jogo.movimentoJ.caminho:
                        corsim = Back.LIGHTGREEN_EX
            if CJ.jogo.movimentoI != None:
                if CJ.jogo.movimentoI.caminho != None:
                    if casa in CJ.jogo.movimentoI.caminho:
                        corsim = Back.LIGHTRED_EX
            print("|"+formatacao+corsim+textoC.format("")+final+cornao,end="")
        print("|")        
        for casa in fileira:
            formatacao = Fore.WHITE
            final = Fore.WHITE
            corsim = Back.BLACK
            cornao = Back.BLACK
            if CJ.jogo.movimentoJ != None:
                if CJ.jogo.movimentoJ.caminho != None:
                    if casa in CJ.jogo.movimentoJ.caminho:
                        corsim = Back.LIGHTGREEN_EX
            if CJ.jogo.movimentoI != None:
                if CJ.jogo.movimentoI.caminho != None:
                    if casa in CJ.jogo.movimentoI.caminho:
                        corsim = Back.LIGHTRED_EX
            carta = casa.carta
            if carta == None:
                cartanome = ""
            else:
                cartanome = carta.nome
            print("|"+formatacao+corsim+textoC.format(cartanome)+cornao,end="")
        print("|")

        print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")

