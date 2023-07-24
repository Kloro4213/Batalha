import PySimpleGUI as sg

cartas = {
    "Carta 1":["Bola de Fogo","Lança uma poderosíssima bola de fogo"],
    "Carta 2":["Soco potente", "Desfere um murraço imprevisível"],
    "Carta 3":["Cuspe Ácido", "Lança um esguicho de solução corrosiva"],
    "Carta 4":["3 Oitão", "O alvo vira queijo suíço"]
        }





jogador = [[sg.Text('Vida'), sg.T(' '  * 3), sg.Text("Valor da vida")],
       [sg.Text('Mente'), sg.T(' '  * 3), sg.Text('Valor da mente')],
       [sg.T(' '  * 3)],
       [sg.Text("",size=(30, 2),background_color="white",text_color="black",key="-nome-" )],
       [sg.Text("Selecione uma carta abaixo",size=(30, 10),background_color="white",text_color="black",key="-desc-" )],
       [sg.Checkbox('Ocultar?'), sg.Checkbox('Preservar?'), sg.Button("OK")],
       [sg.Button(cartas['Carta 1'][0],key="Carta 1"),sg.Button(cartas['Carta 2'][0],key="Carta 2")],
       [sg.Button(cartas['Carta 3'][0],key="Carta 3"),sg.Button(cartas['Carta 4'][0],key="Carta 4")]
     ]

inimigo = [[sg.Text('Vida'), sg.T(' '  * 3), sg.Text("Valor da vida")],
       [sg.Text('Mente'), sg.T(' '  * 3), sg.Text('Valor da mente')],
       [sg.T(' '  * 3)],
       [sg.Text("",size=(30, 2),background_color="white",text_color="black",key="-nome-" )],
       [sg.Text("",size=(30, 10),background_color="white",text_color="black",key="-desc-" )],
       [sg.Button(cartas['Carta 1'][0],key="ICarta 1"),sg.Button(cartas['Carta 2'][0],key="ICarta 2")],
       [sg.Button(cartas['Carta 3'][0],key="ICarta 3"),sg.Button(cartas['Carta 4'][0],key="ICarta 4")]
          ]

layout = [[sg.Column(jogador),sg.Column(inimigo)]]


window = sg.Window('BATALHA', layout)

  
while True:
        event, value = window.read()
        if list(event)[0] == "C": 
            window["-nome-"].update(cartas[event][0])
            window["-desc-"].update(cartas[event][1])
        elif list(event)[0] == "I":
            carta = event.replace("I","")
            layout2 = [[sg.Text(cartas[carta][0])],
                    [sg.Text(cartas[carta][1])],
                    [sg.Button("OK")]
                    ]
            janelinha = sg.Window("Carta",layout2) 
            event, value = janelinha.read()
            janelinha.close()  
        else:
            print(event)
            print(list(event))
            print("olá")
            break

window.close()
