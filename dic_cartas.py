import classe_carta as CC
import numpy as np


DCC = {}

cartas = []

with open("Cartas Formatadas.txt","r", encoding="utf-8") as f:
    cartas = f.readlines()

for carta in cartas:
    cs = carta.split("—")
    DCC.update({int(cs[0]):CC.Carta(int(cs[0]),cs[1],cs[2],None,cs[3])})


def imprimirDCC():

    j = 0

    while j < len(DCC):
        print(DCC[j].id)
        print(DCC[j].nome)
        print(DCC[j].tipo)
        print(DCC[j].desc)
        print("")
        j = j+1

#imprimirDCC()