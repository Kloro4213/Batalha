import classe_carta as CC


class cartinha:
    def __init__ (self,texto,id):
        self.id = id
        self.texto = texto.split(" — ")
        self.nome = self.texto[0]
        self.tipo = self.texto[1]
        self.rotulo = self.texto[2]
        self.desc = self.texto[3].replace("\n","")
        self.efeito = self.texto[4].replace("\n","")





with open("Cartas.txt", "r", encoding="utf-8") as f:
    cartastodas = f.readlines()
    f.close()



i = 0
while True:
    print(i)
    cartastodas[i] = cartinha(cartastodas[i],i)
    i = i+1
    if i == len(cartastodas):
        break

with open("Cartas Formatadas.txt", "w", encoding="utf-8") as f:
    for carta in cartastodas:
        f.write(str(carta.id)+"—"+""+carta.nome+"—"+carta.tipo+"—"+carta.rotulo+"—"+carta.desc+"—"carta.efeito+"\n")
    f.close()