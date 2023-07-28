import PySimpleGUI as sg
import numpy as np

cartas = {
    "Bola de Fogo":"Lança uma poderosíssima bola de fogo",
    "Soco potente": "Desfere um murraço imprevisível",
    "Cuspe Ácido": "Lança um esguicho de solução corrosiva",
    "3 Oitão": "O alvo vira queijo suíço"}

cartos = ["Bola de Fogo","Soco potente","Cuspe Ácido","3 Oitão"]

escolha = cartas[cartos[np.random.randint(len(cartos))]]




layout = [
    []



]


