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
                        corsim = Back.GREEN
                        formatacao = Fore.LIGHTGREEN_EX
            if CJ.jogo.movimentoI != None:
                if CJ.jogo.movimentoI.caminho != None:
                    if casa in CJ.jogo.movimentoI.caminho:
                        corsim = Back.RED
                        formatacao = Fore.LIGHTRED_EX
            ocupante = casa.ocupante
            if ocupante == None:
                ocupantenome = ""
            else:
                ocupantenome = ocupante.nome
                if ocupante == CJ.jogo.jogador:
                    formatacao = Fore.LIGHTGREEN_EX
                elif ocupante == CJ.jogo.inimigo:
                    formatacao = Fore.LIGHTRED_EX
                else: formatacao = ""
            print("|"+formatacao+corsim+textoC.format(ocupantenome)+final+cornao,end="")
        print("|")
        for casa in fileira:
            formatacao = Fore.WHITE
            final = Fore.WHITE
            corsim = Back.BLACK
            cornao = Back.BLACK
            if casa.carta != None:
                if casa.carta.id in CJ.jogo.jogador.baralho:
                    corsim = Back.LIGHTGREEN_EX
                elif casa.carta.id in CJ.jogo.inimigo.baralho:
                    corsim = Back.LIGHTRED_EX
                elif casa.carta.id in CJ.jogo.baralhoregional:
                    corsim = Back.LIGHTBLUE_EX
                if casa.carta.tipo == "Ataque":
                    formatacao = Fore.LIGHTYELLOW_EX
                elif casa.carta.tipo == "Manobra":
                    formatacao = Fore.LIGHTCYAN_EX
                elif casa.carta.tipo == "Talento":
                    formatacao = Fore.LIGHTMAGENTA_EX
            if CJ.jogo.movimentoJ != None:
                if CJ.jogo.movimentoJ.caminho != None:
                    if casa in CJ.jogo.movimentoJ.caminho:
                        corsim = Back.GREEN
            if CJ.jogo.movimentoI != None:
                if CJ.jogo.movimentoI.caminho != None:
                    if casa in CJ.jogo.movimentoI.caminho:
                        corsim = Back.RED
            print("|"+formatacao+corsim+textoC.format("")+final+cornao,end="")
        print("|")        
        for casa in fileira:
            formatacao = Fore.WHITE
            final = Fore.WHITE
            corsim = Back.BLACK
            cornao = Back.BLACK
            if casa.carta != None:
                if casa.carta.id in CJ.jogo.jogador.baralho:
                    corsim = Back.LIGHTGREEN_EX
                elif casa.carta.id in CJ.jogo.inimigo.baralho:
                    corsim = Back.LIGHTRED_EX
                elif casa.carta.id in CJ.jogo.baralhoregional:
                    corsim = Back.LIGHTBLUE_EX
                if casa.carta.tipo == "Ataque":
                    formatacao = Fore.LIGHTYELLOW_EX
                elif casa.carta.tipo == "Manobra":
                    formatacao = Fore.LIGHTCYAN_EX
                elif casa.carta.tipo == "Talento":
                    formatacao = Fore.LIGHTMAGENTA_EX
            if CJ.jogo.movimentoJ != None:
                if CJ.jogo.movimentoJ.caminho != None:
                    if casa in CJ.jogo.movimentoJ.caminho:
                        corsim = Back.GREEN
            if CJ.jogo.movimentoI != None:
                if CJ.jogo.movimentoI.caminho != None:
                    if casa in CJ.jogo.movimentoI.caminho:
                        corsim = Back.RED
            carta = casa.carta
            if carta == None:
                cartanome = ""
            else:
                cartanome = carta.nome
            print("|"+formatacao+corsim+textoC.format(cartanome)+cornao,end="")
        print("|")

        print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")

