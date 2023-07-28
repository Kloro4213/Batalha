import classe_carta as CC


class cartinha:
    def __init__ (self,texto,id):
        self.id = id
        self.texto = texto.split(" — ",2)
        self.nome = self.texto[0]
        self.tipo = self.texto[1]
        self.desc = self.texto[2].replace("\n","")
    





with open("Cartas.txt", "r", encoding="utf-8") as f:
    cartastodas = f.readlines()
    f.close()

print(cartastodas[0])
print(cartastodas[1])
print(cartastodas[2])
print(cartastodas[3])




i = 0
while True:
    print(i)
    cartastodas[i] = cartinha(cartastodas[i],i)
    i = i+1
    if i == len(cartastodas):
        break

with open("Cartas Formatadas.txt", "w", encoding="utf-8") as f:
    for carta in cartastodas:
        f.write(str(carta.id)+"—"+""+carta.nome+"—"+carta.tipo+"—"+carta.desc+"\n")
    f.close()