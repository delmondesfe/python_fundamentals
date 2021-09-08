import csv

with open('cadastro.CSV','r') as arquivo:
    cadastro = arquivo.readlines()

#cadastro com redlines é uma lista
#O primeiro elemente da lista é o cabeçalho

for registro in cadastro:
    if registro.split(';')[4] == 'rj\n':
        print('CPF:',registro.split(';')[0])
        print('Nome:',registro.split(';')[1])
        print('Idade:',registro.split(';')[2])
        print('Sexo:',registro.split(';')[3])
        print('UF:',registro.split(';')[4])
    

