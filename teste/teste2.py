import PySimpleGUI as sg

nome = "VISH"
desc = "MARIA"

cartas = {
    "Carta 1":["Bola de Fogo","Lança uma poderosíssima bola de fogo"],
    "Carta 2":["Soco potente", "Desfere um murraço imprevisível"],
    "Carta 3":["Cuspe Ácido", "Lança um esguicho de solução corrosiva"],
    "Carta 4":["3 Oitão", "O alvo vira queijo suíço"]
        }



col = [[sg.Text('Vida'), sg.T(' '  * 3), sg.Text("Valor da vida")],
    [sg.Text('Mente'), sg.T(' '  * 3), sg.Text('Valor da mente')],
    [sg.T(' '  * 3)],
    [sg.Text(text="Nome",size=(30,2),key="-NOME-")],
    [sg.Text(text='Desc',size=(29, 10), key="-DESC-",background_color="white",text_color="black" )],
    [sg.Button('Carta 1'), sg.Button('Carta 2')],
    [sg.Button('Carta 3'), sg.Button('Carta 4')]]

layout = [[sg.Column(col)],
        [sg.OK()]]

# Display the window and get values

window = sg.Window('Compact 1-line window with column', layout)

    
while True:
        event, value = window.read()
        if list(event)[0] == "C": 
            window["-NOME-"].update(cartas[event][0])
            window["-DESC-"].update(cartas[event][1])
        else:
            print(event)
            print(value)
            print("olá")
            break

window.close()
    