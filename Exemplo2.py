'''
Programa para calcular a raiz quadrada de um 
numero
'''

import PySimpleGUI as sg
from math import sqrt

fonte = ('Helvetica', 16)
janela = sg.Window('Raiz quadrada', font=fonte)

layout = [
    [sg.Text('Valor:'), sg.Input(
        'digite o valor da raiz que vc quer calcular')],
    [sg.T('Resultado:'), sg.Input('resultado', key='resultado')],
    [sg.Button('Calcular'), sg.Button('Sair')]
]

janela.Layout(layout)

while True:
    botao, valores = janela.Read()

    if botao == 'Calcular':
        numero = float(valores[0])
        raiz_quadrada = sqrt(numero)
        janela.FindElement('resultado').Update(raiz_quadrada)
    if botao == 'Sair':
        break

janela.Close()
