











import re

negocio = "jogador.vida<40,[receberVida(23),causarDano(op,45)],causarDano(op,32)"

coisa = re.findall(r'\(.*\)|\[.*\]',negocio)

dicreal = {}

for item in coisa:
    dicreal.update({"blob"+str(coisa.index(item)):item})
    negocio = negocio.replace(item,"blob"+str(coisa.index(item)))

negocio = negocio.split(",")

i=0
while i <len(negocio):
    correspondencia = re.findall(r'blob\d',negocio[i])
    for j in range(len(correspondencia)):        
        negocio[i] = negocio[i].replace(correspondencia[j],dicreal[correspondencia[j]])
    i = i+1










expressao = "pneumoltramicroscopicossilicovulconoconiótico"


print(coisa)






def SEPARAR(texto):
    pilha=[""]
    saída = []
    texto = list(texto)
    i = 0
    while i<len(texto):
        if pilha[len(pilha)-1] != "(" and pilha[len(pilha)-1] != "[":
            if texto[i] != "(" and texto[i] != "[":
                i = i+1
            elif texto[i] == "(":
                saída.append("")
                pilha.append("(")
                saída[len(saída)-1] = saída[len(saída)-1]+texto[i]
                i = i+1
            elif texto[i] == "[":
                saída.append("")
                pilha.append("[")
                saída[len(saída)-1] = saída[len(saída)-1]+texto[i]
                i = i+1
        else:
            if texto[i] != ")" and texto[i] != "]":
                saída[len(saída)-1] = saída[len(saída)-1]+texto[i]
                i = i+1
            elif texto[i] == ")" and pilha[len(pilha)-1] == "(":
                saída[len(saída)-1] = saída[len(saída)-1]+texto[i]
                i = i+1
                del pilha[len(pilha)-1]
            elif texto[i] == "]" and pilha[len(pilha)-1] == "[":
                saída[len(saída)-1] = saída[len(saída)-1]+texto[i]
                i = i+1
                del pilha[len(pilha)-1]
            else:
                saída[len(saída)-1] = saída[len(saída)-1]+texto[i]
                i = i+1
    return saída

print(SEPARAR(negocio))



magic = "condicao(jogador.vida<40,perderVida(99),[receberVida(23)+causarDano(op,45)])"

print(SEPARAR(magic))