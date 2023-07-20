import numpy as np
import PySimpleGUI as sg
from colorama import Fore, Back, Style




class CCasa:
    def __init__(self,y,x,carta=None,ocupante=None,visitado=None):
        self.y = y
        self.x = x
        self.carta = carta
        self.ocupante=ocupante
        self.visitado=visitado

    def definirOcupante(self,ocupante):
        self.ocupante = ocupante
    
    def definirCarta(self,carta):
        self.carta = carta

    def obterVizinhos(self):
        vizinhos = []
        if self.y > 0:
            vizinho = CAMPO[self.y-1][self.x]
            vizinhos.append(vizinho)
            #print(vizinho.carta.nome+" é adjacente a mim, "+self.carta.nome)

        if self.y < 6:
            vizinho = CAMPO[self.y+1][self.x]
            vizinhos.append(vizinho)
            #print(vizinho.carta.nome+" é adjacente a mim, "+self.carta.nome)
        if self.x > 0:
            vizinho = CAMPO[self.y][self.x-1]
            vizinhos.append(vizinho)
            #print(vizinho.carta.nome+" é adjacente a mim, "+self.carta.nome)
        if self.x < 6:
            vizinho = CAMPO[self.y][self.x+1]
            vizinhos.append(vizinho)
            #print(vizinho.carta.nome+" é adjacente a mim, "+self.carta.nome)
        return vizinhos
    
class CJogo:
    def __init__(self):
        self.temjogador = False
        self.teminimigo = False
        self.jogador = None
        self.inimigo = None
        self.movimentoJ = CMovimento(None)
        self.movimentoI = CMovimento(None)



class CMovimento:
    def __init__(self,dono):
        if dono is not None:
            self.dono = dono
            self.casainicial = obtercasa(dono.y,dono.x)
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
                            destino = CAMPO[self.casaatual.y-1][self.casaatual.x]
                    else:
                        sg.popup("Não há mais movimentos restantes")
                        passarvez()
                case "A":
                    if self.movimentorestante > 0:
                        if self.dono.x == 0:
                            sg.popup("Você não pode se mover aí!")
                        else: destino = CAMPO[self.casaatual.y][self.casaatual.x-1]
                    else:
                        sg.popup("Não há mais movimentos restantes")
                        passarvez()
                case "S":
                    if self.movimentorestante > 0:
                        if self.dono.y == 6:
                            sg.popup("Você não pode se mover aí!")
                        else: destino = CAMPO[self.casaatual.y+1][self.casaatual.x]
                    else:
                        sg.popup("Não há mais movimentos restantes")
                        passarvez()
                case "D":
                    if self.movimentorestante > 0:
                        if self.dono.x == 6:
                            sg.popup("Você não pode se mover aí!")
                        else: destino = CAMPO[self.casaatual.y][self.casaatual.x+1]
                    else:
                        sg.popup("Não há mais movimentos restantes")
                        passarvez()
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
                if destino not in self.caminho:
                    self.caminho.append(destino)
                    destino.visitado = self.dono
                    self.movimentorestante -= 1
                    passarvez()        
            else:
                sg.popup("Você não pode se mover aí!")


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

class CCarta:
    def __init__(self,nome=None,efeito=None,dono=None):
        self.nome = nome
        self.efeito = efeito
        self.dono = dono

jogo = CJogo()
letras = ['A','B','C','D','E','F','G']

print(jogo.temjogador)

def batalha():
    sg.popup("A Batalha não existe ainda :)")
    modo[0] = "Edição"
    modo[1] = ""
    modo[2] = ""

def invocarJogador(campo,y,x):
    if jogo.temjogador == True:
        sg.popup("Não podem haver dois jogadores!")
        print(jogo.jogador.x,jogo.jogador.y)
    else:
        Kloro = CJogador(None,None,100)
        campo[y][x].ocupante = Kloro
        Kloro.y = y
        Kloro.x = x
        jogo.temjogador = True
        jogo.jogador = Kloro

def invocarInimigo(campo,y,x):
    if jogo.teminimigo == True:
        sg.popup("Não podem haver dois inimigos!")
    else:
        inimigo = CInimigo(None,None,100)
        campo[y][x].ocupante = inimigo
        inimigo.y = y
        inimigo.x = x
        jogo.teminimigo = True
        jogo.inimigo = inimigo

def passarvez():
    if modo[2] == "I":
        modo[2] = "J"
    else:
        modo[2] = "I"

def obtercasa(y,x):
    if type(y) == str:
        return CAMPO[N(y)][(int(x))-1]
    elif type(y) == int:
        return CAMPO[y][x]

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

def comando(entrada):
    if entrada is "":
        comando = sg.popup_get_text('Entrada', 'O que fazer?')
    else: comando = entrada
    op = "".join([list(comando)[0],list(comando)[1]])
    item = comando.replace(op,"")
    match comando[0]+comando[1]:
        case "XX":
            modo[0] = "Sair"
        case "IT":
            local = ""
            local = local + str(np.random.randint(7))
            local = local + str(np.random.randint(7))
            local = list(local)
            y = int(local[0])
            x = int(local[1])
            invocarJogador(CAMPO,y,x)
            local = ""
            local = local + str(np.random.randint(7))
            local = local + str(np.random.randint(7))
            local = list(local)
            y = int(local[0])
            x = int(local[1])
            invocarInimigo(CAMPO,y,x)
        case "CC":
            local = sg.popup_get_text('Localização da checagem', 'Qual casa você quer checar?')
            local = list(local)
            y = N(local[0])
            xmesmo = local[0]
            x = int(local[1])-1
            ymesmo = str(x+1)
            if CAMPO[y][x].ocupante == None:
                ocupante = "Ninguém"
            else: ocupante = CAMPO[y][x].ocupante.nome
            if CAMPO[y][x].carta == None:
                carta = "Nada"
            else: carta = CAMPO[y][x].carta.nome
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
            return buscaritem(item)
        case "IJ":
            local = sg.popup_get_text('Localização da invocação', 'Em qual casa o jogador será invocado?')
            local = list(local)
            y = N(local[0])
            x = int(local[1])-1
            invocarJogador(CAMPO,y,x)
        case "II":
            local = sg.popup_get_text('Localização da invocação', 'Em qual casa o inimigo será invocado?')
            local = list(local)
            y = N(local[0])
            x = int(local[1])-1
            invocarInimigo(CAMPO,y,x)
        case "CJ":
            if jogo.teminimigo == False:
                sg.popup("Primeiro invoque um inimigo!")
            elif jogo.temjogador == False:
                sg.popup("Primeiro invoque um jogador!")
            else:
                modo[1] = "Movimentação"
                modo[0] = "Jogo"

def imprimirCampo(campo):
    textoE = "{:<9}"
    textoC = "{:^9}"
    textoD = "{:>9}"
    print("_______________________________________________________________________")
    for fileira in campo:
        for casa in fileira:
            formatacao = Fore.WHITE
            final = Fore.WHITE
            corsim = Back.BLACK
            cornao = Back.BLACK
            ocupante = casa.ocupante
            if ocupante == None:
                ocupantenome = ""
            else:
                ocupantenome = ocupante.nome
                if ocupante == jogo.jogador:
                    formatacao = Fore.GREEN
                elif ocupante == jogo.inimigo:
                    formatacao = Fore.RED
                else: formatacao = ""
            print("|"+formatacao+corsim+textoC.format(ocupantenome)+final+cornao,end="")
        print("|")
        for casa in fileira:
            formatacao = Fore.WHITE
            final = Fore.WHITE
            corsim = Back.BLACK
            cornao = Back.BLACK
            if jogo.movimentoJ.caminho != None:
                if casa in jogo.movimentoJ.caminho:
                    corsim = Back.LIGHTGREEN_EX
            if jogo.movimentoI.caminho != None:
                if casa in jogo.movimentoI.caminho:
                    corsim = Back.LIGHTRED_EX
            print("|"+formatacao+corsim+textoC.format("")+final+cornao,end="")
        print("|")        
        for casa in fileira:
            formatacao = Fore.WHITE
            final = Fore.WHITE
            corsim = Back.BLACK
            cornao = Back.BLACK
            carta = casa.carta
            if carta == None:
                cartanome = ""
            else:
                cartanome = carta.nome
            print("|"+formatacao+corsim+textoC.format(cartanome),end="")
        print("|")

        print("———————————————————————————————————————————————————————————————————————")


CAMPO = np.empty([7, 7], dtype = CCasa)


for j in range(7):
    for k in range(7):
        CAMPO[j][k] = CCasa(j,k,CCarta(letras[j]+str(k+1)))

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
                jogo.movimentoJ = CMovimento(jogo.jogador)
                sg.popup("o movimento do jogador começou")
            if jogo.movimentoJ.movimentorestante <= 0:
                if jogo.movimentoJ.movimentorestante != None and jogo.movimentoI.movimentorestante != None:  
                    if jogo.movimentoJ.movimentorestante <= 0:
                        if jogo.movimentoI.movimentorestante <= 0:
                            batalha()
                        else: passarvez()
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
                jogo.movimentoI = CMovimento(jogo.inimigo)
                sg.popup("o movimento do inimigo começou")
            if jogo.movimentoJ.movimentorestante != None and jogo.movimentoI.movimentorestante != None:  
                if jogo.movimentoJ.movimentorestante <= 0:
                    if jogo.movimentoI.movimentorestante <= 0:
                        batalha()
                    else: passarvez()
            jogo.movimentoI.direcionar("?")
        imprimirCampo(CAMPO)
            
