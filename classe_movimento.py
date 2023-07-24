import numpy as np
import PySimpleGUI as sg
from colorama import Fore, Back, Style
import funcoes_gerais as FG
import classe_jogo as CJ

class Movimento:
    def __init__(self,dono):
        if dono is not None:
            self.dono = dono
            self.casainicial = FG.obtercasa(dono.y,dono.x)
            self.casaatual = self.casainicial
            self.casasdisponíveis = None
            self.movimentorestante = 5
        else:
            self.dono = None
            self.casainicial = None
            self.casaatual = None
            self.casasdisponíveis = None
            self.movimentorestante = None
        self.caminho = []


    def direcionar(self,letra):
        destino = ""
        if self.movimentorestante == 0:
            sg.popup("Não há mais movimentos restantes")
        else:
            #print('Minha casa agora é: '+self.casaatual.carta.nome)
            match letra:
                case '?':
                    if self.caminho == []: 
                        self.casasdisponíveis = self.casaatual.obterVizinhos()
                    else:
                        for casa in self.caminho:
                            self.casasdisponíveis = casa.obterVizinhos()
                    self.casasdisponíveis = list(dict.fromkeys(self.casasdisponíveis))
                    for casa in self.casasdisponíveis:
                        if casa.ocupante != None:
                            self.casasdisponíveis.remove(casa)
                        elif casa.visitado != None and casa.visitado != self.dono:
                            self.casasdisponíveis.remove(casa)
                    destino = self.casasdisponíveis[np.random.randint(len(self.casasdisponíveis))]
                case "W":
                    if self.movimentorestante > 0:
                        if self.dono.x == 0:
                            sg.popup("Você não pode se mover aí!")
                        else: 
                            destino = CJ.jogo.campo[self.casaatual.y-1][self.casaatual.x]
                    else:
                        sg.popup("Não há mais movimentos restantes")
                        FG.passarvez()
                case "A":
                    if self.movimentorestante > 0:
                        if self.dono.x == 0:
                            sg.popup("Você não pode se mover aí!")
                        else: destino = CJ.jogo.campo[self.casaatual.y][self.casaatual.x-1]
                    else:
                        sg.popup("Não há mais movimentos restantes")
                        FG.passarvez()
                case "S":
                    if self.movimentorestante > 0:
                        if self.dono.y == 6:
                            sg.popup("Você não pode se mover aí!")
                        else: destino = CJ.jogo.campo[self.casaatual.y+1][self.casaatual.x]
                    else:
                        sg.popup("Não há mais movimentos restantes")
                        FG.passarvez()
                case "D":
                    if self.movimentorestante > 0:
                        if self.dono.x == 6:
                            sg.popup("Você não pode se mover aí!")
                        else: destino = CJ.jogo.campo[self.casaatual.y][self.casaatual.x+1]
                    else:
                        sg.popup("Não há mais movimentos restantes")
                        FG.passarvez()
            if self.caminho == []: 
                self.casasdisponíveis = self.casaatual.obterVizinhos()
            else:
                for casa in self.caminho:
                    self.casasdisponíveis += casa.obterVizinhos()
            self.casasdisponíveis = list(dict.fromkeys(self.casasdisponíveis))
            for casa in self.casasdisponíveis:
                        if casa.ocupante != None:
                            self.casasdisponíveis.remove(casa)
                        elif casa.visitado != None and casa.visitado != self.dono:
                            self.casasdisponíveis.remove(casa)
            if destino in self.casasdisponíveis:
                self.casaatual.ocupante = None
                self.casaatual = destino
                self.casaatual.ocupante = self.dono
                self.dono.x = destino.x
                self.dono.y = destino.y
                if destino.carta != None:
                    self.dono.cartas.update({"Carta "+str(len(self.dono.cartas)+1):destino.carta})
                    destino.carta = None
                if destino not in self.caminho:
                    self.caminho.append(destino)
                    destino.visitado = self.dono
                    self.movimentorestante -= 1
                    FG.passarvez()        
            else:
                sg.popup("Você não pode se mover aí!")