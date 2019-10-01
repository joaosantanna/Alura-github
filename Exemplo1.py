'''
O programa vai pegar o nome e a idade da pessoa
e informar o ano de nascimento ...

feito com PySimpleGUI
'''

import PySimpleGUI as sg

fonte = ('Helvetica', 18)
layout = [
    [sg.Text('Informe sua idade')],
    [sg.Text('Nome:'), sg.InputText()],
    [sg.Text('idade:'), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]

janela = sg.Window('Primeiro programa de teste',
                   font=fonte).Layout(layout)
botao, valores = janela.Read()

print(botao, valores[0], valores[1])

nome = valores[0]
ano_nascimento = 2019 - int(valores[1])
mensagem = 'Bom dia ' + nome + '\n você nasceu em ' + str(ano_nascimento)
print(mensagem)

sg.Popup(mensagem, font=fonte)
